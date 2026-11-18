with open("data.txt", "r")as file:
    content = file.read()
count =0
for i in content:
    if i in "aeious":
        count += 1
print("total vowels:-",count)            