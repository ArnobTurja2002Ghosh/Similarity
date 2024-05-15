import sys
import collections

otherFiles=[]
for i in [1]+list(range(3,len(sys.argv))):
    f = open(sys.argv[i], "r")
    a=[]
    for x in f:
        if(x!="\n"):
            if(len(x[0:-1])>=int(sys.argv[2])):
                a.append(x.split())
    if(i==1):
        mainFile=a
    else:
        otherFiles.append(a)
    print(a)

b='aba ba'

n=int(sys.argv[2])
freq=collections.Counter([b[i:i+n] for i in range(len(b)-n+1)])
print(freq)
for i,j in freq.items():
    print(i, j, freq.total())

a1=[['aba', 'ba'], ['bab'], ['abaaa']]

def list_to_ngrams(a):
    list1=[]
    for i in a:
        for ii in i:
            list1.extend([ii[j:j+n] for j in range(len(ii)-n+1)])
    print(list1, collections.Counter(list1))
    return collections.Counter(list1)




def counter_to_frequency(c1):
    d1={}
    for i in c1:
        d1[i]=c1[i]/c1.total()
    print(d1)
    return d1

main_file_f =counter_to_frequency(list_to_ngrams(mainFile))
other_files_f =[]
for i in otherFiles:
    other_files_f.append(counter_to_frequency(list_to_ngrams(i)))

# counter_to_frequency(list_to_ngrams(mainFile))
# counter_to_frequency(list_to_ngrams(otherFiles[1]))

def Diff(d1, d2):
    a=set(d1)
    b=set(d2)
    sum=0
    for i in a.intersection(b):
        sum+= abs(d1[i]-d2[i])
    for i in a.difference(b):
        sum+=d1[i]
    for i in b.difference(a):
        sum+=d2[i]
    # print(sum)
    return sum
def Sim(d1, d2):
    return 1-Diff(d1, d2)/2
for i in other_files_f:
    print(Sim(main_file_f, i))