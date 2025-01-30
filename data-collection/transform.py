with open("test.txt", "r") as file:
    lines = file.readlines()

count = 1
for line in lines:
    line = line.strip().split("&")[1:]
    current = ""
    current += f"T_{{{count}}} "
    for i in range(len(line)):
        current += "&"
        current += line[i]
    count += 1
    print(current)
