import sys

otherFiles=[]
for i in range(1,len(sys.argv)):
    f = open(sys.argv[i], "r")
    a=[]
    for x in f:
        a.append(x.split())
    if(i==1):
        mainFile=a
    else:
        otherFiles.append(a)

def SD(X,Y):
    setX=set()
    setY=set()
    for i in X:
        for j in i:
            setX.add(j)
    for i in Y:
        for j in i:
            setY.add(j)
    setZ=setX.symmetric_difference(setY)
    #print(setZ)
    return len(setZ), len(setX), len(setY)
max_sim_score=0
for j,i in enumerate(otherFiles):
    a,b,c=SD(mainFile, i)
    print("Sim(", sys.argv[1], ",", sys.argv[2+j], ") =", 1-a/(b+c))
    if(1-a/(b+c)>=max_sim_score):
        max_sim_score=1-a/(b+c)
        mostSimilar = sys.argv[2+j]
print("File", mostSimilar, "is most similar to file",sys.argv[1])