#!/usr/bin/env python
# coding: utf-8

# 
# 
# 

# # Few-Shots Prompting
# 
# Few-shot prompting can be used as a technique to enable in-context learning where we provide demonstrations in the prompt to steer the model to better performance. The demonstrations serve as conditioning for subsequent examples where we would like the model to generate a response.
# 
# ## References:
# * [Touvron et al. 2023](https://arxiv.org/pdf/2302.13971.pdf): present few shot properties  when models were scaled to a sufficient size
# * [Kaplan et al., 2020](https://arxiv.org/abs/2001.08361)
# * [Brown et al. 2020](https://arxiv.org/abs/2005.14165)
# 

# ## Running this code on MyBind.org
# 
# Note: remember that you will need to **adjust CONFIG** with **proper URL and API_KEY**!
# 
# [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/GenILab-FAU/prompt-eng/HEAD?urlpath=%2Fdoc%2Ftree%2Fprompt-eng%2Ffew_shots.ipynb)
# 
# 

# In[1]:


##
## FEW SHOTS PROMPTING
##

from _pipeline import create_payload, model_req

#### (1) Adjust the inbounding  Prompt, simulating inbounding requests from users or other systems
MESSAGE = "Calculate 984 * log(2)"

#### (2) Adjust the Prompt Engineering Technique to be applied, simulating Workflow Templates
FEW_SHOT = "You are a math teacher. If student asked 1 + 1 you answer 2. If student ask 987 * 2 you answer only 1974. Student asked; provide the result only: "
PROMPT = FEW_SHOT + '\n' + MESSAGE 

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


# ## How to improve it?
# 
# Following the findings from [Min et al. (2022)](https://arxiv.org/abs/2202.12837), here are a few more tips about demonstrations/exemplars when doing few-shot:
# 
# * "the label space and the distribution of the input text specified by the demonstrations are both important (regardless of whether the labels are correct for individual inputs)"
# * the format you use also plays a key role in performance, even if you just use random labels, this is much better than no labels at all.
# * additional results show that selecting random labels from a true distribution of labels (instead of a uniform distribution) also helps.
