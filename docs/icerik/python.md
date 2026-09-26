# Python

## 1. Python Nedir?

Python, okunabilirliği yüksek, genel amaçlı ve çok çeşitli alanlarda kullanılabilen bir programlama dilidir. İlk olarak Guido van Rossum tarafından geliştirilen Python, günümüzde web geliştirme, yapay zeka, makine öğrenmesi, veri bilimi, otomasyon, sistem yönetimi ve bilimsel hesaplama gibi birçok alanda kullanılmaktadır.

Python'ın en önemli özelliklerinden biri sade ve anlaşılır bir sözdizimine sahip olmasıdır. Python'da kod blokları süslü parantezlerle değil, girinti (indentation) kullanılarak belirlenir.

Basit bir Python programı:

```python
print("Merhaba Dünya!")
```

Python yorumlayıcısı bu kodu çalıştırdığında ekrana `Merhaba Dünya!` yazdırır.

Python'ın standart kütüphanesi oldukça geniştir ve dilin kendisiyle birlikte birçok hazır modül sunar. Ayrıca Python Package Index (PyPI) üzerinden çok sayıda üçüncü taraf paket kullanılabilir.

---

## 2. Python'ın Kullanım Alanları

Python çok amaçlı bir programlama dili olduğu için farklı yazılım alanlarında kullanılabilir.

Başlıca kullanım alanları şunlardır:

* Yapay zeka
* Makine öğrenmesi
* Veri bilimi
* Web geliştirme
* API geliştirme
* Otomasyon
* Sistem yönetimi
* Siber güvenlik
* Bilimsel hesaplama
* Veri analizi
* Web scraping
* Test otomasyonu
* Masaüstü uygulamaları

Örneğin yapay zeka alanında PyTorch, TensorFlow ve Scikit-learn gibi kütüphaneler kullanılabilir. Web geliştirmede Django, Flask ve FastAPI gibi framework'ler tercih edilebilir.

Python'ın geniş kullanım alanının önemli nedenlerinden biri, farklı alanlarda kullanılabilecek geniş bir kütüphane ve paket ekosistemine sahip olmasıdır.

---

## 3. Python Sözdizimi ve Girinti

Python'da kod blokları girinti kullanılarak belirlenir. Bu nedenle girinti Python programlarının çalışmasında önemli bir yere sahiptir.

Örneğin:

```python
yas = 20

if yas >= 18:
    print("Reşit")
```

Burada `print()` satırı `if` bloğunun içerisinde olduğu için girintilidir.

Python'da yaygın olarak dört boşluk kullanılır.

Yanlış girinti programın çalışmasını engelleyebilir:

```python
if yas >= 18:
print("Reşit")
```

Python'da yorum satırı oluşturmak için `#` kullanılır:

```python
# Bu bir yorum satırıdır
print("Merhaba")
```

---

## 4. Değişkenler ve Veri Tipleri

Python'da değişken oluşturmak için önceden veri tipinin belirtilmesi gerekmez.

```python
isim = "Ali"
yas = 21
ortalama = 85.5
ogrenci = True
```

Python bu değerlerin türlerini otomatik olarak belirler.

En temel Python veri tipleri şunlardır:

* `int`: Tam sayılar
* `float`: Ondalıklı sayılar
* `str`: Metin
* `bool`: `True` veya `False`
* `list`: Liste
* `tuple`: Tuple
* `set`: Küme
* `dict`: Sözlük
* `NoneType`: Değer bulunmadığını ifade eden `None`

Bir değişkenin türünü öğrenmek için `type()` kullanılabilir:

```python
sayi = 10

print(type(sayi))
```

Sonuç:

```text
<class 'int'>
```

Python dinamik tiplendirmeye sahip bir dildir. Bu nedenle değişken oluşturulurken veri tipi açıkça belirtilmek zorunda değildir.

---

## 5. Stringler

String, metinsel verileri ifade eder.

```python
isim = "Ali"
mesaj = "Merhaba Python"
```

Stringler tek veya çift tırnakla oluşturulabilir:

```python
isim = "Ali"
soyisim = 'Kodal'
```

Stringler üzerinde birçok işlem yapılabilir.

```python
metin = "Merhaba Python"

print(metin.upper())
print(metin.lower())
print(len(metin))
```

String içerisindeki karakterlere indeks kullanılarak erişilebilir:

```python
metin = "Python"

print(metin[0])
```

Sonuç:

```text
P
```

Python'da indeksler `0` değerinden başlar.

