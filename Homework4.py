
# 4 Գրել ծրագիր, որը կստանա շախմատի վանդակի կոորդինատները և կտպի վանդակի գույնը։ 

import time
x=(input("enter the 'x' cordinat: "))
y=int(input("enter the 'y' cordinat: "))
add={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
if ((add[str(x)])*y)%2==1:
    print("Black")
else:
    print("White")

time.sleep(5)