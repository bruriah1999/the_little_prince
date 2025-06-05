import importlib
import os

import yaml
from huggingface_hub import login
from smolagents import CodeAgent, HfApiModel

from the_little_prince_system_prompt import THE_LITTLE_PRINCE_SYSTEM_PROMPT
from tools import Address, ContactInfo, FamilyRelation, GossipAboutAPerson, IdentificationNumbers, WorkDetails, PersonalInfo, VehicleOwnership, LinkedInPosts, WhatsAppConversations

login(os.getenv('HF_API_KEY'))

# Initialize model and agent
# model_id = "mistralai/Mistral-7B-Instruct-v0.3"
model_id = "mistralai/Mistral-Small-3.1-24B-Instruct-2503"
model = HfApiModel(model_id=model_id)
prompt_template = yaml.safe_load(
    importlib.resources.files("smolagents.prompts").joinpath("structured_code_agent.yaml").read_text()
)
prompt_template['system_prompt'] = THE_LITTLE_PRINCE_SYSTEM_PROMPT
agent = CodeAgent(
    tools=[Address(), ContactInfo(), FamilyRelation(), GossipAboutAPerson(), IdentificationNumbers(), WorkDetails(), PersonalInfo(), VehicleOwnership(), LinkedInPosts(), WhatsAppConversations()],
    model=model, prompt_templates=prompt_template)

# Run a task
result = agent.run("Tell me everything you know about L61595148?")
print(result) 
