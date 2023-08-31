def pda(string):
    stack = ['X']  # Z_0 = X - маркер дна
    cond = ['q_0', 'q_1', 'q_2', 'q_3', 'q_4', 'q_5']
    # начальное состояние
    q = cond[0]
    # Номер дельта-функции перед каждым условием
    # Иду с начала строки до первой ошибки или до конца
    for i in range(len(string)):
        # 1
        if q == cond[0] and string[i] == 'x' and stack[-1] == 'X':
            stack.pop()
            stack.extend('X11')  # кладу символы наоборот, так как вершина стека в конце
            q = cond[1]
        # 2
        elif q == cond[1] and string[i] == 'x' and stack[-1] == '1':
            stack.pop()
            stack.extend('111')  # кладу символы наоборот, так как вершина стека в конце
        # 3
        elif q == cond[1] and string[i] == 'y' and stack[-1] == '1':
            stack.pop()
            q = cond[2]
        # 4
        elif q == cond[2] and string[i] == 'y' and stack[-1] == '1':
            stack.pop()
        # 6, 7
        elif (q == cond[0] or q == cond[2]) and string[i] == 'z' and stack[-1] == 'X':
            stack.pop()
            stack.extend('X1')  # кладу символы наоборот, так как вершина стека в конце
            q = cond[3]
        # 8
        elif q == cond[3] and string[i] == 'z' and stack[-1] == '1':
            stack.pop()
            stack.extend('2')
            q = cond[3]
        # 9
        elif q == cond[3] and string[i] == 'z' and stack[-1] == '2':
            stack.pop()
            stack.extend('3')
        # 10
        elif q == cond[3] and string[i] == 'z' and stack[-1] == '3':
            stack.pop()
            stack.extend('31')  # кладу символы наоборот, так как вершина стека в конце
        # 11
        elif q == cond[3] and string[i] == 'x' and stack[-1] == '3':
            stack.pop()
            q = cond[4]
        # 12
        elif q == cond[4] and string[i] == 'x' and stack[-1] == '3':
            stack.pop()
        else:
            return f'Ошибка: в позиции {i+1}, неожидаемый символ {string[i]}'
            break
    if len(stack) != 1:
        return 'Ошибка: неожидаемый конец строки'
    else:
        return 'Цепочка принадлежит языку'


if __name__ == '__main__':
    print(pda(input()))