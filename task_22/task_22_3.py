import keyword
def replaceKeywords(text):
    keywords = keyword.kwlist
    for kw in keywords:
        text = text.replace(kw, '<kw>')
    return text

text = 'Напишите continue программу, True которая is принимает as строку else текста for и заменяет from в ней in все lambda ключевые try слова'
modifiedText = replaceKeywords(text)
print(modifiedText)