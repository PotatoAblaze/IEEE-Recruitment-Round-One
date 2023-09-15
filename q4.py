l = 5
n = input("Enter numbers in single line: ").strip().split(" ")
n = [int(x) for x in n]


hcf = n[0]
for x in range(0, l-1):
    if(hcf == 1):
        break
    divisor = min(hcf, n[x+1])
    dividend = max(hcf, n[x+1])
    while(True):
        remainder = dividend % divisor
        if(remainder == 0):
            hcf = divisor
            break
        else:
            dividend = divisor
            divisor = remainder

print(f"HCF of 5 numbers is: {hcf}")
            