# Banka Hesabı (Encapsulation, Inheritance)
class Hesap:
    def __init__(self, sahip_adi, hesap_numarasi, bakiye=0):
        self.sahip_adi = sahip_adi
        self.hesap_numarasi = hesap_numarasi
        self.__bakiye = bakiye  # private
        
    def para_yatir(self, miktar):
        if miktar > 0:
            self.__bakiye += miktar
            print(f"{miktar} TL yatırıldı.")
        else:
            print("Geçersiz miktar.")
    
    def para_cek(self, miktar):
        if miktar > 0 and miktar <= self.__bakiye:
            self.__bakiye -= miktar
            print(f"{miktar} TL çekildi.")
        else:
            print("Yetersiz bakiye veya geçersiz miktar.")
    
    def set_bakiye(self, miktar):
        self.__bakiye= miktar

    def get_bakiye(self):
        return self.__bakiye

    def bakiye_goster(self):
        print(f"Mevcut bakiye: {self.get_bakiye()} TL")
        

class VadesizHesap(Hesap):
    def __init__(self, sahip_adi, hesap_numarasi, bakiye=0):
        super().__init__(sahip_adi, hesap_numarasi, bakiye)
    
    


class VadeliHesap(Hesap):
    def __init__(self, sahip_adi, hesap_numarasi, bakiye=0, faiz_orani=0.05):
        super().__init__(sahip_adi, hesap_numarasi, bakiye)
        self.faiz_orani = faiz_orani
    
    def faiz_hesapla(self):
        faiz = self.get_bakiye() * self.faiz_orani
        print(f"Faiz tutarı: {faiz} TL")
        return faiz
    
    def para_cek(self, miktar):
        if miktar > 0 and miktar <= self.get_bakiye():
            yeni_bakiye = self.get_bakiye() - miktar
            self.set_bakiye(yeni_bakiye)
            print(f"Yeni para {self.get_bakiye()}. Bakiye değiştiği için yeni faiz oranı: {self.faiz_hesapla()} oldu.")
        else:
            print("Yetersiz bakiye veya geçersiz miktar.")
    
    def bakiye_goster(self):
        print(f"Vadeli Hesap bakiye: {self.get_bakiye()} TL")

# Kullanımı
hesap1 = VadesizHesap("Ahmet Yılmaz", "123456", 1000)
hesap1.bakiye_goster()
hesap1.para_yatir(500)
hesap1.para_cek(200)
hesap1.bakiye_goster()

hesap2 = VadeliHesap("Mehmet Kaya", "987654", 2000, 0.08)
hesap2.bakiye_goster()
hesap2.faiz_hesapla()
hesap2.para_cek(500)
hesap2.bakiye_goster()

hesaplar = [hesap1,hesap2]

for i in hesaplar:
    i.bakiye_goster()