n = int(input())

ugly = {1}
now = 1 
while len(ugly) != n:
    if now % 2 == 0:
        if now // 2 in ugly:
            ugly.add(now)
    elif now % 3 == 0:
        if now // 3 in ugly:
            ugly.add(now)
    elif now % 5 == 0:
        if now // 5 in ugly:
            ugly.add(now)
    now += 1

print(max(ugly)) 


