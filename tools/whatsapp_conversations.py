from smolagents.tools import Tool
from data_generator import whatsapp_conversations

class WhatsAppConversations(Tool):
    name = "WhatsAppConversations"
    description = "Fetches WhatsApp conversations for a person, including messages and timestamps."

    def run(self, person_name: str):
        """
        Fetches WhatsApp conversations for the given person.

        Args:
            person_name (str): The name of the person whose WhatsApp conversations are requested.

        Returns:
            list: A list of WhatsApp messages with timestamps.
        """
        return whatsapp_conversations.get(person_name, {"error": "No WhatsApp conversations found for this person."})