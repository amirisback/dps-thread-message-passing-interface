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

# buat COMM
comm = MPI.COMM_WORLD

# dapatkan rank proses
rank = comm.Get_rank()

# dapatkan total proses berjalan
num_procs = comm.Get_size()

# jika saya rank ke 0 maka saya akan mengirimkan pesan ke proses yang mempunyai rank 1 s.d size
if rank == 0:
    for i in range(1, num_procs):
        data = "Hello, Rank " + str(i) + ". Rank 0 here"
        comm.send(data, dest=i)
# jika saya bukan rank 0 maka saya menerima pesan yang berasal dari proses dengan rank 0
else:
    data = comm.recv(source=0)
    print("Pesan yang diterima: " + data)
