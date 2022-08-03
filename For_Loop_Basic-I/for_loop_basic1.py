1.
for x in range(151):
    print(x)

2.
for x in range(0,1001,5):
    print(x)

3.
for x in range(1,101):
    if x % 10 == 0:
        print("Coding Dojo")
    elif x % 5 == 0:
        print("Coding")
    else:
        print(x)

# 4.
sum = 0
for x in range(1,500000):
    if x % 2 != 0:
        sum += x
print(sum)

# 5.
for x in range(2018,0,-4):
    if x % 2 == 0:
        print(x)

# 6.
low_num = 2
high_num = 9
mult = 3

for i in range(low_num,high_num + 1):
    # print(i)
    if i % mult == 0:
        print(i)