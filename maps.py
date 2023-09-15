#0 = empty; 1=block; 2=picobot; 3=passed

empty = """
00000000000000000000000
00000000000000000000000
00000000000000000000000
00000000000000000000000
00000000000000000000000
00000000000000000000000
00000000000000000000000
00000000000000000000000
00000000000000000000000
00000000000000000000000
00000000000000000000000
00000000000000000000000
00000000000000000000000
00000000000000000000000
00000000000000000000000
00000000000000000000000
00000000000000000000000
00000000000000000000000
00000000000000000000000
00000000000000000000000
00000000000000000000000
00000000000000000000000
00000000000000000000000
00000000000000000000000"""

maps = {
    "empty": empty
}

translations = {
    "0": "empty",
    "1": "block",
    "2": "picobot",
    "3": "passed",
}

def parseMap(map):
    arrMap = map.split("\n")[1:]

    for i, j in enumerate(arrMap):
        arrMap[i] = [*arrMap[i]]

    for i, ii in enumerate(arrMap):
        for j, jj in enumerate(arrMap[i]):
            arrMap[i][j] = translations[arrMap[i][j]]

    return arrMap


if(__name__ == "__main__"):
    print(parseMap(empty))