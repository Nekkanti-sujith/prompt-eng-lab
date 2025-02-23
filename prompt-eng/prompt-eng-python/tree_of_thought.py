#!/usr/bin/env python
# coding: utf-8

# 
# 
# 

# # Chain-of-Thought Prompting
# 
# Chain-of-Thought (CoT) prompting enhances complex reasoning by encouraging the model to break down problems into intermediate reasoning steps. When combined with few-shot prompting, it can significantly improve performance on tasks that require multi-step reasoning before arriving at a response.
# 
# ## Automatic Chain-of-Thought (Auto-CoT)
# 
# Traditionally, using CoT prompting with demonstrations involves manually crafting diverse and effective examples. This manual effort is time-consuming and can lead to less-than-optimal results. To address this, Zhang et al. (2022) introduced Auto-CoT, an automated approach that minimizes manual involvement. Their method uses the prompt “Let’s think step by step” to generate reasoning chains automatically for demonstrations. However, this automatic process is not immune to errors. To reduce the impact of such mistakes, the approach emphasizes the importance of diverse demonstrations.
# 
# Auto-CoT operates in two main stages:
# 
# 1. **Question Clustering:** Questions from the dataset are grouped into clusters based on similarity or relevance.
# 2. **Demonstration Sampling:** A representative question from each cluster is selected, and its reasoning chain is generated using Zero-Shot-CoT guided by simple heuristics.
# 
# 
# ## References:
# 
# * (Wei et al. (2022),)[https://arxiv.org/abs/2201.11903]
# * (OpenAI Documentation for Prompt Engineering)[https://platform.openai.com/docs/guides/prompt-engineering]

# ## Running this code on MyBind.org
# 
# Note: remember that you will need to **adjust CONFIG** with **proper URL and API_KEY**!
# 
# [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/GenILab-FAU/prompt-eng/HEAD?urlpath=%2Fdoc%2Ftree%2Fprompt-eng%2Fchain_of_thought.ipynb)
# 

# In[4]:


##
## CHAIN-OF-THOUGHT  PROMPTING
##

from _pipeline import create_payload, model_req


#### (1) Adjust the inbounding  Prompt, simulating inbounding requests from users or other systems
MESSAGE = "200"

#### (2) Adjust the Prompt Engineering Technique to be applied, simulating Workflow Templates
CHAIN_OF_THOUGHT = \
f"""
The odd numbers in this group add up to an even number: 4, 8, 9, 15, 12, 2, 1.
A: Adding all the odd numbers (9, 15, 1) gives 25. The answer is False.
The odd numbers in this group add up to an even number: 17,  10, 19, 4, 8, 12, 24.
A: Adding all the odd numbers (17, 19) gives 36. The answer is True.
The odd numbers in this group add up to an even number: 16,  11, 14, 4, 8, 13, 24.
A: Adding all the odd numbers (11, 13) gives 24. The answer is True.
The odd numbers in this group add up to an even number: 17,  9, 10, 12, 13, 4, 2.
A: Adding all the odd numbers (17, 9, 13) gives 39. The answer is False.
Now Add all odd numbers until {MESSAGE} and let me know. 
Provide only the answer, no explanation!
"""

PROMPT = CHAIN_OF_THOUGHT 

#### (3) Configure the Model request, simulating Workflow Orchestration
# Documentation: https://github.com/ollama/ollama/blob/main/docs/api.md
payload = create_payload(target="ollama",
                         model="llama3.2:latest", 
                         prompt=PROMPT, 
                         temperature=1.0, 
                         num_ctx=100, 
                         num_predict=100)

### YOU DONT NEED TO CONFIGURE ANYTHING ELSE FROM THIS POINT
# Send out to the model
time, response = model_req(payload=payload)
print(response)
if time: print(f'Time taken: {time}s')

