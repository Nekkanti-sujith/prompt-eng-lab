#!/usr/bin/env python
# coding: utf-8

# 
# 
# 

# # Prompt Template Prompting
# 
# Prompt Template Prompting refers to a technique where predefined templates are used to construct effective prompts that guide large language models (LLMs) to generate responses tailored to specific use cases. The templates typically contain static text combined with dynamic input variables, allowing for consistent, reusable, and customizable prompts.
# 
# Prompt templates are widely used across various domains, such as:
# * **Question Generation**: Templates can generate quiz questions by filling in variables related to topics.
# * **Text Summarization**: Static instructions combined with variable documents or inputs allow flexible summarization.
# * **Coding Assistance**: Dynamic prompts help LLMs generate code snippets for different programming tasks.
# 
# ## References:
# 
# * (OpenAI Documentation for Prompt Engineering)[https://platform.openai.com/docs/guides/prompt-engineering]

# ## Running this code on MyBind.org
# 
# Note: remember that you will need to **adjust CONFIG** with **proper URL and API_KEY**!
# 
# [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/GenILab-FAU/prompt-eng/HEAD?urlpath=%2Fdoc%2Ftree%2Fprompt-eng%2Fprompt_template.ipynb)
# 

# In[1]:


##
## PROMPT TEMPLATE PROMPTING
##

from _pipeline import create_payload, model_req

#### (1) Adjust the inbounding  Prompt, simulating inbounding requests from users or other systems
MESSAGE = "984 * log(2)"

#### (2) Adjust the Prompt Engineering Technique to be applied, simulating Workflow Templates
TEMPLATE_BEFORE="Act like you are a math teacher. Answer to this question from an student:"
TEMPLATE_AFTER="Provide the answer only. No explanations!"
PROMPT = TEMPLATE_BEFORE + '\n' + MESSAGE + '\n' + TEMPLATE_AFTER

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

