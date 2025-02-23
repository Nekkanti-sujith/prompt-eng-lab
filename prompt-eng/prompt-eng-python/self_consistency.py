#!/usr/bin/env python
# coding: utf-8

# 
# 
# 

# # Self Consistency Prompting
# 
# One of the more advanced techniques in prompt engineering is self-consistency, introduced by `Wang et al. (2022)`. 
# 
# This method seeks to improve upon the traditional greedy decoding typically used in chain-of-thought (CoT) prompting. 
# 
# The core concept involves sampling multiple diverse reasoning paths through few-shot CoT and leveraging these variations to determine the most consistent answer. The technique  enhances the effectiveness of CoT prompting, particularly for tasks requiring arithmetic and commonsense reasoning.
# 
# ## References:
# * [Wang et al. (2022)](https://arxiv.org/abs/2203.11171)

# ## Running this code on MyBind.org
# 
# Note: remember that you will need to **adjust CONFIG** with **proper URL and API_KEY**!
# 
# [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/GenILab-FAU/prompt-eng/HEAD?urlpath=%2Fdoc%2Ftree%2Fprompt-eng%2Fself_consistency.ipynb)
# 
# 

# In[1]:


##
## ZERO SHOT PROMPTING
##

from _pipeline import create_payload, model_req

#### (1) Adjust the inbounding  Prompt, simulating inbounding requests from users or other systems
MESSAGE = "What is 984 * log(2)"

#### (2) Adjust the Prompt Engineering Technique to be applied, simulating Workflow Templates

## @TODO 
PROMPT = MESSAGE 

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

