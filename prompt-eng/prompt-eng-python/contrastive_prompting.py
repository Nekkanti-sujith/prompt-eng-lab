#!/usr/bin/env python
# coding: utf-8

# 
# 
# 

# # Meta Prompting
# 
# Meta prompting is an advanced technique in prompt engineering that emphasizes the structural and syntactical organization of tasks and problems rather than focusing on their specific content. The objective is to create a more abstract, form-driven way of engaging with large language models (LLMs), highlighting patterns and structure over traditional content-focused methods.
# 
# As outlined by [Zhang et al. (2024)](https://arxiv.org/abs/2311.11482), the defining features of meta prompting include:
# 
# * Structure-Oriented: Prioritizes the organization and pattern of problems and solutions instead of specific content.
# * Syntax-Guided: Leverages syntax as a template to shape the expected responses or solutions.
# * Abstract Frameworks: Uses abstract examples as blueprints, demonstrating the structure of tasks without relying on concrete details.
# * Domain Versatility: Can be applied across multiple fields, offering structured solutions to diverse problem types.
# * Categorical Approach: Draws on type theory to organize and categorize components logically, enhancing prompt coherence and precision.

# ## Running this code on MyBind.org
# 
# Note: remember that you will need to **adjust CONFIG** with **proper URL and API_KEY**!
# 
# [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/GenILab-FAU/prompt-eng/HEAD?urlpath=%2Fdoc%2Ftree%2Fprompt-eng%2Fmeta.ipynb)
# 
# 

# In[ ]:


##
## CONTRASTIVE PROMPTING (FIXED)
##

from _pipeline import create_payload, model_req

MESSAGE = "200"

CONTRASTIVE_PROMPTING = \
f"""
### Incorrect Example:
- Summing all numbers instead of only odd numbers.
- Example: 1 + 2 + 3 + 4 + ... + 200 = Incorrect.

### Correct Example:
- Only sum odd numbers: 1, 3, 5, ..., {MESSAGE}.
- Use S = N² formula.

Now, calculate and provide **only the final answer.**  
"""

PROMPT = CONTRASTIVE_PROMPTING 

payload = create_payload(target="ollama",
                         model="llama3.2:latest", 
                         prompt=PROMPT, 
                         temperature=0.7,  
                         num_ctx=100, 
                         num_predict=10)

time, response = model_req(payload=payload)
print(response)
if time: print(f'Time taken: {time}s')


# 
