#### Nama       : Suriadi Vajrakaruna
#### NPM        : 140810180038
#### Kelas      : B
#### Matkul     : Praktikum Kriptografi (Tugas 2 Nomor 3)
#### Program Shift Chiper

import getpass
import string
def caesar(s, k, decode = False):
   if decode: k = 26 - k
   return s.translate(
       str.maketrans(
           string.ascii_uppercase + string.ascii_lowercase,
           string.ascii_uppercase[k:] + string.ascii_uppercase[:k] +
           string.ascii_lowercase[k:] + string.ascii_lowercase[:k]
           )
       )
msg = getpass.getpass("Masukan Pesan Rahasia: ")
enc = caesar(msg, 20)
print("Pesan Terenkripsi: " + enc)
print("Pesan Terdekripsi: " + caesar(enc, 20, decode = True))