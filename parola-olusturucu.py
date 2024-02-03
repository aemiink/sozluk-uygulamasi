import random

# Kullanıcının parolasının içerebileceği tüm karakterleri içeren bir değişken oluşturun
karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

# Bir değişken oluşturun ve kullanıcıdan parolanın uzunluğunu girmesini isteyin
uzunluk = int(input("Parolanın Uzunluğu Ne Kadar Olmalı? "))

# Programın oluşturulan parolayı saklayacağı bir değişken oluşturun
sifre = ""

# Karakter değişkeninden rastgele bir karakter seçmek ve bunu oluşturulan parolanın bulunduğu değişkene eklemek için bir döngü ve random kütüphanesi kullanın
for i in range(uzunluk):
    sifre = random.choice(karakterler) + sifre

# Elde edilen parolayı konsola yazdırın
print(sifre) 
