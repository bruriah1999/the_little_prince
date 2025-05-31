from smolagents import Tool

from data_generator import gossip_text


class GossipAboutAPerson(Tool):
    name = 'gossip_about_a_person'
    description = 'This tool returns text which is a gossip about a person'
    inputs = {'person': {'type': 'string', 'description': 'some person\'s identifier'}}
    output_type = 'array'

    def forward(self, person):
        print(person)
        return gossip_text
