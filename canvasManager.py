import maps

loadedMap = None


def placePixel(canvas, x, y, pixeltype):

    #offset from edge of map for borders
    # x += 1
    # y += 1
    
    canvas.create_rectangle((x*20, y*20), (x*20+20, y*20+20), fill=maps.colors[pixeltype])



def loadMap(canvas, mapname):

    mapdata = maps.parseMap(maps.maps[mapname])
    
    # print(mapdata)

    limitx = 0
    limity = 0

    for i, ii in enumerate(mapdata):
        for j, jj in enumerate(mapdata[i]):
            # the list is split up so i is the i value and j is the x value. I didnt want it like this but too bad for me ig
            # placePixel(canvas, j, i, mapdata[i][j])

            canvas.create_rectangle((j*20, i*20), (j*20+20, i*20+20), fill=maps.colors[mapdata[i][j]])

            limity = i
            limitx = i

    global loadedMap
    loadedMap = mapdata
