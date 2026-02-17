# Փոխել id = 2 user-ի age → 30
# Ֆայլը պետք է ամբողջությամբ rewrite անել։


with open("users.txt", "r+") as fff:
    temp = fff.readlines()
    fff.seek(0)
    for i in temp:
        if(i.startswith("2")):
            x = i.split(",")
            fff.write(f"{x[0]},{x[1]},30\n")
            continue
        fff.write(i)