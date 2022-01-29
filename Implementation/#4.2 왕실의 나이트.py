#4.2 왕실의 나이트

n = input()
a = n[0]
col = int(n[1])
row = int(ord(a)-ord('a')) +1
count = 0

movetype = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,-2),(-1,2)]

for i in movetype:
    newcol = col + i[1]
    newrow = row + i[0]
    if (0<newcol<9 and 0<newrow<9):
        count += 1

print(count)
