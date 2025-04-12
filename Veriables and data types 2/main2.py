number = input("Введіть тризначне число: ")
if len(number) == 3 and number.isdigit():
    first_digit = int(number[0])
    second_digit = int(number[1])
    third_digit = int(number[2])
    sum_digits = first_digit + second_digit + third_digit
    print(first_digit)
    print(second_digit)
    print(third_digit)
    print(sum_digits)
    print("Будь ласка, введіть коректне тризначне число.")

