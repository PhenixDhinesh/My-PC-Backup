d = {}
for _ in range(int(input())) :
    line = input().strip().split()
    name = " ".join(line[:-1])
    count = int(line[-1])
    if name in d :
        d[name] += count
    else :
        d[name] = count
for a,b in sorted(d.items()) :
    print(a,b)