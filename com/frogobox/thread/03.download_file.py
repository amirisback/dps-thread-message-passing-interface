import os
import requests
import threading
import urllib.request, urllib.error, urllib.parse
import time

from com.frogobox.base.config import *

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
        self.__url = url  # Inisiasi alamat file
        self.__byteRange = byteRange  # Inisiasi bytesrange yang akan di download
        self.req = None

    def run(self):
        self.req = urllib.request.Request(self.__url, headers={
            'Range': 'bytes=%s' % self.__byteRange})  # Request download

    def getFileData(self):
        return urllib.request.urlopen(self.req).read()  # Melakukan stream buffer


def main(url=None, splitBy=3):
    print()
    start_time = time.time()  # Catat waktu download
    if not url:
        print("Please Enter some url to begin download.")
        return

    fileName = url.split('/')[
        -1]  # mendapatkan filename

    # Menyimpan ukuran file
    sizeInBytes = requests.head(url, headers={'Accept-Encoding': 'identity'}).headers.get('content-length', None)
    print("%s bytes to download." % sizeInBytes)  # print ukuran file yang di download

    if not sizeInBytes:
        print("Size cannot be determined.")  # Buat handler apabila size tidak ada lalu keluar dari program
        return

    dataLst = []  # Buat variable untuk menampung buffer

    for idx in range(splitBy):
        byteRange = buildRange(int(sizeInBytes), splitBy)[idx]  # Bagi total bytes kedalam 3 range

        bufTh = SplitBufferThreads(url, byteRange)  # Menyimpan buffer file

        bufTh.start()  # Process download file

        bufTh.join()  # Menyatukan buffer proses download pada tiap thread

        dataLst.append(bufTh.getFileData())  # Memasukan buffer yang terpisah 3 menjadi 1 dalam 1 variable penampung

    content = b''.join(dataLst)  # Konversi tipe data buffer

    if dataLst:
        if os.path.exists(fileName):  # Apabila file sudah ada pada target direktori download maka timpa file tersebut
            os.remove(fileName)

        print("--- %s seconds ---" % str(time.time() - start_time))  # tampilkan waktu berjalannya proses downlaod

        # buat string bytes kedalam suatu file dan menghasilkan suatu file baru
        with open(fileName, 'wb') as fh:
            fh.write(content)
        print("Finished Writing file %s" % fileName)


if __name__ == '__main__':
    team_identity()
    print("----------------------------")
    print("DEFAULT : " + URL_IMAGE_DEFAULT)
    print("TELKOM : " + URL_IMAGE_TELKOM)
    main(URL_IMAGE_DEFAULT)
    main(URL_IMAGE_TELKOM)