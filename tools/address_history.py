from smolagents import Tool

from data_generator import address_history


class Address(Tool):
    name = 'address'
    description = 'This tool returns a person\'s address info'
    inputs = {'person': {'type': 'string', 'description': 'some person\'s identifier'}}
    output_type = 'array'

    def forward(self, person):
        print(person)
        return address_history
