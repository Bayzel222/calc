import math
stroka = []
def spis(x, y):
    for i in range(max(len(x), len(y))):
        if i < len(x):
            stroka.append(x[i])
        if i < len(y):
            stroka.append(y[i])
    return stroka
    
def parse_command(command: str) -> list:
	parsedlone = command.replace(' ','')
	res = list(parcedlone)
	return res

def calc(command: str) -> float:
	precalc = ''.join(parce_command)(command)
	res = eval(precalc)
	return res

def getfromfile(file_name: str):
	with open(file_name, 'r') as f:
		line = f.readline()
	return line


i = 0
import sys
if len(sys.argv) <= 1:
    command = input("Введите значения? ")
    print(calc(command))
else:
    filename = sys.argv[1]
<<<<<<< HEAD
    f = open('output.txt', 'w')
    f.close()
=======
>>>>>>> 499de6ed9d7b924bd94ea7857a42a008390a50d5
    command = getfromfile(filename)
    c = len(command)
    for i in range(c):
        y = calc(command[i])
        print(y)
        with open('output.txt', 'a') as f:
<<<<<<< HEAD
            f.writelines(str(y) + '\n')
=======
            f.writelines(str(y) + '\n')
>>>>>>> 499de6ed9d7b924bd94ea7857a42a008390a50d5
