yearStr=input("Enter a number")
year=int(yearStr)
#year=2016
'''rem=(year%4)

print("The rem is ")
print(rem)'''

if(year%4==0 and (year%100!=0 or year%400==0)):
       print("The year "+str(year)+" is a leap year")
else:
       print("The year "+str(year)+" is not a leap year")


