print("this program saved 1000000000 number in 20 files")
print("file saved as gen0.txt,gen1.txt,gen2.txt,...gen19.txt")
print("for open file enter name(as gen12.txt or gen4.txt)")

def findsmallest(arr):
    smallest=arr[0]
    smallest_index=0
    for i in range(1,len(arr)):
        if arr[i]<smallest:
            smallest=arr[i]
            smallest_index=i
    return smallest_index


def selectionsort(arr):
    newArr=[]
    for i in range(len(arr)):
        smallest=findsmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

def gen(n):
    dict1={}
    for i in range(n):

        import random
        a=random.randint(1,100)
        if a in dict1.keys():
            dict1[a]=dict1[a]+1
        else:
            dict1[a]=1
    return dict1

def list1(dict3):
    l=[]
    for i in selectionsort(list(dict3.keys())):
        for j in range(dict3[i]):
            # print(i,end=',')
            l.append(i)
    return l


for i in range(20):
    s='gen'+str(i)+'.txt'
    with open(s,'w') as file:
        file.write(str(list1(gen(50000000))))

while True:
    a=input('enter file number(0-20)')
    with open(a,'r') as file:
        print(file.read())
        file.close()





