def isIteger(s):
    """Проверяем является ли строка числом"""
    if s.isdigit():
        return "Строка является числом"
    else:
        try:
            float(s)
            return "Строка явялется числом"
        except ValueError:
            return "Строка не является числом"

print("Введите число:" )
print(isIteger(input()))

#Вывод 
Введите число:
+265451
Строка явялется числом