def separate_list(numbers):
    even_list = []
    odd_list = []

    for i in numbers:
        if i % 2 == 0:
            even_list.append(i)
        elif i % 2 != 0:
            odd_list.append(i)

    return even_list, odd_list


numbers = [12, 7, 9, 20, 33, 46, 51, 8]

e_list, o_list = separate_list(numbers)

print("Even numbers:", e_list)
print("Odd numbers:", o_list)