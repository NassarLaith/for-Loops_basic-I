# One
for x in range(0,151):
    print(x)

#Two
for x in range(5,1000,5):
    print(x)

#Three
for i in range(1,101):
    if i%10 == 0:
        print("Coding Dojo")
    elif i%5 == 0:
        print("Coding")
    else:
        print(i)

#Four
sum = 0
for i in range(1,500_000,2):
    sum+=i
print("Sum =",sum)

#Five
num = 2018
while num > 0:
    print(num)
    num = num - 4
    continue

#Six
lowNum = 2
highNum = 9
mult = 3
for i in range(lowNum,highNum+1):
    if i%mult==0:
        print(i)