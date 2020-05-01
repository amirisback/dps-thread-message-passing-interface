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
print("Menambahkan nilai :" + str(rand_int) + " dari rank " + str(rank))

# lakukam penjumlahan dengan teknik reduce, root reduce adalah proses dengan rank 0
sum = comm.reduce(rand_int, MPI.SUM, 0)

# jika saya proses dengan rank 0 maka saya akan menampilkan hasilnya
if rank == 0:
    print("Hasil penjumlahan: " + str(sum))
