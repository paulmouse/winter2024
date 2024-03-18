# Напишите функцию, которой на вход подается строка, содержащая
# последовательность слов (которые могут включать буквы верхнего и нижнего
# регистра). На выходе должна получиться строка в CamelStyle.
# Например, "camel case word" => CamelCaseWord

def to_camel_style(inputString):
    # words = input_string.split()
    # for word in words:
    #     print(word)
    #     capWord = word.capitalize()
    capWord = inputString.title()
    # print(capWord)

    outputString = capWord.replace(' ', '')

    return outputString

inputString = "camel case word"
result = to_camel_style(inputString)
print(result)