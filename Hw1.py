''''
int = hold signed integers of non-limited length
float =  holds floating decimal points and it's accurate up to 15 decimal places.
string = holds sequence of characters
List =  holds collection of items
Bool = hols true or false '''

#Kodlama.io sitesinde değişken olarak kullanıldığını düşündüğünüz verileri, veri tipleriyle örneklendiriniz
yüzde=25 #int
yüzde=25.0 #float
tarih = "1.Gün - 8 Mart 2023" #string
kategori=["Tümü,Programlama(7)"]#List
tıklama=1 #bool

#kodlama.io sitesinde şart blokları kullanıldığını düşündüğünüz kısımları örneklendiriniz.
#if-else kullanarak hesaba giriş örneği
Email=input("Email")
Password=int(input("Password"))
if Email==("123@gmail.com") and Password==123:
    print("İşlem başarılı")
elif Email==("") & Password==(""):
    print("Lütfen tekrar deneyiniz")
else:
    print("Email veya Şifreniz hatalı,Lütfen tekrar deneyiniz!")

