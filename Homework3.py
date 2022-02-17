 #3. Գրել ծրագիր, որը օգտագործողից որպես մուտքային տվյալ կստանա տառ և կտպի հաղորդագրություն, տառը ձայնավոր է,
  #բաղաձայն, թե և՜ ձայնավոր, և՜ բաղաձայն: Ձայնավոր են a, e, i, o, u տառերը, y-ը և՜ ձայնավոր է, և՜ բաղաձայն, մնացածը՝ բաղաձայն:

import time

while True:
    a=input("enter the letter: ")
    if a in ('a','e','i','o','u'):
        print("the '",a,"' is vocals")
    else:
        print("the '",a,"' is not vocal")
 time.sleep(5)