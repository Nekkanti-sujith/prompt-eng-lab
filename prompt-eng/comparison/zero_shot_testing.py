import sys
import os
import time
import threading
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor
from sentence_transformers import SentenceTransformer, util  
from bert_score import score as bert_score  

# Ensure Python can find `_pipeline.py`
sys.path.append("/Users/sujith/Downloads/prompt-eng-lab/prompt-eng/prompt-eng/prompt-eng-python")
from _pipeline import create_payload, model_req  

# File paths for parameters and output results
parameter_file = "/Users/sujith/Downloads/prompt-eng-lab/prompt-eng/prompt-eng/comparison/parameters.txt"
output_file = "/Users/sujith/Downloads/prompt-eng-lab/prompt-eng/prompt-eng/comparison/zero_shot_prompting_results.txt"

# Load sentence transformer for similarity scoring
similarity_model = SentenceTransformer("all-MiniLM-L6-v2")

# Prompt for testing
prompts = {
    "zero_shot_prompt": """Without prior examples, generate a detailed explanation of how to automate Requirement Analysis for a Space Bot, considering AI, NLP, and process automation techniques. Include strategies for keeping the bot updated with the latest space news and ensuring it understands user queries accurately."""
}

# Load parameters from file
parameters = []
try:
    with open(parameter_file, "r") as file:
        for line in file:
            param_dict = {}
            try:
                for param in line.strip().split(","):
                    key, value = param.split("=")
                    param_dict[key.strip()] = float(value.strip())
                parameters.append(param_dict)
            except ValueError:
                print(f"Skipping invalid parameter line: {line.strip()}")
except FileNotFoundError:
    print(f"Missing parameters file: {parameter_file}. Run `parameter_generator.py` first.")
    exit(1)

results = []
best_overall_score = 0
best_overall_params = None

# Compare generated responses to a reference answer for evaluation
def evaluate_response(response):
    if not response:
        return 0  

    length_score = min(len(response) / 100, 1)  

    reference_answer = "Automating requirement analysis for a Space Bot involves using AI-driven NLP models to extract, classify, and validate functional requirements."

    P, R, F1 = bert_score([response], [reference_answer], lang="en", model_type="roberta-large-mnli")
    similarity_score = F1.mean().item()  

    return (length_score + similarity_score) / 2  

# Process each prompt with given parameters
def process_prompt(name, prompt, param, progress_bar):
    global best_overall_score, best_overall_params

    start_time = time.time()
    payload = create_payload(target="ollama", model="llama3.2:latest", prompt=prompt, **param)
    
    latency, response = model_req(payload=payload)
    response_time = time.time() - start_time if latency is None else latency
    score = evaluate_response(response)

    result_text = (
        f"Prompt: {name}\n"
        f"Parameters: {param}\n"
        f"Response Time: {response_time:.2f}s\n"
        f"Score: {score:.2f}\n"
        f"Response: {response[:300]}...\n"
        f"{'-' * 60}\n"
    )

    results.append((name, param, response_time, score, response))

    if score > best_overall_score:
        best_overall_score = score
        best_overall_params = param  

    with open(output_file, "a") as f:
        f.write(result_text)

    progress_bar.update(1)  

# Run multiple iterations to capture the best result
progress_bar = tqdm(total=len(parameters), desc="Processing Prompts", unit="task")

# Ensure output file is cleared before writing new results
with open(output_file, "w") as f:
    f.write("Zero-Shot Prompting Results\n" + "=" * 60 + "\n\n")

for _ in range(5):  
    for param in parameters:
        process_prompt("zero_shot_prompt", prompts["zero_shot_prompt"], param, progress_bar)

progress_bar.close()

# Store the highest-scoring result
with open(output_file, "a") as f:
    f.write("\nBest Overall Score Across Runs:\n")
    f.write(f"➡️ Score: {best_overall_score:.2f}\n")
    f.write(f"➡️ Parameters: {best_overall_params}\n")

print("\nBest Overall Score Across Runs:")
print(f"➡️ Score: {best_overall_score:.2f}")
print(f"➡️ Parameters: {best_overall_params}")
