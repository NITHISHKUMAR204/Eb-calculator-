
num=int(input("Enter a Unit :"))
price=0
if num<=100:
    price+=0
elif num<=200:
    num=num-100
    price=(100*0+num*2.35)
elif num<=400:
    num=num-200
    price=(100*0+100*2.35+num*4.7) 
elif num<=500:
     num=num-400
     price=(100*0+100*2.34+200*4.7+num*6.3)
else:
    num=num-500;
    price=(100*0+100*2.34+200*4.7+100*6.3+num*8.4)


print("if input unit is " +str(num)+ " then amount is Rs: "+str(price))