String içerisinde değişken kullanmak için f-string kullanılabilir:

```python
isim = "Ali"
yas = 21

print(f"Benim adım {isim}, yaşım {yas}.")
```

---

## 6. Operatörler

Python'da matematiksel işlemler için aritmetik operatörler kullanılır.

```text
+   Toplama
-   Çıkarma
*   Çarpma
/   Bölme
//  Tam sayı bölmesi
%   Mod alma
**  Üs alma
```

Örnek:

```python
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
```

Karşılaştırma operatörleri iki değeri karşılaştırır ve `True` veya `False` sonucu üretir.

```text
==   Eşit
!=   Eşit değil
>    Büyük
<    Küçük
>=   Büyük veya eşit
<=   Küçük veya eşit
```

Mantıksal işlemler için `and`, `or` ve `not` kullanılır.

```python
yas = 21
ogrenci = True

if yas >= 18 and ogrenci:
    print("Koşullar sağlandı")
```

---

## 7. Koşullu İfadeler

Python'da programın belirli koşullara göre farklı işlemler yapmasını sağlamak için `if`, `elif` ve `else` kullanılır.

```python
yas = 20

if yas >= 18:
    print("Reşit")
else:
    print("Reşit değil")
```

Birden fazla koşul için `elif` kullanılabilir:

```python
notu = 75

if notu >= 90:
    print("AA")
elif notu >= 80:
    print("BA")
elif notu >= 70:
    print("BB")
else:
    print("Başarısız")
```

Koşullu ifadeler kullanıcı girişi, veri kontrolü, yetkilendirme ve program akışının belirlenmesi gibi birçok durumda kullanılır.

---

## 8. Döngüler

Python'da tekrar eden işlemleri gerçekleştirmek için döngüler kullanılır.

En temel döngüler `for` ve `while` döngüleridir.

`for` döngüsü bir koleksiyon veya belirli bir aralık üzerinde dolaşmak için kullanılabilir:

```python
for i in range(5):
    print(i)
```

Bu kod `0` ile `4` arasındaki değerleri yazdırır.

`while` döngüsü ise belirli bir koşul doğru olduğu sürece çalışır:

```python
sayac = 0

while sayac < 5:
    print(sayac)
    sayac += 1
```

Döngüyü tamamen sonlandırmak için `break`, mevcut iterasyonu atlamak için `continue` kullanılabilir.

---

## 9. Listeler

Liste (`list`), birden fazla veriyi sıralı şekilde saklamak için kullanılan değiştirilebilir bir veri yapısıdır.

```python
meyveler = ["elma", "armut", "muz"]
```

Elemanlara indeks üzerinden erişilebilir:

```python
print(meyveler[0])
```

Listeye eleman eklemek:

```python
meyveler.append("çilek")
```

Eleman silmek:

```python
meyveler.remove("armut")
```

Listeyi sıralamak:

```python
meyveler.sort()
```

Listeler iç içe de kullanılabilir:

```python
ogrenciler = [
    ["Ali", 21],
    ["Ayşe", 22],
    ["Mehmet", 20]
]
```

Listeler Python programlarında en sık kullanılan veri yapılarından biridir.

---

## 10. Tuple, Set ve Dictionary

Python'da listelerin dışında farklı amaçlara hizmet eden veri yapıları da bulunur.

### Tuple

Tuple, sıralı fakat değiştirilemez bir veri yapısıdır.

```python
koordinat = (10, 20)
```

### Set

Set, benzersiz değerleri saklamak için kullanılır.

```python
sayilar = {1, 2, 3, 3, 4}
```

Tekrarlanan değerler yalnızca bir kez tutulur.

### Dictionary

Dictionary, anahtar-değer (`key-value`) yapısıyla veri saklar.

```python
ogrenci = {
    "isim": "Ali",
    "yas": 21,
    "bolum": "Bilgisayar Mühendisliği"
}
```

Değere erişmek:

```python
print(ogrenci["isim"])
```

Dictionary yapısı özellikle JSON verileri, kullanıcı bilgileri, yapılandırma bilgileri ve API cevaplarıyla çalışırken sık kullanılır. Python dokümantasyonu listeler, tuple'lar, setler ve dictionary'leri temel veri yapıları arasında ele almaktadır.

---

## 11. Fonksiyonlar

Fonksiyonlar belirli bir işlemi gerçekleştiren ve gerektiğinde tekrar çağrılabilen kod bloklarıdır.

Fonksiyon tanımlamak için `def` kullanılır.

