import tkinter as tk


def hesapla_vki():
    if entry_name.get() and float(entry_kilo.get()) and float(entry_boy.get()):
        name = entry_name.get()
        kilo = float(entry_kilo.get())
        boy = float(entry_boy.get())
        vki = kilo / boy ** 2
        vki = round(vki, 2)

        if vki <= 18.5:
            durum = "Zayıf"
        elif vki > 18.5 and vki <= 24.9:
            durum = "Normal"
        elif vki >= 25 and vki <= 29.9:
            durum = "Fazla Kilolu"
        elif vki >= 30 and vki <= 34.9:
            durum = "Obezite Sınıfı I"
        elif vki >= 35 and vki <= 99.9:
            durum = "Obezite Sınıfı II"
        elif vki >= 40:
            durum = "Obezite Sınıfı III"

        label_vki.config(text="İsim : {} \n VKI : {}\n Durum : {}".format(name, vki, durum))

    else:
        label_vki.config(text="Bilgiler eksik \n veya \n yanlış lütfen hepsini doğru giriniz !")


root = tk.Tk()
root.geometry("300x300")

root.configure(bg="#F0F0F0")
label_title = tk.Label(root, text="Vücut Kitle İndeks Hesaplama", font=("Arial", 14, "bold"), bg="#333333")
label_title.pack()

label = tk.Label(root, text="Lütfen adınızı giriniz:")
label.pack()

entry_name = tk.Entry(root)
entry_name.pack()

label = tk.Label(root, text="Lütfen kilonuzu giriniz (Örn: 56.8):")
label.pack()

entry_kilo = tk.Entry(root)
entry_kilo.pack()

label = tk.Label(root, text="Lütfen boyunuzu giriniz (Örn: 1.65):")
label.pack()

entry_boy = tk.Entry(root)
entry_boy.pack()

label_vki = tk.Label(root, text="Vücut kitle indeksiniz:")
label_vki.pack()

button = tk.Button(root, text="Hesapla", command=hesapla_vki)
button.pack()

root.mainloop()