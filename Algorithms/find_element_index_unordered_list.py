"""Поиск индекса элемента при помощи enumerate()."""


def find_element_index_in_unordered_list(desired_element, unordered_list):
    """
    Находит индекс первого вхождения искомого элемента
    в неотсортированном списке.
    """
    for index, item in enumerate(unordered_list):
        if item == desired_element:
            return index
    return None


wins = [7495938, 1223125, 2128437, 4567890, 2128500, 2741001, 9314543, 4567687]
my_ticket = 2128506

result = find_element_index_in_unordered_list(my_ticket, wins)
if result is not None:
    print(f'Индекс элемента {my_ticket} в массиве: {result}')
else:
    print(f'Элемент {my_ticket} не найден в массиве.')
