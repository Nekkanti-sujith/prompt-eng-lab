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

# In[2]:


from _pipeline import create_payload, model_req

MESSAGE = "200"

TREE_OF_THOUGHT = \
f"""
The sum of the first N even numbers follows the formula S = N * (N + 1), where N is the number of even numbers.

Step 1: Find N
- Even numbers follow the pattern: 2, 4, 6, ..., {MESSAGE}.
- N is the total number of even numbers up to {MESSAGE}.

Step 2: Compute the sum
- Using S = N * (N + 1), calculate the sum.

Now, provide **only the final answer** with no explanation.
"""

PROMPT = TREE_OF_THOUGHT 

payload = create_payload(target="ollama",
                         model="llama3.2:latest", 
                         prompt=PROMPT, 
                         temperature=0.7,  
                         num_ctx=100, 
                         num_predict=10)  

time, response = model_req(payload=payload)
print(response)
if time: print("Time taken: {time}s")

