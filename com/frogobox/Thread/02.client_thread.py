# import socket dan sys
import socket
import sys


# fungsi utama
def main():
    # buat socket bertipe TCP
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # tentukan IP server target
    host = "127.0.0.1"

    # tentukan por server
    port = 8000

    # lakukan koneksi ke server
    try:
        soc.connect((host, port))
    except:
        # print error
        print("Koneksi error")
        # exit
        sys.exit()

    # tampilkan menu, enter quit to exit
    print("Masukkan 'quit' untuk keluar")
    message = input(" -> ")

    # selama pesan bukan "quit", lakukan loop forever
    while message != 'quit':
        # kirimkan pesan yang ditulis ke server
        soc.sendall(message.encode("utf8"))
        if soc.recv(5120).decode("utf8") == "-":
            pass  # null operation

        # menu (user interface)
        message = input(" -> ")

    # send "quit" ke server
    soc.send(b'--quit--')


# panggil fungsi utama
if __name__ == "__main__":
    main()
