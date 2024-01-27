sozluk = {
    "Esef" : "Olmaması, yapılmaması gereken veya yapılamayan bir şey için duyulan üzüntü." ,
    "Emin" : "Güvenilir, Doğru"
}

print(*sozluk)

kullanici_istek = input("Hangi Kelimenin Anlamını Öğrenmek İsiyorsunuz?")

if kullanici_istek in sozluk.keys():
    print("Girdiğiniz Kelimenin Anlamı: ", sozluk[kullanici_istek])
else:
    print("Bu Kelime Sözlükte Bulunmuyor!")
