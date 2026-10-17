with open("data.txt", "r")as file:
    lines = file.readlines()
print("total lines:",len(lines)) 
if len(lines) >= 2:
    print("second line:", lines[1].strip())
if len(lines)>=4:
    print("Fourth line:",lines[3].strip())       