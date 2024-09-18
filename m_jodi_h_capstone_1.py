kode = ["SK001", "SK002", "SK003", "SK004", "SK005", "SK006", "SK007", "SK008", "SK009", "SK010"]
nama = {"SK001": "Kerupuk Ikan", "SK002": "Kerupuk Udang", "SK003": "Kerupuk Bawang", "SK004": "Kerupuk Kulit", "SK005": "Rempeyek Kacang", "SK006": "Rempeyek Udang", "SK007": "Rempeyek Bayam", "SK008": "Keripik Bawang", "SK009": "Keripik Singkong", "SK010": "Keripik Jagung"}
h_beli = {"SK001": 13500, "SK002": 12000, "SK003": 10500, "SK004": 11000, "SK005": 15500, "SK006": 17000, "SK007": 15000, "SK008": 17500, "SK009": 18000, "SK010": 19500}
h_jual = {"SK001": 15500, "SK002": 13500, "SK003": 12000, "SK004": 13000, "SK005": 17000, "SK006": 19500, "SK007": 18000, "SK008": 20000, "SK009": 21500, "SK010": 21000}
s_awal = {"SK001": 14, "SK002": 10, "SK003": 8, "SK004": 19, "SK005": 17, "SK006": 16, "SK007": 20, "SK008": 15, "SK009": 14, "SK010": 21}

def delete (kb):
    kode.remove (kb)
    del nama[kb]
    del h_beli[kb]
    del h_jual[kb]
    del s_awal[kb]
    print ("Barang", kb, "berhasil dihapus")
    stok ()

def update (kb):
    print ("Masukkan data baru secara berurut")
    k = ""
    k = input ("Masukkan kode barang baru: ")
    n = ""
    n = input ("Masukkan nama barang baru: ")
    hb = 0
    hb = input ("Masukkan harga beli barang baru: ")
    hj = 0
    hj = input ("Masukkan harga jual barang baru: ")
    sa = 0
    sa = input ("Masukkan stok awal barang baru: ")

    while True:
        try:
            int (hb) and int (hj) and int (sa)
            break
        except:
            print ("\nMasukkan harga dan stok dalam bilangan bulat! Pengubahan data dibatalkan")
            stok ()

    hb = int (hb)
    hj = int (hj)
    sa = int (sa)
    t1 = (n, hb, hj, sa)
    t2 = (nama, h_beli, h_jual, s_awal)
    
    if k == kb:
        i = 0
        for i in range (0, len (t1)):
            t2[i][kb] = t1[i]
        print ("\nData barang", kb, "berhasil diubah")
    elif k != kb and k in kode:
        print ("\nKode barang duplikat terdeteksi, pengubahan data dibatalkan")
    elif k != kb and k not in kode:
        kode.remove(kb)
        kode.append(k)
        kode.sort()
        nama[k] = nama[kb]
        del nama[kb]
        h_beli[k] = h_beli[kb]
        del h_beli[kb]
        h_jual[k] = h_jual[kb]
        del h_jual[kb]
        s_awal[k] = s_awal[kb]
        del s_awal[kb]

        i = 0
        for i in range (0, len (t1)):
            t2[i][k] = t1[i]
        print ("\nData barang berhasil diubah dari", kb, "menjadi", k)
    else:
        pass

    stok ()

def search (kw):
    if kw not in kode:
        print ("Barang tidak ditemukan!")
        start ()
    elif kw in kode:
        print ("\n{:<20} {:<12} {:<12} {:<8}".format ("Nama Barang", "Harga Beli", "Harga Jual", "Stok Awal"))
        print ("\n{:<20} {:<12} {:<12} {:<8}".format (nama[kw], h_beli[kw], h_jual[kw], s_awal[kw]))
        print ("\nBarang ditemukan, yakin melanjutkan operasi mutasi? Masukkan 'y' untuk lanjut atau 'n' untuk membatalkan")
        i = input ("(y/n): ")
        if i == "y":
            pass
        elif i == "n":
            print ("Operasi mutasi dibatalkan")
            start ()
        else:
            print ("Input tidak sah, membatalkan operasi")
            start ()
    else:
        pass

def search_to_stok (kw):
    if kw not in kode:
        print ("Barang tidak ditemukan!")
    elif kw in kode:
        print ("\n{:<20} {:<12} {:<12} {:<8}".format ("Nama Barang", "Harga Beli", "Harga Jual", "Stok Awal"))
        print ("\n{:<20} {:<12} {:<12} {:<8}".format (nama[kw], h_beli[kw], h_jual[kw], s_awal[kw]))
    else:
        pass
    
    stok ()    

