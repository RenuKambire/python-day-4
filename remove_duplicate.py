def remove_duplicates(numbers):
    new_list = []

    for num in numbers:
        if num not in new_list:
            new_list.append(num)

    return new_list


numbers = [10, 20, 10, 30, 20, 40, 50, 30]

result = remove_duplicates(numbers)

print(result)