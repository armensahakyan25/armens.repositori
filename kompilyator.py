print("###...kompilyatorum popoxakan nermucelu hamar petq e grel 'var' bary aynuhetev 'var a = 1' 'a' in kta 1 arjeqy")
print("###...tpelu hamar 'tpel a' ktpi a popoxakani arjeqy, 'a = 2 + 3' artahaytutyuny 'a' in talis e '2 + 3' arjeqy")

dic={}
def var(a):
    list1=a.split()
    dic[list1[1]]=(list1[3])
def tpel(a):
    list1 =a.split()
    print(dic[list1[1]])


def arch(a):
    list1=a.split()
    if list1[3]=="+":
        dic[list1[0]]=(int(list1[2])+int(list1[4]))
        #print(int(list1[2])+int(list1[4]))
    elif list1[3]=="-":
        dic[list1[0]] = (int(list1[2]) - int(list1[4]))
        #print(int(list1[2])-int(list1[4]))
    elif list1[3]=="*":
        dic[list1[0]] = (int(list1[2]) * int(list1[4]))
        #print(int(list1[2])*int(list1[4]))
    elif list1[3]=="/":
        dic[list1[0]] = (int(list1[2]) / int(list1[4]))
        # print(int(list1[2])/int(list1[4]))
    else:
        dic[list1[0]] = list1[2]
while True:
    a=input()
    l=a.split()
    if (l[0]=='var'):
        var(a)
    elif (l[0]=='tpel'):
        tpel(a)
        print(dic)
    else:
        arch(a)
# var('var a = 1')
# var('var b = 2')
# var('var c = 3')
# var('var d = 4')
# print(dic)
# tpel('tprl a')
# tpel('tprl b')
# tpel('tprl c')
# tpel('tprl d')