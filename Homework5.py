#5. Ստեղծել ծրագիր, որը օգտագործողից կստանա ջերմաստիճան ըստ Ֆարենհայտի և կտպի համապատասխան ջերմաստիճանը
#արտահայտված ըստ Ցելսիուսի։ Ֆարենհայտից Ցելսիուսի փոխարկման բանաձևը՝ °C = (°F - 32)/1.8։

import time
f=float(input("enter the temperature in farenhite: "))
print("the temperature in celsius is: ",(f - 32)/(1.8))

time.sleep(5)