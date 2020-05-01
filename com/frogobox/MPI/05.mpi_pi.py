"""
    Cara menjalankan 
     1. pip install mpi4py
     2. 
        (Windows)
        2a.1. Install Windows MPI (https://docs.microsoft.com/en-us/message-passing-interface/microsoft-mpi)
        2a.2. Apabila telah ter install jalankan dengan run command `mpiexec -n [JUMLAH_PROSES] python [NAMA_FILE].py`
        
        (Linux)
        2b.1 mpirun -np [JUMLAH_PROSES] python [NAMA_FILE].py
"""

# import mpi4py
from mpi4py import MPI


# buat fungsi dekomposisi bernama local_loop 
# local_loop akan menghitung setiap bagiannya
# gunakan 4/(1+x^2), perhatikan batas awal dan akhir untuk dekomposisi
# misalkan size = 4 maka proses 0 menghitung 0-25, proses 1 menghitung 26-50, dst
def local_loop(num_steps, begin, end):
    step = 1.0 / num_steps
    sum = 0
    # 4/(1+x^2)
    for i in range(begin, end):
        x = float((i + 0.5) * step)
        sum += 4 / (1 + x ** 2)
    print(sum)
    return sum


# fungsi Pi
def Pi(num_steps):
    # buat COMM
    comm = MPI.COMM_WORLD

    # dapatkan rank proses
    rank = comm.Get_rank()

    # dapatkan total proses berjalan
    num_procs = comm.Get_size()

    # buat variabel baru yang merupakan num_steps/total proses
    num_steps = num_steps

    # cari local_sum
    # local_sum merupakan hasil dari memanggil fungsi local_loop
    num_steps2 = int(num_steps / num_procs)
    local_sum = local_loop(num_steps, rank * num_steps2, (rank + 1) * num_steps2)

    # lakukan penjumlahan dari local_sum proses-proses yang ada ke proses 0
    # bisa digunakan reduce atau p2p sum
    pi = comm.reduce(local_sum, MPI.SUM, 0)

    # jika saya proses dengan rank 0  maka tampilkan hasilnya
    if rank == 0:
        pi = pi / num_steps
        print("Hasil perhitungan pi: " + str(pi))


# panggil fungsi utama    
if __name__ == '__main__':
    Pi(10000)
