
def multi(d):#դարձնում է լիստ
    for i in d:
        for j in range(d[i]):
            print(i,end=" ")
    return 0




def gumar(d):#հաշվում է dictionari-ի արժեքների գումարը
    a=0
    for i in d:
        a+=d[i]
    return a

d={29: 1023000, 98: 10075000, 70: 10056000, 4: 10076000, 23: 9970000, 71: 10232000, 6: 10008000, 93: 9928000, 63: 9936000,
 9: 9824000, 52: 9938000, 15: 9938000, 80: 9979000, 86: 10021000, 33: 10117000, 94: 10103000, 44: 9930000, 40: 10076000,
 39: 9986000, 18: 10119000, 32: 10087000, 36: 9981000, 85: 9894000, 30: 9975000, 25: 10066000, 79: 9958000, 83: 9952000,
 81: 10030000, 27: 9928000, 65: 10058000, 66: 9985000, 56: 10202000, 87: 9955000, 55: 9930000, 42: 9892000, 28: 99530000,
 17: 10106000, 99: 10177000, 49: 9844000, 13: 9938000, 21: 9983000, 11: 10011000, 50: 1002000, 57: 9959000, 67: 9970000,
 62: 10053000, 75: 10088000, 34: 10025000, 97: 10167000, 69: 10075000, 5: 9971000, 22: 9855000, 91: 9995000, 60: 9997000,
 59: 98780000, 43: 1002600, 46: 9911000, 92: 9882000, 31: 10056000, 48: 9898000, 16: 10172000, 54: 9961000, 96: 985200,
 77: 1014300, 37: 1001700, 53: 9857000, 45: 9961000, 72: 10103000, 26: 9784000, 38: 10033000, 3: 9900000, 95: 9996000,
 51: 10310000, 12: 985900, 73: 9967000, 61: 10025000, 35: 9965000, 84: 1008300, 64: 10014000, 2: 10191000, 100: 9703000,
 20: 9990000, 68: 9944000, 8: 9966000, 14: 9930000, 78: 9982000, 19: 982100, 88: 1003200, 58: 10117000, 82: 10010000,
 1: 1002700, 7: 990000, 76: 10088000, 24: 9915000, 74: 10056000, 89: 10166000, 41: 9926000, 10: 1002600, 90: 9968000,
 47: 9985000}
print("Numbers count is:  ", + gumar(d),end="\n")
print("numbers is: ",+ multi(d))
