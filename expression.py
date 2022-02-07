a = float(input("Введите число a: "))
b = float(input("Введите число b: "))
c = float(input("Введите число c: "))
expr1 = (a ** 2 + b ** 2) / (3 * b - 4)
expr2 = 4 * c ** 5 / 6
print(expr1)
print(expr2)
print("Целая часть от деления выражения_1 на выражение_2:", expr1 // expr2)
print("Остаток от деления выражения_1 на выражение_2:", expr1 % expr2)
