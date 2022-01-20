
"""


@author: Hsniddin Abdug`ofurov

"""

sevimli_taom = {'karim':'osh','salim':'tovuq sho\'rva','olim':'qozon kabob','asqar':'quymoq',\
                'muslim':'dimlama'}
print(f"Kariming sevimli taomi {sevimli_taom['karim']}")
print(f"Asqarning sevimli taomi {sevimli_taom['salim']}")
print(f"Olimning sevimli taomi {sevimli_taom['olim']}")


python_lug={'float':'o\'nli son','string':'matn','del':'ro\'yhatdan biror elementni olib tashlaydi',\
            'print':'kodni konsolga chiqaradi','f"':'malumotlarni konsolda chiqarishda yordam beradi',
            'tuple':"o'zgarmas ma'lumot turi",'list':'ro\'yhat','integer':'butun son'}

natija=python_lug.get(input('Kalit so\'z kiriting: '),'Bunday kalit so\'z mavjud emas!')
print(natija)
qidiruv=input('Kalit so\'z kiriting: ')
if qidiruv  in python_lug:
    print(python_lug[qidiruv])
else:
    print('Bunday kalit so\'z mavjud emas!')    