```python
def selamla():
    print("Merhaba")
```

Fonksiyon çağrıldığında:

```python
selamla()
```

Parametre kullanılabilir:

```python
def selamla(isim):
    print(f"Merhaba {isim}")

selamla("Ali")
```

Fonksiyonlar değer döndürebilir:

```python
def topla(a, b):
    return a + b

sonuc = topla(10, 20)

print(sonuc)
```

`return`, hesaplanan değeri fonksiyonun dışına aktarır.

Python fonksiyonlarında varsayılan parametreler, keyword argument'ler, değişken sayıda argümanlar, lambda ifadeleri ve type annotation gibi özellikler de kullanılabilir.

---

## 12. List Comprehension

List comprehension, bir listenin kısa ve okunabilir biçimde oluşturulmasını sağlayan Python özelliğidir.

Örneğin:

```python
sayilar = [1, 2, 3, 4, 5]

kareler = [sayi ** 2 for sayi in sayilar]

print(kareler)
```

Sonuç:

```text
[1, 4, 9, 16, 25]
```

Koşul da eklenebilir:

```python
cift_sayilar = [sayi for sayi in range(10) if sayi % 2 == 0]
```

List comprehension özellikle bir listenin elemanlarını dönüştürmek veya filtrelemek için kullanılır. Python resmi öğreticisinde list comprehension ayrı bir veri yapısı tekniği olarak ele alınmaktadır.

---

## 13. Modüller ve import

Python kodlarını farklı dosyalara ayırmak için modüller kullanılabilir.

Örneğin `hesaplama.py` isimli dosyada:

```python
def topla(a, b):
    return a + b
```

bulunduğunu düşünelim.

Başka bir dosyada bu fonksiyon şu şekilde kullanılabilir:

```python
import hesaplama

sonuc = hesaplama.topla(10, 20)

print(sonuc)
```

Belirli bir fonksiyonu doğrudan almak da mümkündür:

```python
from hesaplama import topla
```

Modüler yapı büyük projelerde kodun daha düzenli, okunabilir ve tekrar kullanılabilir olmasını sağlar. Python'da modüller ve paketler standart programlama yapısının önemli parçalarıdır.

---

## 14. Python Paketleri ve pip

Python'ın standart kütüphanesinin dışında üçüncü taraf paketler de kullanılabilir.

Paketleri kurmak için yaygın olarak `pip` kullanılır.

Örneğin:

```bash
pip install requests
```

Kurulan paket Python içerisinde kullanılabilir:

```python
import requests
```

Kurulu paketleri listelemek için:

```bash
pip list
```

Bir paketi kaldırmak için:

```bash
pip uninstall requests
```

Bir projenin bağımlılıklarını `requirements.txt` dosyasında tutmak yaygın bir yöntemdir:

```text
requests
numpy
pandas
```

Daha sonra:

```bash
pip install -r requirements.txt
```

komutuyla paketler kurulabilir.

Python'ın resmi dokümantasyonunda sanal ortamlar ve `pip` paket yönetimi ayrı bir konu olarak ele alınmaktadır.

---

## 15. Virtual Environment

Virtual environment, Python projeleri için izole çalışma ortamı oluşturur.

Bir projede kullanılan paketlerin başka projeleri etkilemesini önlemek için sanal ortam kullanılabilir.

Oluşturmak için:

```bash
python -m venv venv
```

Windows'ta etkinleştirmek için:

```bash
venv\Scripts\activate
```

Linux veya macOS'ta:

```bash
source venv/bin/activate
```

Sanal ortam aktifken yüklenen Python paketleri ilgili ortam içerisinde bulunur.

Bu yapı özellikle farklı projelerin farklı paket veya paket sürümlerine ihtiyaç duyduğu durumlarda önemlidir.

---

## 16. Hata Yönetimi ve Exception

Python'da program çalışırken çeşitli hatalar meydana gelebilir. Python'da çalışma sırasında meydana gelen bu durumlar exception olarak adlandırılır.

Örneğin:

```python
sayi = int("abc")
```

işlemi `ValueError` oluşturabilir.

Hataları kontrol etmek için `try` ve `except` kullanılabilir:

```python
try:
    sayi = int(input("Bir sayı girin: "))
    print(sayi)
except ValueError:
    print("Geçerli bir sayı girilmedi.")
```

Yaygın exception türlerinden bazıları:

* `ValueError`
* `TypeError`
* `NameError`
* `IndexError`
* `KeyError`
* `FileNotFoundError`
* `ZeroDivisionError`

