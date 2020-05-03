"""
    Cara menjalankan
     1. pip install mpi4py
     2.
        (Windows)
        2a.1. Install Windows mpi (https://docs.microsoft.com/en-us/message-passing-interface/microsoft-mpi)
        2a.2. Apabila telah ter install jalankan dengan run command `mpiexec -n [JUMLAH_PROSES] python [NAMA_FILE].py`

        (Linux)
        2b.1 mpirun -np [JUMLAH_PROSES] python [NAMA_FILE].py
"""

# mpiexec -n 5 python 02.bcast_mpi.py


# import mpi4py
from mpi4py import MPI

# buat COMM
comm = MPI.COMM_WORLD

# dapatkan rank proses
rank = comm.Get_rank()

# dapatkan total proses berjalan
num_procs = comm.Get_size()

# jika saya rank 0 maka saya akan melakukan broadscast
if rank == 0:
    comm.bcast("Hello, rank 0 disini, mengirim ke semua rank", root=0)
# jika saya bukan rank 0 maka saya menerima pesan
else:
    data = comm.bcast(None, root=0)
    print("Pesan yang diterima pada rank " + str(rank) + ": " + data)
