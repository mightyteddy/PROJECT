pythonGisa = open("파이썬기사.txt", "r", encoding="UTF8")
pythonGisaRead = pythonGisa.read()
pythonGisaList = pythonGisaRead.split(" ")
pythonNum = 0
for i in pythonGisaList:
    if "파이썬" in i:
        pythonNum += 1
print(pythonNum)

