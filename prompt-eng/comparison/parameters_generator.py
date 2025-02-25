import random

output_file = "/Users/sujith/Downloads/prompt-eng-lab/prompt-eng/prompt-eng/comparison/parameters.txt"

with open(output_file, "w") as f:
    for _ in range(10):  
        temperature = round(random.uniform(1.05, 1.1), 2)  
        num_ctx = 300.0 
        num_predict = 100.0  
        f.write(f"temperature={temperature},num_ctx={num_ctx},num_predict={num_predict}\n")

print(f" Generated optimized parameters in {output_file}")
