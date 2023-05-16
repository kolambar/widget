from utils.function import from_json_to_data
from utils.cl_oper import Operation
import os


def main():
    '''
    программа для виджета.
    виджет выводит последние 5 успешных операций в коротком удобном фармате
    '''

    # получаем инфу из файла
    data = from_json_to_data(os.path.join('operations.json'))

    # превращаем инфу в элементы класса. помещаем их в хронологическом порядке в словарь
    list_of_classes = Operation.born_from_json(data)
    sorted_executed_list = Operation.filter(list_of_classes)

    for i in range(5):
        # для удобство присваиваем имя элементу
        instance = sorted_executed_list[i]

        # получаем название платежной системы и блюрим номер отправителя
        sender_platform = Operation.user_platform(instance.sender)
        sender_num = Operation.blur_num(instance.sender)

        # получаем название платежной системы и блюрим номер получателя
        receiver_platform = Operation.user_platform(instance.to)
        receiver_num = Operation.blur_num(instance.to)

        # получаем информацию о сумме транзакции
        amount = instance.operationAmount['amount']
        currency = instance.operationAmount['currency']['name']

        # выводем в удобном коротком виде
        print(f'{instance.date_to_print} {instance.description}\n'
        f'{sender_platform} {sender_num} -> {receiver_platform} {receiver_num}\n'
        f'{amount} {currency}\n')


if __name__ == "__main__":
    main()
