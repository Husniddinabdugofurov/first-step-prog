# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 07:47:32 2022

@author: lenovo
"""

#avtolar=['chevrolet','bmw','hyundai','bugatti','tesla']

#for avto in avtolar:
   
   # if avto == "bmw":
       # print(avto.upper())
   # else :
        # print(avto.title())
   
    
   
ism=input('Ismingizni kiriting: ')
if ism.lower()=="husniddin":
   print("Hush kelibsiz!", (ism.title()))
else:
   print('Uzr biz Husniddinni kutyapmiz!')
#
yosh=int(input('Tug`ilgan yilingizni kiriting: '))
if 2022-yosh>=18:
    print('Hush kelibsiz!')
else:
    print('Hali yosh bola ekansizku! Katta bo`lganingizda kelasiz!!!')
answer=int(input('5x5 nechaga teng: \n'))

if answer!=25:
    print('Sharmanda qildingiz odamni! Borib karrani yodlab keling ')
else:
    print('Javobingiz to`g`ri! Qoyil lekin! Bo`lajak matematik!!!')
t_yil=int(input('Tug`ilgan yilingizni kiriting: '))
if 18<=2022-t_yil<=30   :
   print('Siz ayni kuchga to`lgan yoshda ekansiz!' )
else:
    print(f"Hush kelibsiz qadrli {2022-t_yil} yosh do`stim! ")
x=int(input('x ga xohlagan qiymat bering: '))
y=int (input("y ga xohlagan qiymat berng: "))  
print('x>=y') if x>=y else print('x<y')
    

   


   
