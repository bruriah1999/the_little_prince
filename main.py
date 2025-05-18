import os

from smolagents import CodeAgent, HfApiModel
from huggingface_hub import login

# Log in to Hugging Face
login(os.getenv('HF_API_KEY'))

# Initialize model and agent
model_id = "mistralai/Mistral-7B-Instruct-v0.3"
model = HfApiModel(model_id=model_id)
agent = CodeAgent(tools=[], model=model)

# Run a task
result = agent.run("What is the 15th prime number?")
print(result)  # Output: The 15th prime number is 47