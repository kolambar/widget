from utils.function import time_metamorphosis


class Operation:
    '''
    класс для работ с операциями
    '''
    def __init__(self, kwargs):
        '''
        конструктор класса.
        принимает словарь, превращает в элемнт класса
        :param kwargs:
        '''
        for key, value in kwargs.items():
            if key == "from":  # еслиключ "from" то поле элемента будет называться "sender"
                setattr(self, "sender", value)
            else:
                setattr(self, key, value)
            # добавляет поле sender, если не было ключа "fore"
            self.sender = getattr(self, "sender", "Счета отправителя нет. Это операция по открытию вклада.")

    def __repr__(self):
        '''
        помимо упомянутых полей у класса после использования time_metamorphosis() в методе filter()
        появляется поле data_to_print
        :return:
        '''
        return f'id: {self.id}, state: {self.state}, date: {self.date}, operationAmount: {self.operationAmount}, ' \
               f'description: {self.description}, from: {self.sender}, to: {self.to}'

    @staticmethod
    def born_from_json(data):
        '''
        принимает список словарей и превращает его словари в элементы Operation
        элементы помещаются в словарь
        словарь возвращается
        :param data:
        :return list_of_classes:
        '''
        list_of_classes = []
        for diction in data:
            if not diction: # проверка словоря на наличие данных
                continue
            operation = Operation(diction)
            list_of_classes.append(operation)
        return list_of_classes

    @staticmethod
    def filter(list_of_classes):
        '''
        принимает список классов и сортирует его в список sorted_executed_list
        при сортировки убираются отклоненные операции, ставшиеся операции сортируются по дате от новых к старым
        помимо этого добавляет каждому элементу поле date_to_print
        :param list_of_classes:
        :return sorted_executed_list:
        '''
        for instance in list_of_classes:
            instance.date, instance.date_to_print = time_metamorphosis(instance.date) # добавляет поле классу для сравнения по времени операции
        list_of_classes_executed = [instance for instance in list_of_classes if instance.state == 'EXECUTED'] # отсеивание непрошедших операций
        sorted_executed_list = sorted(list_of_classes_executed, key=lambda operation: operation.date, reverse=True) # сортировка по времени
        return sorted_executed_list

    @staticmethod
    def blur_num(num):
        '''
        затирает часть чисел в номерах
        после этого, номера можно печатать
        '''
        i, blur_num = 1, []  # счетчик i начинает увеличиваться, когда код доходит до цифр
        if num == '': # проверка, что был счет отправки
            return num
        elif 'Счет ' in num: # для счета отправки особый способ маскировки, так как в нем на 4 цифры больше
            blur_num = '**' + num[-4:]
            return blur_num
        else:
            for symbol in num:
                if symbol.isdigit() and 6 < i < 13: # когда счетчик i в (6:13), код начинает прятать цифры номера за "*"
                    symbol, i = '*', i + 1
                    blur_num.append(symbol)
                elif symbol.isdigit(): # если символ цифра и i не в промежутке, символ записывается
                    blur_num.append(symbol)
                    i += 1

            # расставляем пробелы через каждые 4 цифры для удобства чтения
            blur_num.insert(4, ' ')
            blur_num.insert(9, ' ')
            blur_num.insert(14, ' ')

            blur_num = ''.join(blur_num)
            return blur_num

    @staticmethod
    def user_platform(info):
        '''
        получает информацию о отправителе и получателе возвращает только название карты или счет
        :param info:
        '''
        if 'Visa Platinum' in info:
            return 'Visa Platinum'
        elif 'Visa Gold' in info:
            return 'Visa Gold'
        elif 'Maestro' in info:
            return 'Maestro'
        elif 'МИР' in info:
            return 'МИР'
        elif 'Счета отправител' in info:
            return ''
        elif 'Счет' in info:
            return 'Счет'
        else:
            return 'MasterCard'
