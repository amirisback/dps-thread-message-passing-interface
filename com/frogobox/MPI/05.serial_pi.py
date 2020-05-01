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

import time


def Pi(num_steps):
    start = time.time()
    step = 1.0 / num_steps
    sum = 0
    for i in range(num_steps):
        x = (i + 0.5) * step
        sum = sum + 4.0 / (1.0 + x * x)
    pi = step * sum
    end = time.time()
    print("Pi with %d steps is %f in %f secs" % (num_steps, pi, end - start))


if __name__ == '__main__':
    Pi(100000)
