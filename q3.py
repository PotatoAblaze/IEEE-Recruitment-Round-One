line = input().strip("[] ").split(",")
line = [int(x) for x in line]
l = len(line)
print("[")
for x in range(0, pow(2, l)):
    c = x
    curr_index = 0
    print("[", end="")
    while(c > 0):
        if(c % 2 == 1):
            print(f"{line[curr_index]},", end="")
        c = c >> 1 # Same as c = c // 2, shifting 1 bit
        curr_index = curr_index + 1
    
    print("], ")
        

print("]")
