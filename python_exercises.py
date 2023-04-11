####Temel Python Alıştırmaları#####
#Görev 1
##Verilen değerlerin veri yapılarını inceleyiniz.

x = 8

type(x)

y = 3.2

type(y)

z = 8j + 18

type(z)

a = "Hello World"

type(a)

b = True

type(b)

c = 23 < 22

type(c)

l = [1, 2, 3, 4]

type(l)

d = {"Name": "Jake",
     "Age": 27,
     "Adress": "Downtown"}

type(d)

t = ("Machine Learning", "Data Science")

type(t)

s = {"Python", "Machine Learning", "Data Science"}

type(s)

#Görev 2
##Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. Virgül ve nokta yerine space koyunuz, kelime kelime ayırınız.

text = "The goal is to turn data into information, and information into insgiht."

text = text.upper()
text = text.replace(",", " ")
text = text.replace(".", " ")
list(text.split())

#Görev 3
##Adım 1: Verilen listenin eleman sayısına bakınız.
##Adım 2: Sıfırıncı ve onuncu indeksteki elemanları çağırınız.
##Adım 3: Verilen liste üzerinden ["D", "A", "T", "A"] listesi oluşturunuz. Adım 4: Sekizinci indeksteki elemanı siliniz.
##Adım 5: Yeni bir eleman ekleyiniz.
##Adım 6: Sekizinci indekse "N" elemanını tekrar ekleyiniz.

lst = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]

print(len(lst))

print(lst[0])

print(lst[10])

new = list(lst[0:4])
print(new)

lst.pop(8)

lst

lst.append("Q")

lst.insert(8, "N")

lst

#Görev 4
##Adım 1: Key değerlerine erişiniz.
##Adım 2: Value'lara erişiniz.
##Adım 3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.
##Adım 4: Key değeri Ahmet value değeri [Turkey,24] olan yeni bir değer ekleyiniz. Adım 5: Antonio'yu dictionary'den siliniz.

dict = {'Christian': ["America", 18],
        'Daisy': ["England", 12],
        'Antonio': ["Spain", 22],
        'Dante': ["Italy", 25]}

dict.keys()

dict.values()

dict["Daisy"][1] = 13

dict["Ahmet"] = ["Turkey", 24]

dict.pop("Antonio")

#Görev 5
##Argüman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atayan ve bu listeleri return eden fonksiyon yazınız.

l = [2, 113, 18, 93, 22]

def cano(liste):
    A = []
    B = []
    for i in liste:
        if i % 2 == 0:
            A.append(i)
        else:
            B.append(i)
    return A, B

cano(l)

#Görev 6
##Aşağıda verilen listede mühendislik ve tıp fakülterinde dereceye giren öğrencilerin isimleri bulunmaktadır. Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını temsil ederken son üç öğrenci de tıp fakültesi öğrenci sırasına aittir. Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdırınız.

ogrenciler = ["Ali", "Veli", "Ayşe", "Talat", "Zeynep", "Ece"]

for i, o in enumerate(ogrenciler):
        if i<3:
            i += 1
            print("Mühendislik Fakültesi",i,". öğrenci: ", o)
        else:
            i -= 2
            print("Tıp Fakültesi",i,". öğrenci: ", o)




#Görev 7
##Aşağıda 3 adet liste verilmiştir. Listelerde sırası ile bir dersin kodu, kredisi ve kontenjan bilgileri yer almaktadır. Zip kullanarak ders bilgilerini bastırınız.

ders_kodu = ["CMP1005", "PSY1001", "HUK1005", "SEN2204"]
kredi = [3, 4, 2, 4]
kontenjan = [30, 75, 150, 25]

for ders_kodu, kredi, kontenjan in zip(ders_kodu, kredi, kontenjan):
    print(f"Kredisi {kredi} olan {ders_kodu} kodlu dersin kontenjanı {kontenjan} kişidir.")


#Görev 8
##Aşağıda 2 adet set verilmiştir. Sizden istenilen eğer 1. küme 2. kümeyi kapsiyor ise ortak elemanlarını eğer kapsamıyor ise 2. kümenin 1. kümeden farkını yazdıracak fonksiyonu tanımlamanız beklenmektedir.

kume1 = set(["data", "ptyhon"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])

def ali(set1, set2):
    if set1.issuperset(set2):
        print(set1.intersection(set2))
    else:
        print(set2.difference(set1))

ali(kume1, kume2)
