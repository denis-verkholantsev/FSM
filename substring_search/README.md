# Поиск подстрок

## Задание
Строка символов a,b,c,+, начинающаяся с префикса + и заканчивающаяся суффиксом +, между которыми располагается последовательность символов a,b,c (она может быть и пустой),в которой любая пара различных символов разделяется символом – (пример:+aaa-b-ccc-bbb-c-a-c-aa+).

## Диаграмма переходов

![Untitled Diagram](https://user-images.githubusercontent.com/91876933/205120355-64b25c88-df56-4c19-a3fd-8a6b3ea91a9c.png)\
\0 - дьявольское состояние

## Таблица переходов

|         | a | b | c | + | - |
|---------|---|---|---|---|---|
| -> $q_0$ | $\varnothing$  | $\varnothing$  | $\varnothing$  | $q_1$  | $\varnothing$  |
| $q_1$    |  $q_2$ | $q_3$  | $q_4$  | $q_8$  |  $\varnothing$  |
| $q_2$    | $q_2$  |  $\varnothing$   |  $\varnothing$   |  $q_8$   |  $q_5$ |
| $q_3$    |  $\varnothing$   |   $q_3$  |  $\varnothing$   |   $q_8$  |   $q_6$ |
| $q_4$    |  $\varnothing$   |  $\varnothing$   |   $q_4$ | $q_8$ |  $q_7$  |
| $q_5$    |  $\varnothing$   | $q_3$  | $q_4$  |  $\varnothing$   |  $\varnothing$   |
| $q_6$    | $q_2$  |  $\varnothing$   | $q_4$  | $\varnothing$  |  $\varnothing$   |
| $q_7$    | $q_2$  | $q_3$  |  $\varnothing$   | $\varnothing$  |  $\varnothing$   |
| $q_8$*    | $\varnothing$  | $\varnothing$  | $\varnothing$  | $\varnothing$  | $\varnothing$  |
| $\varnothing$ | $\varnothing$ | $\varnothing$ | $\varnothing$ | $\varnothing$ | $\varnothing$  |


## Регулярное выражение

(+)(+)+(+)+aa*(+)+bb*(+)+cc*(+)+(aa*-)(bb*(+)+cc*(+))+(bb*-)(aa*(+)+cc*(+)+(aa*-)(bb*(+)+cc*(+))+(cc*- +(aa*-)(cc*-)+(bb*-)(aa*(+)+cc*(+)+(aa*-)(bb*(+)+cc*(+))( $\varepsilon$ +(aa*-)(cc*-)+(bb*-)(cc*- +(aa*-)(cc*-))\*(aa\*(+)+bb*(+)+(aa*-)(bb*(+)+cc*(+))+(bb*-)(aa*(+)+cc*(+)+(aa*-)(bb*(+)+cc*(+)))

## Описание:
Программа заключается в рассмотрении всех подстрок, заключенных в “+”. Получим их разбиением исходной строки. Каждую получившуюся подстроку мы проверяем на соответствие условию задачи. Для этого разбиваем каждую из получившихся подстрок на еще меньшие подстроки, используя в качестве разделителя “-“ (например, “b-cc-bb”: “b”, “cc”, “bb”). Проверяем, чтобы символы в каждой были одинаковыми, и примыкающие друг к другу подстроки состояли из разных символов.


## Тесты

1. **Вход:**\
+a-bb-cc++c-ab-cb+c-c-+a-c+c-a+ \
**Выход:**\
{1: '+a-bb-cc+', 9: '++', 23: '+a-c+', 27: '+c-a+'}

2. **Вход:**\
aabb++ccb+a-c-c+\
**Выход:**\
{5: '++'}

3. **Вход:**\
aa+aaa++b-c++\
**Выход:**\
{3: '+aaa+', 7: '++', 8: '+b-c+', 12: '++'}

4. **Вход:**\
a+a-bc-c+a-b-b+a-b-c-c+a-bb+\
**Выход:**\
{23: '+a-bb+'}

5. **Вход:**\
a+a-bbb-cc-aa+aabbcc++\
**Выход:**\
{2: '+a-bbb-cc-aa+', 21: '++'}

6. **Вход:**\
+aaa-b+++c-aaa+cc-a+b-c\
**Выход:**\
{1: '+aaa-b+', 7: '++', 8: '++', 9: '+c-aaa+', 15: '+cc-a+'}

7. **Вход:**\
aa-b+c-aaa+aa-cc++++a-c-b+\
**Выход:**\
{5: '+c-aaa+', 11: '+aa-cc+', 17: '++', 18: '++', 19: '++', 20: '+a-c-b+'}

8. **Вход:**\
++a-c-b+a-bbbb+\
**Выход:**\
{1: '++', 2: '+a-c-b+', 8: '+a-bbbb+'}

9. **Вход:**\
+a-c-bb-cc-a++bb-cc+\
**Выход:**\
{1: '+a-c-bb-cc-a+', 13: '++', 14: '+bb-cc+'}

10. **Вход:**\
aaaa+aaa-bb+bb-c\
**Выход:**\
{5: '+aaa-bb+'}

11. **Вход:**\
+a+a+b+c+cccc+bbb\
**Выход:**\
{1: '+a+', 3: '+a+', 5: '+b+', 7: '+c+', 9: '+cccc+'}

12. **Вход:**\
++a-c-b+c-a+\
**Выход:**\
{1: '++', 2: '+a-c-b+', 8: '+c-a+'}

13. **Вход:**\
aa-ccc+cc-aa-bb++\
**Выход:**\
{7: '+cc-aa-bb+', 16: '++'}

14. **Вход:**\
a-c-b+a-c\
**Выход:**\
{}

15. **Вход:**\
++++\
**Выход:**\
{1: '++', 2: '++', 3: '++'}



