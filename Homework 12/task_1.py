"""Вирус повредил систему прав доступа к файлам. Известно, что над каждым файлом можно производить
определенные действия:
запись – W;
чтение – R;
запуск – X.
На вход программе подается:
число n – количество файлов;
n строк с именами файлов и допустимыми операциями;
число m – количество запросов к файлам;
m запросов вида «операция файл».
Для каждого допустимого запроса программа должна возвращать OK, для недопустимого – Access denied."""

actions_permissions = {
    'write': 'W',
    'read': 'R',
    'execute': 'X'
}
result = ''
files_actions = {}
n = int(input('Please enter a number of required files - '))

for i in range(n):
    file, *permissions = input('Add file and permission to it (where W- write, R - read, X - execute): ').split()
    files_actions[file] = set(permissions)

m = int(input('Please enter number of actions to files - '))

for i in range(m):
    action, file = input('Add action and file: ').split()
    if actions_permissions[action] in files_actions[file]:
        res_1 = 'OK'
        result += res_1 + '\n'
    else:
        res_2 = 'Access denied'
        result += res_2 + '\n'
print(result)