Python'da syntax hataları ile çalışma sırasında oluşan exception'lar farklı kavramlardır. Exception'lar uygun şekilde `try-except` yapılarıyla ele alınabilir.

---

## 17. Dosya İşlemleri

Python ile dosya oluşturma, okuma ve yazma işlemleri yapılabilir.

Dosya okumak:

```python
with open("veri.txt", "r", encoding="utf-8") as dosya:
    veri = dosya.read()

print(veri)
```

Dosyaya yazmak:

```python
with open("veri.txt", "w", encoding="utf-8") as dosya:
    dosya.write("Merhaba Python")
```

Yaygın dosya açma modları:

```text
r   Okuma
w   Yazma
a   Sona ekleme
b   Binary veri
```

`with` yapısının kullanılması, dosya gibi kaynakların işlem tamamlandıktan sonra uygun şekilde kapatılmasını kolaylaştırır. Python resmi öğreticisinde dosya okuma ve yazma işlemleri standart giriş/çıkış konuları içerisinde açıklanmaktadır.

---

## 18. JSON ile Çalışmak

JSON, uygulamalar arasında yapılandırılmış veri alışverişinde yaygın olarak kullanılan bir veri formatıdır.

Örnek JSON:

```json
{
    "isim": "Ali",
    "yas": 21,
    "ogrenci": true
}
```

Python'da JSON işlemleri için `json` modülü kullanılabilir.

```python
import json

veri = {
    "isim": "Ali",
    "yas": 21
}

json_verisi = json.dumps(veri)

print(json_verisi)
```

JSON dosyasından veri okumak:

```python
with open("veri.json", "r", encoding="utf-8") as dosya:
    veri = json.load(dosya)
```

JSON özellikle web API'leri, konfigürasyon dosyaları ve uygulamalar arası veri aktarımında sık kullanılır.

---

## 19. Nesne Yönelimli Programlama

Python, Nesne Yönelimli Programlama yani Object-Oriented Programming (OOP) yaklaşımını destekler.

OOP'de temel kavramlar:

* Class
* Object
* Attribute
* Method
* Inheritance
* Encapsulation
* Polymorphism

Basit bir sınıf:

```python
class Araba:
    def __init__(self, marka):
        self.marka = marka

    def bilgi_ver(self):
        print(f"Araba markası: {self.marka}")
```

Nesne oluşturmak:

```python
araba = Araba("Toyota")

araba.bilgi_ver()
```

Burada `Araba` bir class, `araba` ise bu class'tan oluşturulmuş bir object'tir.

Python resmi öğreticisi sınıflar, nesneler, sınıf değişkenleri, kalıtım, iterator ve generator gibi konuları OOP kapsamında ele almaktadır.

---

## 20. Kalıtım ve Polymorphism

Kalıtım yani inheritance, bir sınıfın başka bir sınıfın özelliklerini ve davranışlarını kullanabilmesini sağlar.

```python
class Hayvan:
    def ses_cikar(self):
        print("Hayvan sesi")


class Kedi(Hayvan):
    def ses_cikar(self):
        print("Miyav")
```

Burada `Kedi`, `Hayvan` sınıfından kalıtım almıştır.

`Kedi` sınıfı üst sınıftaki `ses_cikar()` metodunu kendi davranışına göre yeniden tanımlamıştır.

Bu işlem method overriding olarak adlandırılır.

Polymorphism ise farklı nesnelerin aynı metot çağrısına farklı davranışlarla cevap verebilmesini ifade eder.

```python
hayvanlar = [Kedi(), Hayvan()]

for hayvan in hayvanlar:
    hayvan.ses_cikar()
```

Kalıtım ve polymorphism, büyük ve karmaşık Python uygulamalarında kodun organize edilmesine yardımcı olabilir.

---

## 21. Scope ve Namespace

Python'da bir değişkenin erişilebilir olduğu alan scope olarak adlandırılır.

Örneğin bir fonksiyon içerisinde oluşturulan değişken genellikle local scope'a aittir:

```python
def test():
    isim = "Ali"
    print(isim)
```

Fonksiyon dışındaki bir değişken global scope içerisinde bulunabilir:

```python
isim = "Ali"

def test():
    print(isim)
```

Python'da isim arama mekanizması genellikle LEGB sırasıyla açıklanır:

```text
Local
Enclosing
Global
Built-in
```

Scope ve namespace kavramları özellikle büyük programlarda değişkenlerin nereden erişilebildiğini anlamak açısından önemlidir.

