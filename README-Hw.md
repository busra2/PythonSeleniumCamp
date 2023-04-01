# PyTest Decorator Ödevi 
```
@pytest.mark.skip
```
Bu dekoratör, test fonksiyonlarını atlamak için kullanılır. Bu, test senaryolarının bazı koşullar altında çalıştırılmamasını sağlar.

```
@pytest.mark.parametrize
```
Bağımsız değişkenlerin parametreleştirilmesini sağlar.

```
@pytest.mark.xfail
```
Bir testin özellikle başarısız olacağını bilerek kullanılır. Bu, bir testin hatalı sonuç vermesini bekleyen durumlarda kullanılır.
```
@pytest.mark.timeout
```
Belirli bir süre içinde tamamlanması gereken testler için kullanılır. Bu, test süresinin sınırlanması gerektiği durumlarda kullanılabilir.
```
@pytest.mark.dependency
```
Testler arasında bağımlılıklar tanımlamanıza olanak tanır. Bu, bir testin diğer bir testin başarılı bir şekilde çalışması için önce çalışması gerektiği durumlarda kullanılabilir.

```
@pytest.mark.skipif
````
Koşulumuz doğru ise fonksiyonu atlamamızı sağlar.

````
@pytest.exit
````
Test sürecinden çıkmamızı sağlar
