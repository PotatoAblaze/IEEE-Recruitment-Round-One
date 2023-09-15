t = int(input())

for i in range(0, t):
    n = input("Enter numbers in single line: ").strip().split(" ")
    n = [abs(int(x)) for x in n]
    l = len(n)
    if(l < 2):
        print(n[0])
        continue

    pos_range = [n[x] for x in range(0, l, 2)]
    neg_range = [n[x] for x in range(1, l, 2)]

    min_pos_num = min(pos_range)
    max_neg_num = max(neg_range)

    if(min_pos_num < max_neg_num):
        t = max_neg_num
        neg_range.remove(max_neg_num)
        pos_range.remove(min_pos_num)
        pos_range.append(max_neg_num)
        neg_range.append(min_pos_num)
        
    result = sum(pos_range) - sum(neg_range)
    print(result)