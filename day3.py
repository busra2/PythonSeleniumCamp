class Human:
    #name = "büşra"
    def __init__(self,name):
       # self.name=name diyemem not defined 
       self.name = name
    def talk(self,sentence):
        print(f"{self.name}: {sentence}")
    def walk (self):
        print(f"{self.name} is walking")

# instance => örnek
human1 = Human("büş")
#human1.name="esma"
human1.talk("Merhaba")
human1.walk()
print(human1)

human2 = Human("halit")
#human2.name="Esma"
human2.talk("Selam")
human2.walk()

#selenium import etmek için 
#pip install selenium

import selenium
# selenium inmesine rağmen hata alıyordum. Default python uzantısını değiştirerek çözüldü sorun.