---

## 22. Iterator ve Generator

Iterator, bir koleksiyon içerisindeki elemanların sırayla alınmasını sağlayan nesnedir.

Örneğin:

```python
sayilar = [1, 2, 3]

iterator = iter(sayilar)

print(next(iterator))
print(next(iterator))
```

Generator ise değerleri ihtiyaç oldukça üretebilen özel bir yapıdır.

Generator oluşturmak için `yield` kullanılabilir:

```python
def sayilar():
    for i in range(5):
        yield i
```

Kullanımı:

```python
for sayi in sayilar():
    print(sayi)
```

Generator'lar özellikle çok miktarda verinin işlendiği durumlarda bütün sonuçların aynı anda bellekte tutulmasını önleyerek daha verimli bir çalışma modeli sağlayabilir. Python resmi öğreticisi iterator ve generator konularını sınıflar bölümünde ayrıca ele almaktadır.

---

## 23. Decorator

Decorator, bir fonksiyonun davranışını değiştirmek veya fonksiyona ek özellik kazandırmak için kullanılan Python yapısıdır.

Basit bir örnek:

```python
def logla(func):
    def wrapper():
        print("Fonksiyon çalışıyor")
        func()

    return wrapper
```

Decorator şu şekilde kullanılabilir:

```python
@logla
def merhaba():
    print("Merhaba")
```

Decorator'lar web framework'lerinde, logging işlemlerinde, yetkilendirmede, cache mekanizmalarında ve çeşitli yazılım tasarım ihtiyaçlarında kullanılabilir.

Örneğin Flask'taki route tanımlamaları decorator kullanımına örnektir:

```python
@app.route("/")
def home():
    return "Merhaba"
```

---

## 24. Type Hinting

Python dinamik tiplendirmeye sahip olsa da fonksiyon ve değişkenlerde beklenen veri tiplerini belirtmek için type hint kullanılabilir.

Örnek:

```python
def topla(a: int, b: int) -> int:
    return a + b
```

Burada:

* `a: int` → `a` için beklenen veri tipi
* `b: int` → `b` için beklenen veri tipi
* `-> int` → fonksiyonun döndürmesi beklenen tip

Type hint'ler Python'un çalışma zamanında otomatik olarak zorunlu tip kontrolü yaptığı anlamına gelmez. Daha çok kodun okunabilirliği, IDE desteği ve statik analiz araçları açısından kullanılır.

---

## 25. Python ile Web Geliştirme

Python web uygulamaları ve API'ler geliştirmek için kullanılabilir.

Yaygın Python web framework'leri arasında:

* Django
* Flask
* FastAPI

bulunur.

Django daha kapsamlı web uygulamaları geliştirmek için kullanılabilen bir framework'tür.

Flask daha hafif ve esnek bir web framework'üdür.

FastAPI ise özellikle modern API geliştirme ve type hint kullanımı açısından öne çıkan bir framework'tür.

Basit bir Flask örneği:

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Merhaba Dünya"

app.run()
```

Python web uygulamalarında veritabanı, authentication, API, frontend ve backend gibi farklı bileşenlerle birlikte kullanılabilir.

---

## 26. Python ile Veritabanı İşlemleri

Python birçok farklı veritabanı sistemiyle birlikte kullanılabilir.

Örneğin:

* SQLite
* MySQL
* PostgreSQL
* Microsoft SQL Server
* MongoDB

SQLite Python ile birlikte gelen `sqlite3` modülüyle kullanılabilir.

```python
import sqlite3

baglanti = sqlite3.connect("database.db")

cursor = baglanti.cursor()

cursor.execute(
    "CREATE TABLE IF NOT EXISTS users (id INTEGER, name TEXT)"
)

