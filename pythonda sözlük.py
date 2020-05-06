#key - value

##41 => kocaeli 35 => izmir

sehirler=['kocaeli','izmir']
plakalar=[41,35]
print(plakalar[sehirler.index('izmir')])
#print(plakalar['kocaeli])=>41
#prin(plakalalar['izmir])=>35
plakalar={'kocaeli':41,'izmir':35}

print(plakalar['kocaeli'])
print(plakalar['izmir'])

plakalar['ankara']=6
print(plakalar)
###örnek2
users={
      'sadikturan':{
          'age':36,
          'email':'sadik@gmail.com',
          'adres':'kocaeli',
          'phone':'12345'
          },
      'cinarturan':{
          'age':2,
          'phone':'1243214'
          
          }
}
print(users['cinarturan'])
print(users['cinarturan']['phone'])
###ornek3
fruits={'orange','apple','banana'}

for x in fruits:
    print(x)

fruits.add('cherry')#listeye ekleme
print(fruits)

myList = [1,2,5,4,4,2,1]
print(myList)
print(set(myList))



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

