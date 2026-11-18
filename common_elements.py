
# Q6: Find Common Elements in Two Lists

def common_elements(list1, list2):
    common = []
    for i in list1:
        if i in list2:
            common.append(i)
    return common


# Main Program

list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 50, 60, 70]

result = common_elements(list1, list2)

print("Common elements:", result)
