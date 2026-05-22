def listexample(num, inc, base):
    i = len(num) - 1
    num[i] += inc
    while i >= 0:
        if num[i] >= base:
            carry = num[i] // base
            num[i] = num[i] % base
            if i == 0:
                num.insert(0, carry)
            else:
                num[i - 1] += carry
        i -= 1
    return num

digits = list(map(int, input("Enter digits: ").split()))
inc = int(input("Enter inc: "))
base = int(input("Enter base: "))
result = listexample(digits, inc, base)
print(result)
