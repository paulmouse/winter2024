# Задача 163
# Создайте декоратор, который переводит результат функций в нижний регистр.

def lowerCase(func):
    def wrapper():
        origResult = func()
        modifyResult = origResult.lower()
        return modifyResult
    return wrapper
@lowerCase
def h():
    return 'ИнсТитуТ ТочнОй МехАниКи ОпТикИ'
print(h())