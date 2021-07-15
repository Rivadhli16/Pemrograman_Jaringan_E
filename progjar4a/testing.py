from file_client_cli import remote_get
import time
import datetime
import threading
import socket

def kirim_semua():
    texec = dict()
    daftar = 'pokijan.jpg'

    catatan_start = datetime.datetime.now()
    for k in range(100):
        print(f"mengirim {k}")
        texec[k] = threading.Thread(target=remote_get, args=(daftar,))
        texec[k].start()
        
    for k in range(100):
        texec[k].join()

    catatan_end = datetime.datetime.now()
    selesai = catatan_end - catatan_start
    print(f"TOTAL waktu yang dibutuhkan yaitu {selesai} detik {catatan_start} sampai {catatan_end}")

if __name__=='__main__':
    kirim_semua()