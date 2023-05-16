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

    @staticmethod
    def blur_num(num):
        i, blur_num = 1, []
        if num == 'Счета отправителя нет. Это операция по открытию вклада.':
            return num
        elif 'Счет ' in num:
            for symbol in num:
                if symbol.isdigit() and i < 17:
                    symbol, i = '*', i + 1
                    blur_num.append(symbol)
                elif symbol in '0123456789':
                    blur_num.append(symbol)
                    i += 1
            blur_num.insert(4, ' ')
            blur_num.insert(9, ' ')
            blur_num.insert(14, ' ')
            blur_num.insert(19, ' ')
            blur_num = ''.join(blur_num)
            return blur_num
        else:
            for symbol in num:
                if symbol.isdigit() and 6 < i < 13:
                    symbol, i = '*', i + 1
                    blur_num.append(symbol)
                elif symbol in '0123456789':
                    blur_num.append(symbol)
                    i += 1
            blur_num.insert(4, ' ')
            blur_num.insert(9, ' ')
            blur_num.insert(14, ' ')
            blur_num = ''.join(blur_num)
            return blur_num

    @staticmethod
    def user_platform(info):
        if 'Visa Platinum' in info:
            return 'Visa Platinum'
        elif 'Visa Gold' in info:
            return 'Visa Gold'
        elif 'Maestro' in info:
            return 'Maestro'
        elif 'МИР' in info:
            return 'МИР'
        elif 'Счета отправител' in info:
            return None
        elif 'Счет' in info:
            return 'Счет'
        else:
            return 'MasterCard'
