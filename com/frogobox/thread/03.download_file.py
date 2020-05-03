import os
import requests
import threading
import urllib.request, urllib.error, urllib.parse
import time

url = "https://apod.nasa.gov/apod/image/1901/LOmbradellaTerraFinazzi.jpg"

"""
    Fungsi untuk membagi range dari total bytes yang akan di download
    (1024 bytes akan di bagi menjadi 2) maka fungsi mengembalikan 512 [1024/2]
"""


def buildRange(value, numsplits):
    lst = []
    for i in range(numsplits):
        if i == 0:
            lst.append('%s-%s' % (i, int(round(1 + i * value / (numsplits * 1.0) + value / (numsplits * 1.0) - 1, 0))))
        else:
            lst.append('%s-%s' % (int(round(1 + i * value / (numsplits * 1.0), 0)),
                                  int(round(1 + i * value / (numsplits * 1.0) + value / (numsplits * 1.0) - 1, 0))))
    return lst


""" Splits the buffer to ny number of threads
    thereby, concurrently downloading through
    ny number of threads.
"""


class SplitBufferThreads(threading.Thread):
    def __init__(self, url, byteRange):
        super(SplitBufferThreads, self).__init__()
        # Inisiasi string url file yg akan di download
        self.__url = url
        # Inisiasi bytesrange yang akan di download
        self.__byteRange = byteRange
        self.req = None

    def run(self):
        # Melakukan request download pada suatu bytesrange
        self.req = urllib.request.Request(self.__url, headers={'Range': 'bytes=%s' % self.__byteRange})

    def getFileData(self):
        # Melakukan stream buffer pada url target
        return urllib.request.urlopen(self.req).read()


def main(url=None, splitBy=3):
    # Catat waktu mulai download
    start_time = time.time()
    if not url:
        print("Please Enter some url to begin download.")
        return

    # Mengambil filename dengan cara mengambil suffix terakhir dari string url dengan delimiter '/'
    fileName = url.split('/')[-1]

    # Menyimpan ukuran file kedalam suatu variable
    sizeInBytes = requests.head(url, headers={'Accept-Encoding': 'identity'}).headers.get('content-length', None)

    # Tampilkan ukuran bytes ke monitor
    print("%s bytes to download." % sizeInBytes)

    # Buat handler apabila size tidak ada lalu keluar dari program
    if not sizeInBytes:
        print("Size cannot be determined.")
        return

    # Buat variable untuk menampung buffer yang akan di split saat proses download dengan threading dilakukan
    dataLst = []

    for idx in range(splitBy):
        # Bagi total bytes kedalam 3 range
        byteRange = buildRange(int(sizeInBytes), splitBy)[idx]

        # Menyimpan buffer file yang sedang di download pada suatu variable untuk nanti digabungkan
        bufTh = SplitBufferThreads(url, byteRange)

        # Process download file (dalam buffer) dimulai
        bufTh.start()

        # Menyatukan buffer proese download pada tiap thread
        bufTh.join()

        # Memasukan buffer yang terpisah 3 menjadi 1 dalam 1 variable penampung
        dataLst.append(bufTh.getFileData())

    # Konversi tipe data buffer string menjadi byte dengan menambahkan prefix b (bytes)
    content = b''.join(dataLst)

    if dataLst:
        # Apabila file sudah ada pada target direktori download maka timpa file tersebut
        if os.path.exists(fileName):
            os.remove(fileName)

        # Catat waktu selesai, lalu tampilkan waktu berjalannya proses downlaod
        print("--- %s seconds ---" % str(time.time() - start_time))

        # Tulis string bytes kedalam suatu file, lalu akan dihasilkan suatu file baru
        with open(fileName, 'wb') as fh:
            fh.write(content)
        print("Finished Writing file %s" % fileName)


if __name__ == '__main__':
    main(url)
