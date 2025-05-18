from smolagents import Tool

from data_generator import contact_info


class ContactInfo(Tool):
    name = 'contact_info'
    description = 'This tool returns a person\'s contact info'
    inputs = {'person': {'type': 'string', 'description': 'some person\'s identifier'}}
    output_type = 'array'

    def forward(self, person):
        print(person)
        return contact_info
