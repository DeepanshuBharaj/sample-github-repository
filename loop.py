#  loop statements
yes="yes"
no="no"
print("do you want to participate ??")
a=input("enter yes/no :- \n")
if a=='no':
  print("thanks for your response")
while a == 'yes':    

 x=int(input("enter a number from 1-10 \n"))

 if 0 < x <  11:
    print("number is in between the given instructions\n")
    break

 elif x <= 0 or x >= 11 :
    print("number given by the user is out of the given range ??????\n")
    break
 