baglanti.commit()
baglanti.close()
```

Gerçek uygulamalarda veritabanı işlemleri için uygun kütüphaneler, ORM araçları veya database driver'ları kullanılabilir.

Kullanıcı girdilerinin SQL sorgularına doğrudan string birleştirme yöntemiyle eklenmesi güvenlik açısından sakıncalıdır. Parametreli sorgular tercih edilmelidir.

---

## 27. Python ile Yapay Zeka ve Veri Bilimi

Python, yapay zeka ve veri bilimi alanlarında yaygın olarak kullanılmaktadır.

Bu alanda kullanılan önemli kütüphanelerden bazıları:

* NumPy
* Pandas
* Scikit-learn
* PyTorch
* TensorFlow
* Matplotlib

NumPy, sayısal hesaplama ve dizi işlemleri için kullanılır.

Pandas, tablo şeklindeki verilerin işlenmesi ve analiz edilmesini kolaylaştırır.

Scikit-learn, klasik makine öğrenmesi algoritmalarının uygulanmasında kullanılır.

PyTorch ve TensorFlow ise özellikle derin öğrenme ve yapay sinir ağı modellerinin geliştirilmesinde kullanılabilir.

Python'ın yapay zeka alanında yaygın olmasının önemli nedenlerinden biri, bu alanlara yönelik geniş kütüphane ve araç ekosistemidir.

---

## 28. Python ile Otomasyon ve Sistem İşlemleri

Python, tekrar eden işlemleri otomatikleştirmek için kullanılabilir.

Örneğin:

* Dosya oluşturma
* Dosya taşıma
* Dosya isimlerini değiştirme
* Klasör oluşturma
* Log dosyalarını analiz etme
* API çağrıları yapma
* Sistem bilgilerini alma
* Rapor oluşturma
* Web otomasyonu
* Sunucu yönetimi

gibi işlemler Python ile otomatikleştirilebilir.

Örneğin `pathlib` ile dosya ve klasör işlemleri yapılabilir:

```python
from pathlib import Path

klasor = Path("raporlar")

klasor.mkdir(exist_ok=True)
```

İşletim sistemiyle ilgili işlemler için `os` ve `subprocess` gibi modüller de kullanılabilir.

Python'ın standart kütüphanesi işletim sistemi arayüzleri, dosya işlemleri, internet erişimi, tarih-saat işlemleri, logging ve benzeri birçok alanda hazır modüller sunmaktadır.

---

## 29. Python'da Async, Threading ve Multiprocessing

Python farklı eşzamanlılık ve paralellik yaklaşımlarını destekler.

`async` ve `await`, özellikle I/O ağırlıklı işlemlerde asenkron programlama için kullanılır.

```python
import asyncio

async def merhaba():
    print("Merhaba")

asyncio.run(merhaba())
```

`threading`, birden fazla thread ile çalışmayı sağlar ve özellikle I/O ağırlıklı işlemlerde kullanılabilir.

`multiprocessing` ise ayrı process'ler oluşturarak özellikle CPU ağırlıklı işlemlerde kullanılabilir.

Bu üç yaklaşım birbirinin tamamen alternatifi değildir. Uygulamanın yaptığı işlemin CPU ağırlıklı mı yoksa I/O ağırlıklı mı olduğuna göre uygun yöntem seçilir.

Python standart kütüphanesinde çoklu iş parçacığı ve benzeri programlama araçları da bulunmaktadır.

---

## 30. Python'da İyi Kodlama ve Proje Geliştirme

Python'da sadece çalışan kod yazmak değil, okunabilir, sürdürülebilir ve güvenli kod yazmak da önemlidir.

İyi bir Python projesinde:

* Anlamlı değişken isimleri kullanılmalıdır.
* Fonksiyonlar mümkün olduğunca belirli görevlerden sorumlu olmalıdır.
* Kod tekrarından kaçınılmalıdır.
* Hatalar uygun şekilde yönetilmelidir.
* Hassas bilgiler kaynak koduna yazılmamalıdır.
* Gerekli bağımlılıklar belirtilmelidir.
* Sanal ortam kullanılmalıdır.
* Kod sürüm kontrolü altında tutulmalıdır.
* Testler yazılmalıdır.
* Proje yapısı düzenli tutulmalıdır.
* Gereksiz karmaşıklıktan kaçınılmalıdır.

Örnek olarak:

```python
def hesapla_toplam(fiyat, miktar):
    return fiyat * miktar
```

gibi açık ve anlaşılır bir fonksiyon, ne yaptığı belli olmayan uzun ve karmaşık kodlara göre daha kolay okunabilir.

Python ekosisteminde kodlama stili ve okunabilirlik önemli bir yere sahiptir. Python resmi dokümantasyonu da fonksiyonlar ve veri yapılarının yanında kodlama stiline ayrı bir bölüm ayırmaktadır.

Python öğrenirken temel sözdiziminden başlayarak değişkenler, veri tipleri, koşullar, döngüler, veri yapıları, fonksiyonlar, modüller, hata yönetimi ve sınıflar öğrenilebilir. Daha sonra Python'ın kullanım amacına göre web geliştirme, yapay zeka, veri bilimi, otomasyon veya sistem yönetimi gibi alanlara geçilebilir.
