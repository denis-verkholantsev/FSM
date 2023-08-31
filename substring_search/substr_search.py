# Проверка: повторяются символы или нет
def check_repeated_characters(substr):
    for i in range(1, len(substr), 1):
        if substr[i] != substr[i-1]:
            return False
    return True


# Обработка подстроки после разбиения '+'
def processing_string(substr):
    if substr == '':
        return True
    # Разбиваем подстроки вида '+...+' на подстроки, разделенные '-'
    splitted_substring = substr.split('-')
    # Храним символы подстрок, разбитых '-', для проверки на то, чтобы символы до и после '-' не были одинаковыми
    character_of_splitted_substr = []
    # Проверяем на соответсиве условию все подстроки, разбитые '-'
    for i in range(len(splitted_substring)):
        if splitted_substring[i] == '':
            return False
        # Проверяем, чтобы символы в подстроке вида '-...-' были одинаковыми
        if check_repeated_characters(splitted_substring[i]):
            character_of_splitted_substr.append(splitted_substring[i][0])
        else:
            return False
        # Проверяем, чтобы символы до '-' и после не были одинаковыми
        if i > 0:
            if character_of_splitted_substr[i] == character_of_splitted_substr[i-1]:
                return False
    return True


# Поиск индекса начала подстрок, вида '+...+'
def find_pluses_indexes():
    indexes_plus = []
    for i in range(len(string)):
        if string[i] == '+':
            indexes_plus.append(i)
    return indexes_plus


if __name__ == '__main__':
    string = input()
    # Разбиваем на подстроки вида '+...+'
    splitted_string = string.split('+')
    splitted_string.pop(0)
    splitted_string.pop(len(splitted_string) - 1)
    # Находим индексы начала подстрок
    plus_index = find_pluses_indexes()
    result = {}
    for i in range(len(plus_index)-1):
        if processing_string(splitted_string[i]):
            result.update({plus_index[i] + 1: '+' + splitted_string[i] + '+'})
    print(result)