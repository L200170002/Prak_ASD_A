                                                            #TUGAS MODUL 2
                                                           # NAMA  : SUGIYOW
                                                            # NIM   : L200170002
                                                            # KELAS : A

# NOMER 1
class Pesan():
    """
        Sebuah class bernama Pesan.Untuk memahami konsep Class dan Object.
    """
    def __init__(self,sebuahString):
        self.teks = sebuahString
    def cetakIni(self):
        print(self.teks)
    def cetakPakaiHurufKapital(self):
        print(str.upper(self.teks))
    def cetakPakaiHurufKecil(self):
        print(str.lower(self.teks))
    def jumKar(self):
        return len(self.teks)
    def cetakJumlahKarakterku(self):
        print("Kalimatku mempunyai",len(self.teks),"karakter")
    def perbarui(self,stringBaru):
        self.teks = stringBaru

# NOMER 1A
    def apakahTerkandung(self,x):
        if x in self.teks:
            print("Terdapat")
        else:
            print("Tidak Terdapat")

# NOMER 1B
    def hitungKonsonan(self):
        konsonan = "bcdfghijklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
        jumlahKonsonan =""
        for karakter in self.teks:
            if karakter in konsonan:
                jumlahKonsonan += karakter
        print(len(jumlahKonsonan))

# NOMER 1C
    def hitungVokal(self):
        vokal = "aiueoAIUEO"
        jumlahVokal =""
        for karakter in self.teks:
            if karakter in vokal:
                jumlahVokal += karakter
        print(len(jumlahVokal))

## HAKAKSES
print("Nomer 1 A")
p9 = Pesan("Indonesia adalah negeri yang indah")
p9.apakahTerkandung("ege")
p9.apakahTerkandung("eka")
print("\n" +"Nomer 1 B")
p10 = Pesan("Surakarta")
p10.hitungKonsonan()
print("\n" +"Nomer 1 C")

# NOMER 2
class Manusia(object):
    keadaan = "lapar"
    def __init__(self,nama):
        self.nama = nama
    def ucapkanSalam(self):
        print("Salam, namaku", self.nama)
    def makan(self,K):
        print("Saya baru saja makan", K)
        self.keadaan = "kenyang"
    def olahraga(self,L):
        print("Saya baru saja latihan", L)
        self.keaddan = "lapar"
    def mengalikanDenganDua(self,n):
        return n*2

p1 = Manusia("Fatimah")
p1.ucapkanSalam
        
class Mahasiswa(Manusia):
    
    
    """Class Mahasiswa yang dibangun dari class Manusia"""
    def __init__(self,nama,NIM,kota,us):
        """Metode inisialisasi ini menutupimetode inisiasi di class Manusia."""
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangsaku = us
    def __str__(self):
        s=self.nama+", NIM" + str(self.NIM)\
           +". Tinggal di" + self.kotaTinggal \
           +". Uang saku Rp."+ str(self.uangsaku)\
           +" tiap bulannya."
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilUangSaku(self):
        return self.uangsaku
    def makan(self,s):
        """Metode ini menutupi makan -nya class Manusia. Mahasiswa kalau makan sambil belajar"""
        print("Saya baru saja makan",s,"sambil belajar.")
        self.keadaan="Kenyang"

# NOMER 2A
    def ambilKotaTinggal(self):
        return self.kotaTinggal

    
# NOMER 2B
    def perbaruiKotaTinggal(self,x):
        self.kotaTinggal=x

# NOMER 2C
    def tambahUangSaku(self,y):
        self.y=y
        self.uangsaku=self.uangsaku+self.y


# NOMER 3
a = input("masukan nama : ")
b = input("masukan NIM : ")
c = input("masukan kota asal : ")
d = input("jumlah uang saku : ")

# instance
m1 =  Mahasiswa("gio","L2001700o2","karanganyar",15000000)
m2 = Mahasiswa("susi","D2001600124","surakarta",650000)
m3 = Mahasiswa("gilang","D2001700620","",400000)
mb = Mahasiswa(a,b,c,d)
a = MhsTIF("Desya",2327,"sulawesi",350000)
p10.hitungVokal()

# NOMER 4
    listKuliah =["ALGORITMA"]
    def ambilKuliah(self, kuliah):
        self.listKuliah.append(kuliah)


# NOMER 5
    def hapusKuliah(self, item):
        self.listKuliah.remove(item)

# NOMER 6
class SiswaSMA(Manusia):
    """Class SiswaSMA yang dibangun dari class Manusia"""
    def __init__(self,umur,id_siswa,asal):
        """Metode inisialisasi ini menutupimetode inisiasi di class Manusia."""
        self.umur = umur
        self.id = id_siswa
        self.sekolah = asal
    def __str__(self):
        a="ID Siswa :"+str(self.id)+'\n'+"Umur Siswa :"+str(self.umur)+'\n'+"Asal Sekolah :" +self.sekolah 
        print (a)
    def tampilkanumur(self):
        return self.umur
    def asalSekolah(self):
        return self.sekolah
    def idSiswa(self):
        return self.id


##NOMER 7
class MhsTIF(Mahasiswa):
    """Class MhsTIF yang dibangun dari class Mahasiswa"""
    def katakanpy(self):
        print('Python is cool.')

##keterangan no.7
#class Mahasiswa:
# a.NIM                 
# a.ambilKotaTinggal    
# a.ambilkuliah         
# a.ambilNIM            
# a.ambilNama           
# a.ambilUangSaku       
# a.hapusKuliah
# a.kotaTinggal         
# a.listKuliah
# a.perbaruiKotaTinggal
# a.tambahUangSaku      
# a.uangsaku           
#
#class Manusia:
# a.keadaan
# a.makan               
# a.mengalikanDenganDua 
# a.nama               
# a.olahraga
# a.ucapkanSalam
#
#class MhsTIF:
# a.katakanpy
    
##AKSES     
m9 = Mahasiswa("GIO","L2001700O2","KARANGANYAR",50000)
s1 = SiswaSMA("DANU",L200170002,54,"NGANJUK")

## m9.ambilKotaTinggal()
## m9.perbaruiKotaTinggal('Solo')
## m9.ambilKotaTinggal()
## m9.ambilUangSaku()
## m9.tambahUangSaku(45000)

