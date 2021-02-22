
def getInput():
    scalingY = 1000
    scalingX = 1000
    x = []
    y = []
    label = []
    for line in open("inputCoordinates.txt").readlines():
        values = line[:-1].split(",")
        y.append(float(values[0])/scalingY) #webots is reversed
        x.append(float(values[1])/scalingX)
        label.append(int(values[2]))

    return x, y, label


if __name__ == "__main__":
    
    xList, yList, labelList = getInput()

    result = ""
    i=0
    for x, y, label in zip(xList, yList, labelList):
        if label == 3 or label == 0: 
            colour = "blue"
        else:
            colour = "yellow"
        translation = str(round(float(x),2)) + " -0.3 " + str(round(float(y),2))
        name = "cone" + colour + str(i)
        content = f'\n\ttranslation {translation}\n\tname "{name}"\n\tcolor "{colour}"\n'
        fullString = "FsCone {" + content + "}\n"
        i+=1
        result += fullString 

    open("map.txt", "w").write(result)