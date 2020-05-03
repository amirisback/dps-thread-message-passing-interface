# import mpi4py
from mpi4py import MPI

# buat COMM
comm = MPI.COMM_WORLD

# dapatkan rank proses
rank = comm.Get_rank()

# dapatkan total proses berjalan
num_procs = comm.Get_size()

# jika saya rank terbesar maka saya akan mengirimkan pesan ke proses yang mempunyai rank 0 s.d rank terbesar-1
if rank == num_procs - 1:
    for i in range(num_procs):
        print(i)
        data = "Hello, Rank " + str(i) + " Rank " + str(num_procs - 1) + " here"
        comm.send(data, dest=i)
# jika saya bukan rank terbesar maka saya akan menerima pesan yang berasal dari proses dengan rank terbesar
else:
    data = comm.recv(source=num_procs - 1)
    print("Pesan yang diterima: " + data)
