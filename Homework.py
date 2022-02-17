
#1. Գրել ծրագիր, որը օգտագործողից հարցնում է աշխատանքային ժամերի քանակը, մեկ ժամի դրույքաչափը և հաշվում աշխատավարձը:
#Oրինակ.
#     Enter Hours: 35
#     Enter Rate: 2.75
#     Pay: 96.25

import time
working_hours_number=float(input("Enter the number of working hours:"))
rate=float(input("enter the rate:"))
print(working_hours_number*rate)

time.sleep(3)