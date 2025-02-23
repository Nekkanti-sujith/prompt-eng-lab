import sys
sys.path.append("/Users/sujith/Downloads/prompt-eng-lab/prompt-eng/prompt-eng")
from _pipeline import create_payload, model_req

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


# List to store response times
response_times = []

# Loop through prompts and get responses
for name, prompt in prompts.items():
    print(f"Processing: {name}")
    
    payload = create_payload(target="ollama",
                             model="llama3.2:latest", 
                             prompt=prompt, 
                             temperature=0.7,  
                             num_ctx=100, 
                             num_predict=10)

    time, response = model_req(payload=payload)
    print(f"Response for {name}: {response}\n")
    
    if time:
        print(f'Time taken: {time}s\n{"-"*40}')
        response_times.append((name, time))

# Sort prompts by response time in ascending order (fastest first)
response_times.sort(key=lambda x: x[1])

# Print ranked response times
print("\nRanking of Prompts by Response Time:")
for rank, (name, time) in enumerate(response_times, start=1):
    print(f"{rank}. {name}: {time}s")
