list1=['one','two','there']
list2=['four','five','six']

numbers=list1+list2
print(numbers)

print(len(numbers))

print(numbers[3])

userA=['sadık',36]
userB=['çınar',2]
users=userA+userB

print(userA)
print(userB)
print(users)
########
##1- bmw,mercedes,opel,mazda liste oluştur
arabalar=['bmw','mercedes','opel','mazda']
##2-liste kac elemanlıdır?
result=len(arabalar)
##3-listenin ilk ve son elemanı nedir?
result=arabalar[0]
result=arabalar[3]
result=arabalar[-1]
##4-mercedes listenin bir elemanı mıdır?
result='mercedes' in arabalar
##5-listenin ilk 3 elemanı alın
result=arabalar[0:3]
#6-liste elemanlarını tersten yazdırınız
result=arabalar[:,:,-1]
#####
numbers=[1,10,5,16,4,9,10]
letters=['a','s','g','b']
val=min(numbers)
val=max(numbers)
val=max(letters)
val=min(letters)

val=numbers[3:6]
val=numbers[:3]
val=numbers[4:]

numbers[4]=40

numbers.append(49)#index ekleme
numbers.insert(3,78)


numbers.pop(0)#index silme
numbers.remove(49)

numbers.sort()
letters.sort()

numbers.reverse()

print(numbers)
print(letters)

print(len(numbers))
print(len(letters))

print(numbers.count(10))#kac tane 10 var
print(letters.count('a'))#kac tane a var

#uygulamalar
names=['ali','yagmur','hakan','deniz']
years=[1998,2000,1998,1987]
#1"cenk ismini listenin sonuna ekleyiniz.
names.append('cenk')
#2 "sena ismini listenin başına ekleyiniz
names.insert(0, 'sena')
#3 deniz ismini listeden siliniz
names.remove('deniz')
#4 deniz isminin indexi nedir
index=names.index('deniz')
#5 ali listenin bir elamanı mıdır
result='ali' in names
#6liste elemanlarını ters çevirin
names.reverse()
#7 liste elemanlarını alfabetik sırala
names.sort()
#8 years listesinin rakamsal büyüklük sırala
years.sort()
#9 years dizisinin en büyük ve en küçük elemanı nedir
min=min(years)
max=max(years)
#10 kac tane 1998 degerı war 
result=years.count(1998)
#11 years dizisinin tüm elemanlarını silin
years.clear
#12 kullanıcıdan aldıgınız 3 tane marka ismini liste şeklınde saklayınız

markalar=[]
marka=input("marka: ")
markalar.append(marka)


print(markalar)
####TUPLE LİSTE####
list=[1,2,3]
tuple=(1,'iki',3)
print(type(list))
print(type(tuple))

print(list[2])
print(tuple[2])

list=['ali','veli']
tuple=('damlar','ayşe')

list[0]='ahmet'
tuple[0]='deniz'

print(list)
print(tuple)































