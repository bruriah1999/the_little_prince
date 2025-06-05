from smolagents.tools import Tool
from data_generator import linkedin_posts

class LinkedInPosts(Tool):
    name = "LinkedInPosts"
    description = "Fetches LinkedIn posts for a person, including content and timestamps."

    def run(self, person_name: str):
        """
        Fetches LinkedIn posts for the given person.

        Args:
            person_name (str): The name of the person whose LinkedIn posts are requested.

        Returns:
            list: A list of LinkedIn posts with content and timestamps.
        """
        return linkedin_posts.get(person_name, {"error": "No LinkedIn posts found for this person."})