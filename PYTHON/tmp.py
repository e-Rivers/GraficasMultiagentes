def test(n):
    lines = ["12345","54321"]
    cityMap = []
    #with open('base.txt') as baseFile:
    #    lines = baseFile.readlines()

    for line in lines:
        cityMap.append("".join([item for i in range(n) for item in line.replace("\n","")]))
    cityMapCopy = cityMap.copy()
    for i in range(n-1):
        print(cityMapCopy)
        print("o o o o o")
        cityMap.extend(cityMapCopy)


    print("")
    print("")
    print("")
    print(lines)
    print("")
    print("")
    print("")
    print(cityMap)


test(3)
