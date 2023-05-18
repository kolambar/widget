import datetime


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
            self.sender = getattr(self, "sender", "")

    def __repr__(self):
        '''
        помимо упомянутых полей у класса после использования time_metamorphosis() в методе filter()
        появляется поле data_to_print
        :return:
        '''
        return f'id: {self.id}, state: {self.state}, date: {self.date}, operationAmount: {self.operationAmount}, ' \
               f'description: {self.description}, from: {self.sender}, to: {self.to}'

    def time_metamorphosis(self, date):
        '''
        превращает дату формата файла json из строки в data_to_compare, data_to_print
        data_to_compare нужна, чтобы сравнивать по хронологии. формат datatime
        data_to_print дата в удобном виде для вывода пользователю
        :param date:
        :return data_to_compare, data_to_print:
        '''
        self.date_to_compare = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f')
        self.date_to_print = self.date_to_compare.strftime('%d.%m.%Y')

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
    def bagger(list_of_classes):
        '''
        принимает список классов и сортирует его в список sorted_executed_list
        при сортировки убираются отклоненные операции, ставшиеся операции сортируются по дате от новых к старым
        помимо этого добавляет каждому элементу поле date_to_print
        :param list_of_classes:
        :return sorted_executed_list:
        '''
        for instance in list_of_classes:
            instance.time_metamorphosis(instance.date) # добавляет поле классу для сравнения по времени операции
        list_of_classes_executed = [instance for instance in list_of_classes if instance.state == 'EXECUTED'] # отсеивание непрошедших операций
        sorted_executed_list = sorted(list_of_classes_executed, key=lambda operation: operation.date, reverse=True) # сортировка по времени
        return sorted_executed_list

    @staticmethod
    def blur_num(num):
        '''
        затирает часть чисел в номерах
        после этого, номера можно печатать
        '''
        if num: # проверяет, что номер есть
            num_string = num.split(' ')

            if num_string[0] == 'Счет': # для счета свой алгоритм. в нем на 4 цифры больше
                return 'Счет ' + '**' + num_string[1][-4:]
            else:
                return ' '.join(num_string[:-1]) + ' ' + num_string[-1][:4] + ' ' + num_string[-1][4:6] + '** **** ' + num_string[-1][-4:]
