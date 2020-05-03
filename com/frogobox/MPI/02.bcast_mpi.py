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
