from smolagents import Tool

from data_generator import identification_numbers


class IdentificationNumbers(Tool):
    name = 'identification_numbers'
    description = 'This tool returns a person\'s identifications numbers'
    inputs = {'person': {'type': 'string', 'description': 'some person\'s identifier'}}
    output_type = 'array'

    def forward(self, person):
        print(person)
        return identification_numbers
