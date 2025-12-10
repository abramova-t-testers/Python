# dev_by_three_as_str = input("Делится ли на три <число>?")
# dev_by_three = int(dev_by_three_as_str)
# feedback = ' '
# if dev_by_three % 3 == 1:
#     feedback = input("Нет")
# else: feedback = input("Да")
# print(feedback)

def dev_by_three(number):
    return "Да" if number % 3 == 0 else "Нет"


num = int(input("Введите число: "))
result = dev_by_three(num)
print(f"Делится ли на три {num}? - {result}")
