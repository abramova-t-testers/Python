def quarter_of_year(month):
    if 1 <= month <= 3:
        return "I квартал"
    elif 4 <= month <= 6:
        return "II квартал"
    elif 7 <= month <= 9:
        return "III квартал"
    elif 10 <= month <= 12:
        return "IV квартал"
    else:
        return "Неверно"


month = int(input("Введите номер месяца:"))
print(quarter_of_year(month))
