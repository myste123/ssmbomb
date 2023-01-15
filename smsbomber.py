from colorama import Fore, Style
from time import sleep
from os import system
from requests import get
r = get("https://raw.githubusercontent.com/tingirifistik/Enough/main/sms.py").text
with open("sms.py", "r", encoding="utf-8") as f:
    read = f.read()
if read == r:
    pass
else:
    print(Fore.RED + "Güncelleme yapılıyor...")
    with open("sms.py", "w", encoding="utf-8") as f:
        f.write(r)
from sms import SendSms
r = get("https://raw.githubusercontent.com/tingirifistik/Enough/main/call.py").text
with open("call.py", "r", encoding="utf-8") as f:
    read = f.read()
if read == r:
    pass
else:
    print(Fore.RED + "Güncelleme yapılıyor...")
    with open("call.py", "w", encoding="utf-8") as f:
        f.write(r)
from call import SendCall

servisler_call = []
for attribute in dir(SendCall):
    attribute_value = getattr(SendCall, attribute)
    if callable(attribute_value):
        if attribute.startswith('__') == False:
            servisler_call.append(attribute)
servisler_sms = []
for attribute in dir(SendSms):
    attribute_value = getattr(SendSms, attribute)
    if callable(attribute_value):
        if attribute.startswith('__') == False:
            servisler_sms.append(attribute)    

while 1:
    system("cls||clear")
    print("""{}
     ______                         _     
█▀▀ █▀▄▀█ █▀▀   █▀▀▄ █▀▀█ █▀▄▀█ █▀▀▄ █▀▀ █▀▀█
▀▀█ █░▀░█ ▀▀█   █▀▀▄ █░░█ █░▀░█ █▀▀▄ █▀▀ █▄▄▀
▀▀▀ ▀░░░▀ ▀▀▀   ▀▀▀░ ▀▀▀▀ ▀░░░▀ ▀▀▀░ ▀▀▀ ▀░▀▀
                 {}by $hitt.#7777  
    """.format(Fore.LIGHTCYAN_EX, len(servisler_sms), len(servisler_call), Style.RESET_ALL, Fore.LIGHTRED_EX))
    try:
        menu = int(input(Fore.LIGHTMAGENTA_EX + " 1- SMS Gönder\n 2- Ara\n 3- Çıkış\n\n" + Fore.LIGHTYELLOW_EX + " Seçim: "))
    except ValueError:
        system("cls||clear")
        print(Fore.LIGHTRED_EX + "Hatalı giriş yaptınız. Tekrar deneyiniz.")
        sleep(3)
        continue
    if menu == 1:
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "Telefon numarasını başında '+90' olmadan yazınız: "+ Fore.LIGHTGREEN_EX, end="")
            tel_no = int(input())
            if len(str(tel_no)) != 10:
                raise ValueError
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı telefon numarası. Tekrar deneyiniz.") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "Mail adresi (Bilmiyorsanız 'enter' tuşuna basın): "+ Fore.LIGHTGREEN_EX, end="")
            mail = input()
            if ("@" not in mail or ".com" not in mail) and mail != "":
                raise
        except:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı mail adresi. Tekrar deneyiniz.") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "Kaç adet SMS göndermek istiyorsun: "+ Fore.LIGHTGREEN_EX, end="")
            kere = int(input())
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı giriş yaptınız. Tekrar deneyiniz.") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "Kaç saniye aralıkla göndermek istiyorsun: "+ Fore.LIGHTGREEN_EX, end="")
            aralik = int(input())
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı giriş yaptınız. Tekrar deneyiniz.") 
            sleep(3)
            continue
        system("cls||clear")
        sms = SendSms(tel_no, mail)
        while sms.adet < kere:
            for attribute in dir(SendSms):
                attribute_value = getattr(SendSms, attribute)
                if callable(attribute_value):
                    if attribute.startswith('__') == False:
                        if sms.adet == kere:
                            break
                        exec("sms."+attribute+"()")
                        sleep(aralik)
        print(Fore.LIGHTRED_EX + "\nMenüye dönmek için 'enter' tuşuna basınız..")
        input()
    elif menu == 2:
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "Telefon numarasını başında '+90' olmadan yazınız: "+ Fore.LIGHTGREEN_EX, end="")
            tel_no = int(input())
            if len(str(tel_no)) != 10:
                raise ValueError
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı telefon numarası. Tekrar deneyiniz.") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "Mail adresi (Bilmiyorsanız 'enter' tuşuna basın): "+ Fore.LIGHTGREEN_EX, end="")
            mail = input()
            if ("@" not in mail or ".com" not in mail) and mail != "":
                raise
        except:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı mail adresi. Tekrar deneyiniz.") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + f"Kaç kere aransın (max: {len(servisler_call)}): "+ Fore.LIGHTGREEN_EX, end="")
            kere = int(input())
            if kere > len(servisler_call):
                raise ValueError
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı giriş yaptınız. Tekrar deneyiniz.") 
            sleep(3)
            continue
        system("cls||clear")
        call = SendCall(tel_no, mail)
        while call.adet < kere:
            for attribute in dir(SendCall):
                attribute_value = getattr(SendCall, attribute)
                if callable(attribute_value):
                    if attribute.startswith('__') == False:
                        if call.adet == kere:
                            break
                        exec("call."+attribute+"()")
        print(Fore.LIGHTRED_EX + "\nMenüye dönmek için 'enter' tuşuna basınız..")
        input()
    elif menu == 3:
        system("cls||clear")
        print(Fore.LIGHTRED_EX + "Çıkış yapılıyor...")
        break
