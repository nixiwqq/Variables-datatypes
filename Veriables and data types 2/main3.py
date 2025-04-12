first_digit = input("Введіть першу цифру: ")
second_digit = input("Введіть другу цифру: ")
if first_digit.isdigit() and second_digit.isdigit():
    new_number = first_digit + second_digit
    print("Сформоване число:", new_number)
else:
    print("Будь ласка, введіть дійсні цифри.")
