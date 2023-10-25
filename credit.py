credit=""
card_type=""
while(len(credit)<16 or len(credit)>16):
    credit=input("Your card number")
odd_num =[credit[0],credit[2],credit[4],credit[6],credit[8],credit[10],credit[12],credit[14]]
even_num=[credit[1],credit[3],credit[5],credit[7],credit[9],credit[11],credit[13],credit[15]]

add=0
for i in range(len(odd_num)):
    num=0
    num=(int)(odd_num[i])
    num=num*2
    if(num>9):
        split_v1=int(str(num)[0])
        split_v2=int(str(num)[1])
        num=split_v1+split_v2
        add=add+num
    else:
        add+=num
for i in range(len(even_num)):
    num=0
    num=(int)(even_num[i])
    add=add+num
if(int(str(add)[1])==0):
    print("The card is legit")
if(credit[0]=='4'):
    card_type=card_type+"Visa"
elif(credit[0]+credit[1]=="34" or credit[0]+credit[1]=="37"):
    card_type=card_type+"American Express"
elif(credit[0]+credit[1]=="51" or credit[0]+credit[1]=="52" or credit[0]+credit[1]=="53" or credit[0]+credit[1]=="54" or credit[0]+credit[1]=="55"):
    card_type=card_type+"Master Card"
else:
    card_type=card_type+"unknown"
print(card_type)
