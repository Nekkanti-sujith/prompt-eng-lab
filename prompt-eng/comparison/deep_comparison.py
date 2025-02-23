import sys
sys.path.append("/Users/sujith/Downloads/prompt-eng-lab/prompt-eng/prompt-eng")
import os
import time
import numpy as np
from _pipeline import create_payload, model_req

# Ensure correct path for imports
sys.path.append("/Users/sujith/Downloads/prompt-eng-lab/prompt-eng/prompt-eng")

# Define prompts
prompts = {
    "tree_of_thought_prompt": "Break down the automation of Requirement Analysis into key decision points: (1) Choose between rule-based or ML-based extraction, (2) Determine methods for requirement classification, (3) Identify validation techniques, (4) Optimize for real-time space data integration. Select the best path for implementation based on evaluation.",
    "contrastive_prompt": "Compare two approaches to automating Requirement Analysis for a Space Bot: one using manual data extraction from documents and the other leveraging AI-driven NLP techniques. Highlight the inefficiencies of the manual method and the advantages of automation in terms of accuracy, speed, and adaptability for dynamic space news updates.",
    "meta_prompt": "Before responding, reflect on the purpose of automating Requirement Analysis for a Space Bot. Ensure that the response includes AI-based approaches, practical implementation strategies, and validation methods for extracted requirements. The bot should be capable of handling real-time space updates and user interactions dynamically.",
    "prompt_template_prompt": "Given a user query about automating Requirement Analysis for a Space Bot, generate responses based on these categories: 1. AI-based extraction → 'Use NLP models like BERT to extract space-related news and classify requirements for the bot’s functions.' 2. Automation tools → 'Leverage APIs like NASA’s Open APIs or custom-built RPA bots to streamline data ingestion.' 3. Validation and refinement → 'Use rule-based AI to validate extracted data and ensure accuracy before updating the bot’s responses.'",
    "chain_thought_prompt": "To automate Requirement Analysis for implementing a Space Bot, follow these steps: (1) Identify key functional needs like fetching space news, fun facts, and planning meetings, (2) Extract structured requirements using NLP from user queries and documents, (3) Classify and prioritize requirements, (4) Validate extracted data with AI, (5) Generate structured implementation guidelines. Ensure logical reasoning at each step.",
    "few_shots_prompt": "Example 1: 'To automate requirement analysis for a Space Bot, we use NLP to extract keywords from astronomy-related sources and classify them into bot response categories.' Example 2: 'A machine learning model categorizes user queries into functional and non-functional requirements, ensuring the bot understands and responds effectively.' Based on these examples, generate an optimal approach.",
    "self_consistency_prompt": "Generate multiple approaches to automating Requirement Analysis for the Space Bot using AI. Compare their effectiveness in terms of accuracy, scalability, and real-time adaptability. Identify the most reliable and scalable solution by analyzing consistency across different generated responses.",
    "zero_shot_prompt": "Without prior examples, generate a detailed explanation of how to automate Requirement Analysis for a Space Bot, considering AI, NLP, and process automation techniques. Include strategies for keeping the bot updated with the latest space news and ensuring it understands user queries accurately."
}

# Model parameters grid
parameters = [
    {"temperature": 0.5, "num_ctx": 100, "num_predict": 20},
    {"temperature": 0.7, "num_ctx": 200, "num_predict": 50},
    {"temperature": 1.0, "num_ctx": 300, "num_predict": 100}
]

# Store results
results = []
best_technique = None
best_score = float('-inf')

def evaluate_response(response):
    """Evaluate response quality based on coherence and relevance using a scoring function."""
    if not response:
        return 0  # Empty response gets a low score
    length_score = min(len(response) / 100, 1)  # Scale response length (max 1)
    keyword_score = sum(1 for word in ["AI", "automation", "NLP", "classification"] if word in response) / 4
    return (length_score + keyword_score) / 2  # Weighted average

# Loop through prompts and parameters
for name, prompt in prompts.items():
    for param in parameters:
        print(f"Processing: {name} with params {param}")
        
        start_time = time.time()
        payload = create_payload(target="ollama", model="llama3.2:latest", prompt=prompt, **param)
        latency, response = model_req(payload=payload)
        end_time = time.time()
        
        response_time = end_time - start_time if latency is None else latency
        score = evaluate_response(response)
        
        results.append((name, param, response_time, score, response))

        # Update best technique based on highest accuracy score and lowest response time
        if score > best_score or (score == best_score and response_time < results[-1][2]):
            best_score = score
            best_technique = name
        
        print(f"Response for {name}: {response}\n")
        print(f"Time taken: {response_time:.2f}s, Score: {score:.2f}\n{'-'*40}")

# Rank prompts based on latency and accuracy trade-off
results.sort(key=lambda x: (x[2] - x[3]))  # Minimize (latency - accuracy score)

# Print ranking
print("\nRanking of Prompts by Performance (Latency vs. Accuracy):")
for rank, (name, param, response_time, score, response) in enumerate(results, start=1):
    print(f"{rank}. {name} | Params: {param} | Time: {response_time:.2f}s | Score: {score:.2f}")

# Print the best technique
print("\n Best Prompt Engineering Technique:")
print(f"➡️ {best_technique} with Score: {best_score:.2f}")
