# import function
# import os
class Operation:

    def __init__(self, kwargs):
        for key, value in kwargs.items():
            if key == "from":
                setattr(self, "sender", value)
            else:
                setattr(self, key, value)
            self.sender = getattr(self, "sender", "Счета отправителя нет. Это операция по открытию вклада.")

    def __repr__(self):
        return f'id: {self.id}, state: {self.state}, date: {self.date}, operationAmount: {self.operationAmount}, description: {self.description}, from: {self.sender}, to: {self.to}'

    def born_from_json(data):
        list_of_operation = []
        for diction in data:
            if not diction:
                continue
            operation = Operation(diction)
            list_of_operation.append(operation)
        return list_of_operation

# data = function.from_json_to_data(os.path.join("..", 'operations.json'))
#
# print(Operation.born_from_json(data))