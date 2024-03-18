# Напишите функцию, которой на вход подается строка, содержащая
# последовательность слов (которые могут включать буквы верхнего и нижнего
# регистра). На выходе должна получиться строка в CamelStyle.
# Например, "camel case word" => CamelCaseWord

def toCamelStyle(inputString):
    # words = input_string.split()
    # for word in words:
    #     print(word)
    #     capWord = word.capitalize()
    capWord = inputString.title()
    # print(capWord)

    outputString = capWord.replace(' ', '')

    return outputString

inputString = 'camel caSe wOrd teSt 4 for test'
res = toCamelStyle(inputString)
print(res)