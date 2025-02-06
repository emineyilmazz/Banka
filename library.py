# Kütüphane Yönetim Sistemi 

class Kitap:
    def __init__(self, ad, yazar, sayfa_sayisi, isbn):
        self.ad = ad
        self.yazar = yazar
        self.sayfa_sayisi = sayfa_sayisi
        self.isbn = isbn

    def __str__(self):
        return f"{self.ad} - {self.yazar} (ISBN: {self.isbn})"
    
class Kutuphane:
    def __init__(self):
        self.__kitaplar = []  # Encapsulation

    def kitap_ekle(self, kitap):
        if any(k.isbn == kitap.isbn for k in self.__kitaplar):
            raise Exception("Bu ISBN ile bir kitap zaten mevcut!")
        self.__kitaplar.append(kitap)
        print(f"{kitap.ad} kütüphaneye eklendi.")

    def kitap_sil(self, isbn):
        for kitap in self.__kitaplar:
            if kitap.isbn == isbn:
                self.__kitaplar.remove(kitap)
                print(f"{kitap.ad} kütüphaneden kaldırıldı.")
                return
        raise Exception("Belirtilen ISBN ile kitap bulunamadı!")

    def kitaplari_goster(self):
        if not self.__kitaplar:
            print("Kütüphanede hiç kitap yok.")
        else:
            for kitap in self.__kitaplar:
                print(kitap)

# Kullanım örneği
kutuphane = Kutuphane()
kitap1 = Kitap("1984", "George Orwell", 328, "1234567890")
kitap2 = Kitap("Sefiller", "Victor Hugo", 1200, "0987654321")

try:
    kutuphane.kitap_ekle(kitap1)
    kutuphane.kitap_ekle(kitap2)
    kutuphane.kitap_ekle(kitap1)  # Aynı kitabı eklemeye çalışıyoruz, hata fırlatmalı
except Exception as e:
    print(f"Hata: {e}")

kutuphane.kitaplari_goster()

try:
    kutuphane.kitap_sil("1234567890")
    kutuphane.kitap_sil("1111111111")  # Mevcut olmayan bir kitap, hata fırlatmalı
except Exception as e:
    print(f"Hata: {e}")

kutuphane.kitaplari_goster()
