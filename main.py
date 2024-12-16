#read gcode
#slice
#assemble slices
#pack




maxSlice  = 4
configuration = [[4,60,60],[3,60,70]] #sides,center x, center y
safeXpos  = 80
startingZ = 0
preCode = "preCode.gcode"
postCode = "postCode.gcode"

#read gcode


squareSteps = []
squareFile = open("square.gcode")
for line in squareFile.read().split("\n"):
    if not line == "":
        if not line[0] == ";":
            if line.split(" ")[0][:1] == "G":
                args = line.split(" ")
                argsF = [None,None,None,None,None,None]
                for arg in args:
                    letter = arg[:1]
                    if letter == "G":
                        argsF[0] = arg
                    if letter == "X":
                        argsF[1] = arg[1:]
                    if letter == "Y":
                        argsF[2] = arg[1:]
                    if letter == "Z":
                        argsF[3] = arg[1:]
                    if letter == "E":
                        argsF[4] = arg[1:]
                    if letter == "F":
                        argsF[5] = arg[1:]
                squareSteps.append(argsF)
            else:
                squareSteps.append([line])

triangleSteps = []
triangleFile = open("square.gcode")
for line in triangleFile.read().split("\n"):
    if not line == "":
        if not line[0] == ";":
            if line.split(" ")[0][:1] == "G":
                args = line.split(" ")
                argsF = [None,None,None,None,None,None]
                for arg in args:
                    letter = arg[:1]
                    if letter == "G":
                        argsF[0] = arg
                    if letter == "X":
                        argsF[1] = arg[1:]
                    if letter == "Y":
                        argsF[2] = arg[1:]
                    if letter == "Z":
                        argsF[3] = arg[1:]
                    if letter == "E":
                        argsF[4] = arg[1:]
                    if letter == "F":
                        argsF[5] = arg[1:]
                triangleSteps.append(argsF)
            else:
                triangleSteps.append([line])

