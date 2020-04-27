# import mpi4py


# buat fungsi dekomposisi bernama local_loop 
# local_loop akan menghitung setiap bagiannya
# gunakan 4/(1+x^2), perhatikan batas awal dan akhir untuk dekomposisi
# misalkan size = 4 maka proses 0 menghitung 0-25, proses 1 menghitung 26-50, dst
def local_loop(num_steps,begin,end):
    step = 1.0/num_steps
    sum = 0
    # 4/(1+x^2)
    for i in range(begin,end):
        
    print (sum)
    return sum    

# fungsi Pi
def Pi(num_steps):
    
    # buat COMM
    
    
    # dapatkan rank proses
    
    
    # dapatkan total proses berjalan
    
    
    # buat variabel baru yang merupakan num_steps/total proses
    
    
    # cari local_sum
    # local_sum merupakan hasil dari memanggil fungsi local_loop
    
    
    # lakukan penjumlahan dari local_sum proses-proses yang ada ke proses 0
    # bisa digunakan reduce atau p2p sum
    
    
    # jika saya proses dengan rank 0  maka tampilkan hasilnya
    if rank == 0:
        pi = sum / num_steps
        print (pi)
    
# panggil fungsi utama    
if __name__ == '__main__':
    Pi(10000)
