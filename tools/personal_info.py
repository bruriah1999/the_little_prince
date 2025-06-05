from smolagents.tools import Tool
from data_generator import personal_info

class PersonalInfo(Tool):
    name = "PersonalInfo"
    description = "Fetches personal information for a person, including name, age, and gender."

    def run(self, person_name: str):
        """
        Fetches personal information for the given person.

        Args:
            person_name (str): The name of the person whose personal info is requested.

        Returns:
            dict: A dictionary containing the personal information.
        """
        return personal_info.get(person_name, {"error": "No personal information found for this person."})