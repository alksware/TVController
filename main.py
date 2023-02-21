import random
import msvcrt
import time as tm


class Kumanda():

    def __init__(self, tv_durum="Kapalı", tv_ses=0, kanal_listesi=["Trt"], kanal="Trt", dil_ayarı="Türkçe",altyazı_destegi=["Türkçe"]):
        print("Kumanda Oluşturuluyor...")

        self.tv_ses = tv_ses

        self.tv_durum = tv_durum

        self.kanal_listesi = kanal_listesi

        self.kanal = kanal

        self.dil_ayarı = dil_ayarı

        self.altyazı_destegi = altyazı_destegi

    def sesi_azalt_artir(self):

        while True:
            karakter = input("Azaltmak için '<' Artırmak İçin '>' Tamam ise 'q' ya basın")

            if (karakter == "<"):
                if (self.tv_ses != 0):
                    self.tv_ses -= 1
                    print("Ses:", self.tv_ses)
            elif (karakter == ">"):
                if (self.tv_ses != 32):
                    self.tv_ses += 1
                    print("Ses:", self.tv_ses)
            else:
                print("Ses Güncellendi:", self.tv_ses)
                break

    def tv_kapat(self):
        print("Tv kapatılıyor.")

        self.tv_durum = "Kapalı"

    def tv_aç(self):
        print("Tv Açılıyor.")
        self.tv_durum = "Açık"

    def __str__(self):
        return "Tv Durumu : {}\nSes: {}\nKanallar: {}\nŞu anki kanal: {}\n".format(self.tv_durum, self.tv_ses,
                                                                                   self.kanal_listesi, self.kanal)

    def __len__(self):
        return len(self.kanal_listesi)

    def rastgele_kanal(self):
        rastgele = random.randint(0, len(self.kanal_listesi) - 1)

        self.kanal = self.kanal_listesi[rastgele]

        print("Şu anki Kanal:", self.kanal)

    def kanal_ekle(self, kanal):
        print("Kanal Eklendi ", kanal)
        self.kanal_listesi.append(kanal)

    def dil_ayarı_degistir(self):
        secenek = input("Lütfen istediğiniz dili seçiniz:")
        self.dil_ayarı = secenek
        print("Lütfen bekleyiniz...")
        tm.sleep(1)
        print("Dil ayarı güncellendi:",secenek,"yeni dil olarak seçildi")

    def altyazı_secenegi_ekle(self):
        secenek = input("Lütfen eklemek istediğiniz altyazı dilini seçiniz:")
        print("Lütfen bekleyiniz... {}  indiriliyor...".format(secenek))
        tm.sleep(2)
        self.altyazı_destegi.append(secenek)
        print("{} varsayılan altyazı dillerine eklendi".format(secenek))

    def mevcut_dil_ayarlarını_goster(self):
        print("Bilgilere erişiliyor...")
        tm.sleep(2)
        print("Mevcut dil:",self.dil_ayarı)
        print("Mevcut altyazı seçenekleri:", self.altyazı_destegi)




kumanda = Kumanda()
print("""*******************

Televizyon Uygulaması

İşlemler ;

1. Televizyonu Aç

2. Televizyonu Kapat

3. Televizyon Bilgileri

4. Kanal Sayısını Öğrenme

5. Kanal Ekle

6. Rastgele Kanal'a Geç

7. Sesi Azalt Ya da Artır

8. Dil ayarı değiştir

9. Altyazı seçeneği ekle

10. Mevcut dil seçeneklerini öğrenme

Çıkmak için 'q' ya basın.
*******************""")

while True:

    işlem = input("İşlemi Seçiniz:")
    if (işlem == "q"):
        print("Programdan Çıkılıyor...")
        break
    if (işlem == "1"):
        kumanda.tv_aç()
    elif (işlem == "2"):
        kumanda.tv_kapat()
    elif (işlem == "3"):
        print(kumanda)
    elif (işlem == "4"):
        print("Kanal Sayısı: ", len(kumanda))
    elif (işlem == "5"):
        kanallar = input("Eklemek İstediğiniz Kanalları ',' ile ayırarak girin:")
        eklenecekler = kanallar.split(",")
        for i in eklenecekler:
            kumanda.kanal_ekle(i)
        print("Kanal Listesi Başarıyla Güncellendi.")
    elif (işlem == "6"):
        kumanda.rastgele_kanal()
    elif (işlem == "7"):
        kumanda.sesi_azalt_artir()
    elif (işlem == "8"):
        kumanda.dil_ayarı_degistir()
    elif (işlem == "9"):
        kumanda.altyazı_secenegi_ekle()
    elif (işlem == "10"):
        kumanda.mevcut_dil_ayarlarını_goster()
    else:
        print("Geçersiz İşlem...")











