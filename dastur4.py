# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 13:31:16 2022

@author: lenovo
"""

mahsulotlar=['guruch','un','shakar','tuxum','makka','non','ketchup','makaron','olma']
savat=[]
print('Sotib olmoqchi bo\'lgan 5 ta mahsulot nomini kiriting:')
for k in range(5):
    savat.append(input(f"{k+1} - mahsulot nomini kiriting>>> ").lower())
for n in savat:
   if n in mahsulotlar:
       print(f'{n} mahsuloti bizda bor')
   else:
       print(f"{n} mahsuloti bizda yo'q")
           
