
    # Заглавные буквы
# s - исходная строка 

def capitalize(s):
    result = s
    # первый непробельный символ заглавный
    pos = 0
    while pos < len(s) and result[pos] == ' ':
        pos = pos + 1
    if pos < len(s):
        result = result[0 : pos] + result[pos].upper() + \
        result[pos + 1 : len(result)]
    # первая буква после точки , восклицвткльного или вопросительного знаков   
    pos = 0
    while pos < len(s):
        if result[pos] == "." or result[pos] == "!" or \
            result[pos] == "?":
            pos = pos + 1
            while pos < len(s) and result[pos] == " ":
                pos = pos + 1
        if pos < len(s):
            result = result[0 : pos] + \
            result[pos].upper() + \
            result[pos + 1 : len(result)]
        pos = pos + 1
    # заглавные буквы i    
    pos = 1
    while pos < len(s) - 1:
        if result [pos - 1] == " " and result[pos] == "i" and \
           (result[pos + 1] == " " or result[pos + 1] == "." or \
            result[pos + 1] == "!" or result[pos + 1] == "?" or \
            result[pos + 1] == "'"):
            result = result[0 : pos] + "I" + \
            result[pos + 1 : len(result)]
        pos = pos + 1
    return result
def main():
    s = input("Введите текст: ")
    capitalized = capitalize(s)
    print("Новая версия: ", capitalized)
main()    

#Вывод #Знаю что не доработано не понял шде не правильно.
Введите текст: "what time do i have to be there? what`the address? i`ll try to be there on time!"
Новая версия:  "WHAT TIME DO I HAVE TO BE THERE? WHAT`THE ADDRESS? I`LL TRY TO BE THERE ON TIME!"