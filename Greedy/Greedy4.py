a,b = map(int,input().split())
count = 0

while (1):
    if (a<=1):
        break

    if (a%b == 0):
        a /= b
        count += 1
    else:
        a -= 1
        count += 1

print(count)
