# Задание 17 2
# Создайте декоратор, которые переводит все текстовые аргументы функции в верхний регистр и возвращает их в виде списка текстовых аргументов.
# Текстовые аргументы – это строки в args и строковые значения в kwargs.

def upperCase(func):
    def wrapper(*args, **kwargs):
        aList = []
        #print(args)
        for arg in args:
            if type(arg) != str:
                #print(type(arg))
                #print('')
                pass
            else:
                a = arg.upper()
                aList.append(a)
        for arg in kwargs:
            if type(kwargs[arg]) != str:
                #print(type(arg))
                pass
            else:
                a = kwargs[arg].upper()
                aList.append(a)
        print(aList)
        return func#(*args, **kwargs)
    return wrapper

@upperCase
def test(*args, **kwargs):
    pass

test(1, 'Hello', 'World', 234,[1,2,3], 'upper', 'for', 'args', v1 = 'Hello', v2 = 'kwargstest', v3 = 333)