def read ():
    print ("\n{:<15} {:<20} {:<12} {:<12} {:<8}".format ("Kode Barang", "Nama Barang", "Harga Beli", "Harga Jual", "Stok Awal\n"))
    i = 0
    for i in range (0, len (kode)):
        print ("{:<15} {:<20} {:<12} {:<12} {:<8}".format (kode[i], nama[kode[i]], h_beli[kode[i]], h_jual[kode[i]], s_awal[kode[i]]))
    stok ()

def create (kb):
    search (kb)
    print ("\nMasukkan jumlah barang masuk dan barang keluar untuk barang ini")
    m = 0
    k = 0
    m = input ("Jumlah barang masuk: ")
    k = input ("Jumlah barang keluar: ")

    while True:
        try:
            int (m) and int (k)
            break
        except:
            print ("\nMasukkan jumlah barang dalam bilangan bulat! Operasi dibatalkan")
            start ()

    m = int (m)
    k = int (k)
    r = 0
    sa = 0
    r = m - k
    sa = s_awal[kb]
    if sa + r < 0:
        print ("Perhatian, stok akhir barang kurang dari nol. Input salah! Operasi dibatalkan")
        start ()
    else:
        pass

    s_awal[kb] = sa + r
    print ("\nMutasi barang:")
    print ("\n{:<20} {:<12} {:<12} {:<8} {:<8} {:<8} {:<8}".format ("Nama Barang", "Harga Beli", "Harga Jual", "Stok Awal", "Barang Masuk", "Barang Keluar", "Stok Akhir"))
    print ("\n{:<20} {:<12} {:<12} {:<8} {:<8} {:<8} {:<8}".format (nama[kb], h_beli[kb], h_jual[kb], sa, m, k, s_awal[kb]))

    if s_awal[kb] == 0:
        print ("Perhatian, stok barang", kb, "sudah habis")
    else:
        pass
    start ()

def m_start (o):
    if o == "1":
        stok ()
    elif o == "2":
        mutasi ()
    elif o == "q":
        print ("\nSampai jumpa!")
        quit ()
    else:
        print ("Maaf, input tidak sah")
        start ()

def m_stok (o):
    k = ""
    k1 = ""
    c = ""
    if o == "1":
        print ("\nDaftar barang:")
        read ()
    elif o == "2":
        print ("\nMasukkan kode barang atau masukkan 'q' untuk ke menu sebelumnya")
        c = input ("Kode barang: ")
        if c == "q":
            stok ()
        elif c != "q":
            search_to_stok (c)
        else:
            pass
    elif o == "3":
        print ("\nMasukkan kode barang yang akan diubah")
        k = input ("Kode barang: ")
        if k not in kode:
            print ("Barang tidak ditemukan")
            stok ()
        elif k in kode:
            print ("Barang", k, "ditemukan. Ubah data barang ini? Masukkan 'y' untuk melanjutkan atau 'n' untuk membatalkan")
            k1 = input ("(y/n): ")
            if k1 == "y":
                update (k)
            elif k1 == "n":
                print ("Pengubahan data dibatalkan")
                stok ()
            else:
                print ("Input tidak sah, membatalkan pengubahan data")
                stok ()
    elif o == "4":
        print ("\nMasukkan kode barang yang akan dihapus")
        k = input ("Kode barang: ")
        if k not in kode:
            print ("Barang tidak ditemukan")
            stok ()
        elif k in kode:
            print (k, "ditemukan. Yakin hapus barang ini? Masukkan 'y' untuk menghapus atau 'n' untuk membatalkan")
            k1 = input ("(y/n): ")
            if k1 == "y":
                delete (k)
            elif k1 == "n":
                print ("Penghapusan dibatalkan")
                stok ()
            else:
                print ("Input tidak sah, membatalkan penghapusan")
                stok ()
    elif o == "q":
        start ()
    else:
        print ("Maaf, input tidak sah \n")
        stok ()

def mutasi ():
    print ("Masukkan kode barang:")
    k = ""
    k = input ("Kode barang:")
    create (k)

def stok ():
    print ("\nMenu: \n1. Tampilkan stok barang \n2. Cari barang \n3. Ubah data barang \n4. Hapus barang \nMasukkan angka 1-4 untuk menuju ke opsi menu yang diinginkan atau masukkan 'q' untuk ke menu sebelumnya")
    opsi = ""
    opsi = input ("Opsi (1/2/3/4/q): ")
    m_stok (opsi)

def start ():
    print ("\nSelamat datang di aplikasi inventaris gudang \nMenu: \n1. Stok Barang \n2. Mutasi Barang \nMasukkan angka 1-2 untuk menuju ke opsi menu yang diinginkan atau masukkan 'q' untuk keluar aplikasi")
    opsi = ""
    opsi = input ("Opsi (1/2/q): ")
    m_start (opsi)

start ()