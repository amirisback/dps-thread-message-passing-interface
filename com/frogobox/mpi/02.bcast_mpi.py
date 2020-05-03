# import mpi4py
from mpi4py import MPI

# buat COMM

BROADCAST_MESSAGE = "Hello, rank 0 disini, mengirim ke semua rank"


def team_identity():
    amir = "Muhammad Faisal Amir (1301198497)"
    cika = "Friskadini Ismayanti (1301198496)"
    ridho = "Ridho Maulana Cahyudi (1301198515)"
    print(cika)
    print(amir)
    print(ridho)


def broadcast_receive_message(rank, data):
    return "Pesan yang diterima pada rank " + str(rank) + ": " + data


comm = MPI.COMM_WORLD

# dapatkan rank proses
rank = comm.Get_rank()

# dapatkan total proses berjalan
num_procs = comm.Get_size()

# jika saya rank 0 maka saya akan melakukan broadscast
if rank == 0:
    comm.bcast(BROADCAST_MESSAGE, root=0)
# jika saya bukan rank 0 maka saya menerima pesan
else:
    data = comm.bcast(None, root=0)
    print(broadcast_receive_message(rank, data))

# How To Run
# mpiexec -n 5 python 02.bcast_mpi.py
