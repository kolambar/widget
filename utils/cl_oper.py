import os
# from function import from_json_to_data
from utils.function import time_metamorphosis
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

    @staticmethod
    def born_from_json(data):
        list_of_classes = []
        for diction in data:
            if not diction:
                continue
            operation = Operation(diction)
            list_of_classes.append(operation)
        return list_of_classes

    @staticmethod
    def filter(list_of_classes):
        for instance in list_of_classes:
            instance.date, instance.date_to_print = time_metamorphosis(instance.date)
        list_of_classes_executed = [instance for instance in list_of_classes if instance.state == 'EXECUTED']
        sorted_executed_list = sorted(list_of_classes_executed, key=lambda operation: operation.date, reverse=True)
        return sorted_executed_list

# data = from_json_to_data(os.path.join("..", 'operations.json'))
#
# print(Operation.born_from_json(data))