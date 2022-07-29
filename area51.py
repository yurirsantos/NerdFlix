series = [1, 2, ]
tamnho = len(series)

cod = int(input("cod.. "))

while cod < 0 or cod > tamnho:
    print("Op inváliada")
    input()
