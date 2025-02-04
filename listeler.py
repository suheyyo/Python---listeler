#count 
liste = [2, 7, 45, 3, 7, 2, 45, 7, 34, 3]
print("listedeki 7 rakamnının tekrar sayısı", liste.count(7))
#len
list = ["selam", "naber", "nasılsın", "iyi misin"]
print("listedeki eleman sayısı", len(list))
#index
liste = [2, 7, 45, 3, 7, 2, 45, 7, 34, 3]
print("listedeki sayının numarası", liste.index(7))
#sayı birden fazla yerde ise en baştakini yazdırır.
#listeler içerisinde her veri türünden barındırabilir.
yeniliste = ["ali yılmaz", "55443322", True]
#listeler list() şeklinde de yazılabilir.
#listedeki verilen sayıdaki elemanı bulma
liste = [2, 7, 45, 3, 7, 2, 45, 7, 34, 3]
print(liste[1])
#başlangıç-bitiş bulma
liste = [2, 7, 45, 3, 7, 2, 45, 7, 34, 3]
print(liste[:3])
print(liste[2:6])
rakamlar = [0, 1, 2, 3, 4, 5, 6, 7 ,8, 9, 10, 11, 12]
print(rakamlar[1:11:2])
#atlama parametresi
rakamlar = [0, 1, 2, 3, 4, 5, 6, 7 ,8, 9, 10, 11, 12]
print(rakamlar[::4])
#if ile sorgulama yapma
rakamlar = [0, 1, 2, 3, 4, 5, 6, 7 ,8, 9, 10, 11, 12]
if 14 in rakamlar:
    print("yazılan sayı, verilen listeye dahildir.")
else:
    print("yazılan sayı, verilen listeye dahil değildir.")
#listedeki verileri değiştirmek
rakamlar = [0, 1, 2, 3, 4, 5, 6, 7 ,8, 9, 10, 11, 12]
print(rakamlar)
rakamlar[2] = 19
print(rakamlar)
#toplu veri değiştirme (listeye liste eklemek)
rakamlar = [0, 1, 2, 3, 4, 5, 6, 7 ,8, 9, 10, 11, 12]
rakamlar[-1] = [23, 24, 25]
print(rakamlar)
print(rakamlar[-1])
#listede mesela 7 veri mevcut gibi görünüyorsa ancak liste boyuna baktığımızda 6 veriyor ise listenin son verisinin de bir liste olarak sayılmasından kaynaklanır.
#eğer sonda tekrardan yeni listeyi yazmak istemiyorsan print(rakamlar[-1]) yazabilirsin.
rakamlar = [0, 1, 2, 3, 4, 5, 6, 7 ,8, 9, 10, 11, 12]
rakamlar[-1] = [23, 24, 25]
print(rakamlar)
#listeye yeni bir veri eklemek için append() kullanılır. en sona veriyi ekler.
rakamlar = [0, 1, 2, 3, 4, 5, 6, 7 ,8, 9, 10, 11, 12]
rakamlar.append(23)
print(rakamlar)
#index
rakamlar = [0, 1, 2, 3, 4, 5, 6, 7 ,8, 9, 10, 11, 12]
rakamlar.index(7)
print(rakamlar)
#veri silme (direkt verinin kendisini silmek için remove, dsıra numarasıyla silmek için de pop veya delete(del) fonksiyonuyla da silebilirsin.)
rakamlar = [0, 1, 2, 3, 4, 5, 6, 7 ,8, 9, 10, 11, 12]
rakamlar.remove(7)
print(rakamlar)
#pop
rakamlar = [0, 1, 2, 3, 4, 5, 6, 7 ,8, 9, 10, 11, 12]
rakamlar.pop(5)
print(rakamlar)
#clear
fruits = ['apple', 'banana', 'cherry', 'orange']
fruits.clear()
#del direkt listeyi siler, clear ise içeriği siler.
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
#while döngüsü
rakamlar = [0, 1, 2, 3, 4, 5, 6, 7 ,8, 9, 10, 11, 12]
veriboyu = len(rakamlar)
x = 0
while x < veriboyu:
    print(x, ":", rakamlar[x])
    x += 1
#listeleri sıralamak sort() kullanmak
rakamlar = [0, 1, 2, 3, 4, 5, 6, 7 ,8, 9, 10, 11, 12]
rakamlar.sort()
print(rakamlar)
#reverse kullanarak sıralamak
rakamlar = [0, 1, 2, 3, 4, 5, 6, 7 ,8, 9, 10, 11, 12]
print(rakamlar)
rakamlar.reverse()
print(rakamlar)
rakamlar = [0, 1, 2, 3, 4, 5, 6, 7 ,8, 9, 10, 11, 12]
rakamlar.sort()
rakamlar.reverse()
print(rakamlar)
#reverse, tersten çevirerek yazmak demektir. bu şekilde sıralama terse döner.
#listeleri kopyalamak, referans vererek liste1=liste2 şekline kopyalamak mümkün değildir, çünkü bu şekilde birinde yapılan değişiklik diğerine de yansıyacaktır.
#bu iki liste aslında birbirinin kopyası değil, aynısıdır. bir listenin bağımsız bir kopyasını oluşturmak için copy() methodundan faydalanılabilir.
#pythonda birden fazla listenin verilerini birleştirmek için birden çok method bulunur, örneğin veri birleştirmek için + methodunu kullanabiliriz.
#eğer, iki listenin verilerini birleştiren üçüncü bir liste oluşturulmak istenmiyor, sadece bir listeye diğer listenin verileri eklenmek isteniyorsa extend() methodu kullanılabilir.
projeler1 = ["proje1", "proje2", "proje3"]
projeler2 = ["design1", "design2"] 
projeler1.extend(projeler2)
print(projeler1)
#liste üreteçleri, varolan bir listenin verileriyle yeni bir liste oluşturulmak istendiğinde kısa bir kod yazım tekniği sunar. standart olarak bir listenin verilerinden başka liste oluşturulmak istenirse.
yeniliste = []
for x in liste: 
    yeniliste.append(x)
    #şeklinde kodlanabilir. liste üreteçleriyle;
    
    yeniliste = [x in liste]