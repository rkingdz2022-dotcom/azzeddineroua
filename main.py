a=int(input("veuiller saisir la valeur de a  :"))
b=int(input("veuiller saisir la valeur de b  :"))
if a>b:
    min=a
else:
    min=a
for i in range(1, min+1) :
    if a%i ==0 and b%i == 0:
        PGCD=i
print("le PGCD  de ",a,"est de  ",b,"est  :",PGCD)
