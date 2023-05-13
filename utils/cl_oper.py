import function
import os
class Operation:

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __repr__(self):
        return f'{self.id}, {self.state}, {self.description}, {self.operationAmount}'

    def born_from_json(data):
        list_of_operation = []
        for diction in data:
            if not diction:
                continue
            operation = Operation(**diction)
            list_of_operation.append(operation)
        return list_of_operation

data = function.from_json_to_data(os.path.join("..", 'operations.json'))
