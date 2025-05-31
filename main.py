import os

from huggingface_hub import login
from smolagents import CodeAgent, HfApiModel

from tools import Address, ContactInfo, FamilyRelation, GossipAboutAPerson, IdentificationNumbers, WorkDetails

login(os.getenv('HF_API_KEY'))

# Initialize model and agent
# model_id = "mistralai/Mistral-7B-Instruct-v0.3"
model_id = "mistralai/Mistral-Small-3.1-24B-Instruct-2503"
model = HfApiModel(model_id=model_id)
agent = CodeAgent(
    tools=[Address(), ContactInfo(), FamilyRelation(), GossipAboutAPerson(), IdentificationNumbers(), WorkDetails()],
    model=model)

# Run a task
result = agent.run("Tell me everything you know about L61595148?")
print(result)  # Output: The 15th prime number is 47
