#read gcode
#slice
#assemble slices
#pack
import math



maxSlice  = 4
configuration = [[4,60,60]] #sides,center x, center y
safeXpos  = 80
startingZ = 0
preCode = "preCode.gcode"
postCode = "postCode.gcode"

#read gcode


squareSteps = []
squareFile = open("square.gcode","r")
prevE = 0
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
                        argsF[1] = float(arg[1:])-117.5
                    if letter == "Y":
                        argsF[2] = float(arg[1:])-117.5
                    if letter == "Z":
                        argsF[3] = float(arg[1:])
                    if letter == "E":
                        argsF[4] = float(arg[1:])-prevE
                        prevE=float(arg[1:])
                    if letter == "F":
                        argsF[5] = float(arg[1:])
                squareSteps.append(argsF)
            else:
                squareSteps.append([line])

triangleSteps = []
triangleFile = open("triangle.gcode","r")
prevE = 0
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
                        argsF[1] = float(arg[1:])-117.5
                    if letter == "Y":
                        argsF[2] = float(arg[1:])-117.5
                    if letter == "Z":
                        argsF[3] = float(arg[1:])
                    if letter == "E":
                        argsF[4] = float(arg[1:])-prevE
                        prevE=float(arg[1:])
                    if letter == "F":
                        argsF[5] = float(arg[1:])
                triangleSteps.append(argsF)
            else:
                triangleSteps.append([line])


triz=0
for step in triangleSteps:
    if step[0] == "G1":
        if not step[3] == None and step[3] > triz:
            triz = step[3]
print(triz)





sqrz=0
for step in squareSteps:
    if step[0] == "G1":
        if not step[3] == None and step[3] > sqrz:
            sqrz = step[3]
squareSlices = [[[None,None,None,None,None,None]],[[None,None,None,None,None,None]],[[None,None,None,None,None,None]],[[None,None,None,None,None,None]],[[None,None,None,None,None,None]],[[None,None,None,None,None,None]],[[None,None,None,None,None,None]],[[None,None,None,None,None,None]],[[None,None,None,None,None,None]],[[None,None,None,None,None,None]],[[None,None,None,None,None,None]]]
z = 0
for step in squareSteps:
    if step[0] == "G1" or step[0] == "G0" :
        if not step[3] == None:
            z = step[3]
    squareSlices[math.floor(z/maxSlice)].append(step)


print(squareSteps)

preCodeFile = open(preCode,"r")

GCODE = preCodeFile.read()




postCodeFile = open(postCode,"r")

GCODE += postCodeFile.read()

GCODEFile = open("output.gcode","w")
GCODEFile.write(GCODE)
GCODEFile.close()
