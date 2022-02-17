
#Գրել ծրագիր, որն անընդհատ ընդունում է թվեր մինչև օգտագործողը մուտքագրում է «done»: «done» մուտքագրելուց հետո տպել մուտքագրված թվերի գումարը, քանակը,և միջին թվաբանականը: Եթե օգտագործողը մուտքագրում է այլ բան թվի փոխարեն, տպել հաղորդագրություն սխալ մուտքի մասին և սպասել հաջորդ թվին: 
#   	Enter a number: 4
#  	Enter a number: 5
# 	Enter a number: bad data
#	Invalid input
#	Enter a number: 7
#   Enter a number: done
#16 3 5.333333333333333

import time
summ=0
num=0

while True:
   a=(input("enter a number:  "))
   if a=="done":
     print("the summ of nubers is ",summ)
     print("the quantity of number is ",num)
     print("the arithmetic average of nubers is ", summ/num)
     break
   b=int(a)
   summ+=b 
   num+=1

time.sleep(5)