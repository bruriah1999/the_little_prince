from smolagents import Tool

from data_generator import family_relationships


class FamilyRelation(Tool):
    name = 'family_relations'
    description = 'This tool returns a person\'s family relations info'
    inputs = {'person': {'type': 'string', 'description': 'some person\'s identifier'}}
    output_type = 'array'

    def forward(self, person):
        print(person)
        return family_relationships
