# import os, re dan threading
import os
import re
import threading

# import time
import time


# buat kelas ip_check
class ip_check(threading.Thread):

    # fungsi __init__; init untuk assign IP dan hasil respons = -1
    def __init__(self, ip):
        threading.Thread.__init__(self)
        self.ip = ip
        self.__successful_pings = -1

    # fungsi utama yang diekseskusi ketika thread berjalan
    def run(self):
        # lakukan ping dengan perintah ping -n (gunakan os.popen())
        ping_out = os.popen("ping -n 2 " + self.ip, "r")

        # loop forever
        while True:
            # baca hasil respon setiap baris
            line = ping_out.readline()

            # break jika tidak ada line lagi
            if not line: break

            # baca hasil per line dan temukan pola Received = x
            n_received = re.findall(received_packages, line)

            # tampilkan hasilnya
            if n_received:
                self.__successful_pings = int(n_received[0])

    # fungsi untuk mengetahui status; 0 = tidak ada respon, 1 = hidup tapi ada loss, 2 = hidup
    def status(self):
        # 0 = tidak ada respon
        if self.__successful_pings == 0:
            return "tidak ada respon"


        # 1 = ada loss
        elif self.__successful_pings == 1:
            return "ada loss"

        # 2 = hidup
        elif self.__successful_pings == 2:
            return "hidup"

        # -1 = seharusnya tidak terjadi
        else:
            return "seharusnya tidak terjadi"


# buat regex untuk mengetahui isi dari r"Received = (\d)"
received_packages = re.compile(r"Received = (\d)")

# catat waktu awal
start = time.time()

# buat list untuk menampung hasil pengecekan
check_results = []

# lakukan ping untuk 20 host
for suffix in range(1, 20):
    # tentukan IP host apa saja yang akan di ping
    ip = "192.168.1." + str(suffix)

    # panggil thread untuk setiap IP
    current = ip_check(ip)

    # masukkan setiap IP dalam list
    check_results.append(current)

    # jalankan thread
    current.start()

# untuk setiap IP yang ada di list
for el in check_results:
    # tunggu hingga thread selesai
    el.join()

    # dapatkan hasilnya
    print("Status from ", el.ip, "is", el.status())

# catat waktu berakhir
end = time.time()

# tampilkan selisih waktu akhir dan awal
print(f"Waktu berjalan program: {end - start:0.4f} detik")
