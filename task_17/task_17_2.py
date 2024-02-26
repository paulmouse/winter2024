# Задание 17 2
# Создайте декоратор, которые переводит все текстовые аргументы функции в верхний регистр и возвращает их в виде списка текстовых аргументов.
# Текстовые аргументы – это строки в args и строковые значения в kwargs.

def upperCase(func):
    def wrapper(*args, **kwargs):
        aList = []
        #print(args)
        for arg in args:
            a = arg.upper()
            aList.append(a)
        for arg in kwargs:
            a = kwargs[arg].upper()
            aList.append(a)
        print(aList)
        return func#(*args, **kwargs)
    return wrapper

@upperCase
def test(*args, **kwargs):
    pass

test('Hello', 'World', 'upper', 'for', 'args', v1 = 'Hello', v2 = 'kwargstest')