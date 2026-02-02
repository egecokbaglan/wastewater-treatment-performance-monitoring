import matplotlib.pyplot as plt
import random
import pandas as pd

# TR: Limitler (Sunum ve Rapora uygun)
limit_tablosu = {
    "KOI": 160, 
    "BOI": 50,  
    "AKM": 60,  
    "NH4": 10   
}

print(" T.C. ISTANBUL ÜNİVERSİTESİ-CERRAHPAŞA")
print(" EVSEL ATIK SU ARITMA TESİSİ PERFORMANS İZLEME PROGRAMI")
print("-------------------------------------------------------")

# --- BÖLÜM 1: ETKİLEŞİM (10 SORU KURALI) ---

# Soru 1-4: Metin girişleri (Hata riski düşük, döngüye gerek yok)
muhendis = input("1. Mühendis Adı Soyadı: ")
rapor_no = input("2. Rapor No: ")
tarih = input("3. Tarih (GG.AA.YYYY): ")

while True:
    # TR: Koruma eklendi (Sadece E veya H)
    ekipman = input("4. Arızalı ekipman var mı? (E/H): ")
    if ekipman == "E" or ekipman == "e" or ekipman == "H" or ekipman == "h":
        break
    else:
        print("-> HATA: Lütfen sadece 'E' veya 'H' giriniz!")

# Soru 5: Tesis Seçimi
# Not: Rapora göre (Sayfa 14) farklı isim girilebilir, bu yüzden döngü yok.
print("\n--- Tesis Listesi ---")
print("1- Ankara AAT | 2- Ataköy AAT | 3- Paşaköy AAT")
tesis_girdi = input("5. Tesis Seçimi veya İsmi: ")

if tesis_girdi == "1":
    tesis_adi = "Ankara AAT"
elif tesis_girdi == "2":
    tesis_adi = "Ataköy AAT"
elif tesis_girdi == "3":
    tesis_adi = "Paşaköy AAT"
else:
    tesis_adi = tesis_girdi 

# Soru 6: Parametre Seçimi (KORUMA EKLENDİ)
while True:
    print("\n--- Parametreler ---")
    print("1- KOI | 2- BOI | 3- AKM | 4- NH4")
    p_secim = input("6. Analiz Parametresi (1-4): ")

    if p_secim == "1" or p_secim == "KOI":
        parametre = "KOI"
        limit = 160
        break
    elif p_secim == "2" or p_secim == "BOI":
        parametre = "BOI"
        limit = 50
        break
    elif p_secim == "3" or p_secim == "AKM":
        parametre = "AKM"
        limit = 60
        break
    elif p_secim == "4" or p_secim == "NH4":
        parametre = "NH4"
        limit = 10
        break
    else:
        print("-> HATA: Lütfen listeden geçerli bir numara (1-4) seçiniz!")

# Soru 7: Veri Kaynağı (KORUMA EKLENDİ)
while True:
    print("\n--- Veri Kaynağı ---")
    print("1- Otomatik | 2- Manuel | 3- CSV Dosyası")
    kaynak = input("7. Veri Kaynağı Seçimi: ")
    
    if kaynak == "1" or kaynak == "2" or kaynak == "3":
        break
    else:
        print("-> HATA: Lütfen 1, 2 veya 3 giriniz!")

# Soru 8: Yağış (KORUMA EKLENDİ)
yagis = "H"
if kaynak == "1":
    while True:
        yagis = input("8. Bölgede yağış var mı? (E/H): ")
        if yagis == "E" or yagis == "e" or yagis == "H" or yagis == "h":
            break
        else:
            print("-> HATA: Sadece E veya H giriniz!")

# Soru 9: Renk (KORUMA EKLENDİ)
while True:
    print("\n--- Grafik Rengi ---")
    print("1- Kirmizi | 2- Mavi | 3- Yesil")
    renk_no = input("9. Renk Seçimi: ")
    
    if renk_no == "1": 
        color = "red"
        break
    elif renk_no == "2": 
        color = "blue"
        break
    elif renk_no == "3":
        color = "green"
        break
    else:
        print("-> HATA: Lütfen renk seçiniz (1-3)!")

# Soru 10: Kayıt (KORUMA EKLENDİ)
while True:
    kayit = input("10. Veriler kaydedilsin mi? (E/H): ")
    if kayit == "E" or kayit == "e" or kayit == "H" or kayit == "h":
        break
    else:
        print("-> HATA: Sadece E veya H giriniz!")

# --- BÖLÜM 2: VERİ İŞLEME ---
gunler = [1, 2, 3, 4, 5, 6, 7]
giris_listesi = []
cikis_listesi = []

if kaynak == "2": # Manuel
    print("\n--- Manuel Veri Girişi ---")
    for i in range(7):
        print(f"Gün {i+1}:")
        # Burası mühendis girişi olduğu için basit input bıraktık
        # Sayı girilmezse Python hata verir, ama try-except yasak olduğu için böyle kalmalı.
        g = float(input(" Giriş Değeri: "))
        c = float(input(" Çıkış Değeri: "))
        giris_listesi = giris_listesi + [g]
        cikis_listesi = cikis_listesi + [c]

elif kaynak == "3": # CSV (Pandas)
    print("\n-> 'atiksu_verileri.csv' okunuyor...")
    # Dosya yoksa hata verir, ama basitlik için kontrol eklemedik
    df = pd.read_csv("atiksu_verileri.csv")
    giris_listesi = df["Giris"].tolist()
    cikis_listesi = df["Cikis"].tolist()

else: # Otomatik
    print("\n-> Simülasyon verileri üretiliyor...")
    for i in range(7):
        r_g = random.randint(200, 500)
        r_c = random.randint(20, 180)
        if yagis == "E" or yagis == "e":
            r_g = r_g * 0.9 
            r_c = r_c * 0.9
        giris_listesi = giris_listesi + [int(r_g)]
        cikis_listesi = cikis_listesi + [int(r_c)]

# --- BÖLÜM 3: ANALİZ VE ÇIKTI ---
print("\n" + "="*50)
print(f" TESİS: {tesis_adi} | PARAMETRE: {parametre}")
print(f" MÜHENDİS: {muhendis} | LIMIT: {limit} mg/L")
print("="*50)

asimi_kontrol = False

for i in range(7):
    g = giris_listesi[i]
    c = cikis_listesi[i]
    
    # Verim Hesabı
    if g == 0: verim = 0
    else: verim = ((g - c) / g) * 100
    
    durum = "UYGUN"
    if c > limit:
        durum = "!!! LIMIT ASILDI !!!"
        asimi_kontrol = True
    
    print(f"Gün {i+1}: Giriş={int(g)}, Çıkış={int(c)}, Verim=%{int(verim)} -> {durum}")

    if verim < 70:
        print("   -> ÖNERİ: Verim düşük! Havalandırma tanklarını kontrol edin.")

print("-" * 50)
if asimi_kontrol:
    print("SONUÇ: Kritik limit aşımı tespit edildi!")
else:
    print("SONUÇ: Tesis performansı uygundur.")

# --- BÖLÜM 4: GRAFİK ---
plt.plot(gunler, cikis_listesi, color=color, marker='o', label="Çıkış Suyu")
plt.plot(gunler, [limit]*7, color='red', linestyle='--', label="Yasal Limit")

plt.title(f"{tesis_adi} - {parametre} Analizi")
plt.xlabel("Günler")
plt.ylabel("Konsantrasyon (mg/L)")
plt.legend()
plt.grid(True)
plt.show()
