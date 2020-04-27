# import os, re dan threading


# import time


# buat kelas ip_check
class ip_check(threading.Thread):
    
    # fungsi __init__; init untuk assign IP dan hasil respons = -1
    def __init__ (self,ip):
        
    
    # fungsi utama yang diekseskusi ketika thread berjalan
    def run(self):
        # lakukan ping dengan perintah ping -n (gunakan os.popen())
        
        
        # loop forever
        while True:
            # baca hasil respon setiap baris
            
            
            # break jika tidak ada line lagi
            
            
            # baca hasil per line dan temukan pola Received = x
            
            
            # tampilkan hasilnya
            
                
    # fungsi untuk mengetahui status; 0 = tidak ada respon, 1 = hidup tapi ada loss, 2 = hidup
    def status(self):
        # 0 = tidak ada respon
        
        
        # 1 = ada loss
        
        # 2 = hidup
        
        # -1 = seharusnya tidak terjadi
            
# buat regex untuk mengetahui isi dari r"Received = (\d)"


# catat waktu awal


# buat list untuk menampung hasil pengecekan


# lakukan ping untuk 20 host
for suffix in range(1,20):
    # tentukan IP host apa saja yang akan di ping
    
    
    # panggil thread untuk setiap IP
    
    
    # masukkan setiap IP dalam list
    
    
    # jalankan thread
    

# untuk setiap IP yang ada di list
for el in check_results:
    
    # tunggu hingga thread selesai
    el.join()
    
    # dapatkan hasilnya
    

# catat waktu berakhir


# tampilkan selisih waktu akhir dan awal

