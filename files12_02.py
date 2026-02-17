# Կարդալ ֆայլը և տպել բոլոր անունները։
# with open ('users.txt','r') as f:
#     for lines in f:
#         parts=lines.strip().split(',')
#         print (parts[:-1])

# Մուտք ընդունել id և տպել համապատասխան user-ը։

# with open ('users.txt','r') as f:
#     id=input('enter your id')
#     for lines in f:
#         parts=lines.strip().split(',')
#         if id==parts[0]:
#             print(parts[1])


# Փոխել id = 2 user-ի age → 30

# fd = open("users.txt", "r+")
# content = fd.readlines()
# for i in range(len(content)):
#     parts = content[i].strip().split(",")
#     # print(parts)
#     if parts[0] == '2':
#         parts[-1] = '30'
#     content[i] = ",".join(parts) + "\n"
    
# print(content)
# fd.seek(0)
# fd.writelines(content)
# fd.close()

# Տպել բոլոր user-ներին որոնց age >= 21
# fd = open("users.txt", "r+")
# content = fd.readlines()
# for i in range(len(content)):
#     parts = content[i].strip().split(",")
#     if int(parts[-1]) >= 21:
#         print(content[i])

# Տպել քանի user կա ֆայլում։

# fd = open("users.txt","r+")
# content = fd.readlines()
# print(len(content))

# Սորտ անել user-ներին ըստ age և գրել ֆայլի մեջ։

fd = open("users.txt","r+")
content = fd.readlines()
for i in range(len(content)):
    parts=content[i].strip().split(",")
    parts[-1]=int(parts[-1])
    content[i] = parts

print(content)
content.sort(key=lambda x: x[2])
print(content)
fd.seek(0)

for i in range(len(content)):
    parts=[str(x) for x in content[i]]
    line = ",".join(parts) + "\n"
    fd.write(line)