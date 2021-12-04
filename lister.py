def funk():
    spis = list()
    m = input()
    while m != "":
        spis.append(m)
        m = input()
    spis.sort(key=int)
    return spis
