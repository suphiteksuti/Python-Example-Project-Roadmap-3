class Ogrenci:
    ogrenciAdi = []
    ogrenciSoyadi = []
    ogrenciSınıfı = []

class Sorular:
    def __init__(self, dogru, yanlis):
        self.dogru = dogru
        self.yanlis = yanlis

    def netSayisi(self):
        self.net = float(self.dogru - (self.yanlis/4))
        return self.net

    def hesapla(self):
        puan = float(self.net*10)
        return puan

Ogrenci.ogrenciAdi = input("Adiniz :")
Ogrenci.ogrenciSoyadi = input("Soyadiniz :")
Ogrenci.ogrenciSınıfı = input("Snıfı :")
dogruSayisi = float(input("Dogru Sayisi :"))
yanlisSayisi = float(input("Yanlis Sayisi :"))
gonder = Sorular(dogruSayisi, yanlisSayisi)

print("--------------\n Adı: {} \n Soyadı: {} \n Sınıfı: {} \n Net: {} \n Puan: {}".format(Ogrenci.ogrenciAdi, Ogrenci.ogrenciSoyadi,
                                                                                           Ogrenci.ogrenciSınıfı, gonder.netSayisi(), gonder.hesapla()) )