# import mpi4py
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

from mpi4py import MPI

# import library random untuk generate angka integer secara random
import random

# buat COMM
comm = MPI.COMM_WORLD

# dapatkan rank proses
rank = comm.Get_rank()

# dapatkan total proses berjalan
num_procs = comm.Get_size()

# generate angka integer secara random untuk setiap proses
rand_int = random.randint(1, 100)

# jika saya adalah proses dengan rank 0 maka:
# saya menerima nilai dari proses 1 s.d proses dengan rank terbesar
# menjumlah semua nilai yang didapat (termasuk nilai proses saya)
if rank == 0:
    sum = 0
    for i in range(1, num_procs):
        sum += comm.recv(source=i)
    print("Hasil akhir penjumlahan total: " + str(sum))
# jika bukan proses dengan rank 0, saya akan mengirimkan nilai proses saya ke proses dengan rank=0
else:
    print("Menambahkan nilai: " + str(rand_int) + " ke rank  0")
    comm.send(rand_int, dest=0)
