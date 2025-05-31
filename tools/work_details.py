from smolagents import Tool

from data_generator import work_details


class WorkDetails(Tool):
    name = 'work_details'
    description = 'This tool returns a person\'s work details info'
    inputs = {'person': {'type': 'string', 'description': 'some person\'s identifier'}}
    output_type = 'array'

    def forward(self, person):
        print(person)
        return work_details
