def myfunc(m,outf):
    asum = []
    bsum = []
    sumo = 0
    for y,x in enumerate(outf):
        sumo += x
        if x == m and sumo <= m:
            bsum.append([x])
            asum, sumo = [], 0
        elif sumo <= m:
            asum.append(x)
            if sumo == m or y == len(outf)-1:
                bsum.append(asum)
                asum, sumo = [], 0
        elif sumo > m:
            bsum.append(asum)
            asum, sumo = [], 0
            if x == m : bsum.append([x])

    return max([ len(x) for x in bsum ])

print(myfunc(6,[2,3,6,1,1,2]))