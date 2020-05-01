# import socket, sys, traceback dan threading
import socket
import sys
import traceback
from threading import Thread


# jalankan server
def main():
    start_server()


# fungsi saat server dijalankan
def start_server():
    # tentukan IP server
    host = "127.0.0.1"

    # tentukan port server
    port = 8000  # arbitrary non-privileged port

    # buat socket bertipe TCP
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # option socket
    soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print("Socket dibuat")

    # lakukan bind
    try:
        soc.bind((host, port))
    except:
        # exit pada saat error
        print("Bind gagal. Error : " + str(sys.exc_info()))
        sys.exit()

    # listen hingga 5 antrian
    soc.listen(5)

    print("Socket mendengarkan")

    # infinite loop, jangan reset setiap ada request
    while True:
        # terima koneksi
        connection, address = soc.accept()

        # dapatkan IP dan port
        ip, port = str(address[0]), str(address[1])

        print("Connected dengan " + ip + ":" + port)

        # jalankan thread untuk setiap koneksi yang terhubung
        try:
            Thread(target=client_thread, args=(connection, ip, port)).start()
        except:
            # print kesalahan jika thread tidak berhasil dijalankan
            print("Thread tidak berjalan.")
            traceback.print_exc()

    # tutup socket
    soc.close()


def client_thread(connection, ip, port, max_buffer_size=4096):
    # flag koneksi
    is_active = True

    # selama koneksi aktif
    while is_active:

        # terima pesan dari client
        client_input = connection.recv(max_buffer_size)

        # dapatkan ukuran pesan
        client_input_size = sys.getsizeof(client_input)

        # print jika pesan terlalu besar
        if client_input_size > max_buffer_size:
            print("Size terlalu besar {}".format(client_input_size))

        # dapatkan pesan setelah didecode
        decoded_input = client_input.decode("utf8")
        print("Pesan: " + decoded_input)

        # jika "quit" maka flag koneksi = false, matikan koneksi
        if "quit" in decoded_input:
            # ubah flag
            is_active = False

            print("Client meminta keluar")

            # matikan koneksi
            connection.close()

            print("Connection " + ip + ":" + port + " ditutup")

        else:
            # tampilkan pesan dari client
            print("Processed result: {}".format(decoded_input))
            connection.sendall("-".encode("utf8"))


# panggil fungsi utama
if __name__ == "__main__":
    main()
