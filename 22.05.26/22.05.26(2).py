
l = list(map(int, input("Enter list: ").split()))
n = int(input("Enter number: "))
count = 0
for i in range(len(l)):
    if l[i] != n:
        l[count] = l[i]
        count += 1
for i in range(count, len(l)):
    l[i] = n
print("list:", l)
print("Count:", count)
