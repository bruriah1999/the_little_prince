from smolagents.tools import Tool
from data_generator import vehicle_ownership

class VehicleOwnership(Tool):
    name = "VehicleOwnership"
    description = "Fetches vehicle ownership details for a person, including vehicle type, model, and registration."

    def run(self, person_name: str):
        """
        Fetches vehicle ownership details for the given person.

        Args:
            person_name (str): The name of the person whose vehicle ownership details are requested.

        Returns:
            list: A list of vehicles owned by the person.
        """
        return vehicle_ownership.get(person_name, {"error": "No vehicle ownership details found for this person."})