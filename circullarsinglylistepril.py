class Node:
    def __init__(self, value=None):
        self.value = value                # Isi data di dalam kotak/gerbong
        self.next = None                 # Tali penyambung ke gerbong berikutnya

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None                 # Penanda gerbong pertama
        self.tail = None                 # Penanda gerbong terakhir

    def __iter__(self):
        node = self.head                 # Mulai dari gerbong depan
        while node:
            yield node                   # Ambil data gerbong saat ini
            if node.next == self.head:   # Kalau tali berikutnya balik ke depan, berhenti
                break
            node = node.next             # Pindah ke gerbong berikutnya

    def createCSLL(self, nodeValue):
        node = Node(nodeValue)           # Bikin satu gerbong baru
        node.next = node                 # Talinya mengikat ke dirinya sendiri (melingkar)
        self.head = node                 # Gerbong ini jadi yang pertama
        self.tail = node                 # Gerbong ini juga jadi yang terakhir
        return "List dibuat"

    def insertCSLL(self, value, location):
        if self.head is None:            # Jika belum ada gerbong sama sekali
            return "List kosong"
        
        newNode = Node(value)            # Bikin gerbong baru
        if location == 0:                # Jika mau ditaruh paling depan
            newNode.next = self.head     # Sambungkan ke gerbong pertama lama
            self.head = newNode          # Jadikan dia gerbong pertama baru
            self.tail.next = newNode     # Gerbong terakhir ikat ke dia agar tetap melingkar
        elif location == 1:              # Jika mau ditaruh paling belakang
            newNode.next = self.tail.next # Sambungkan gerbong baru ke depan
            self.tail.next = newNode     # Gerbong terakhir lama sambung ke yang baru
            self.tail = newNode          # Jadikan dia gerbong terakhir baru
        else:                            # Jika mau disisipkan di tengah
            tempNode = self.head
            index = 0
            while index < location - 1:  # Cari posisi gerbong sebelum tempat sisip
                tempNode = tempNode.next
                index += 1
            newNode.next = tempNode.next # Gerbong baru sambung ke gerbong depannya
            tempNode.next = newNode      # Gerbong sebelumnya sambung ke yang baru
        return "Node berhasil masuk"

    def traversalCSLL(self):
        if self.head is None:
            print("Tidak ada gerbong")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)    # Intip isi gerbong
                if tempNode.next == self.head: # Jika sudah kembali ke awal, stop
                    break
                tempNode = tempNode.next

    def searchCSLL(self, nodeValue):
        if self.head is None:
            return "List kosong"
        tempNode = self.head
        while tempNode:
            if tempNode.value == nodeValue: # Jika datanya cocok
                return tempNode.value
            if tempNode.next == self.head:  # Jika sudah muter sampai akhir tetap tidak ada
                break
            tempNode = tempNode.next
        return "Data tidak ketemu"

    def deleteNode(self, location):
        if self.head is None:
            return "List kosong"
        if location == 0:                # Hapus gerbong paling depan
            if self.head == self.tail:   # Jika cuma tinggal satu gerbong
                self.head.next = None
                self.head = self.tail = None
            else:
                self.head = self.head.next # Gerbong kedua naik jadi yang pertama
                self.tail.next = self.head # Gerbong terakhir ikat ke yang pertama baru
        elif location == 1:              # Hapus gerbong paling belakang
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                node = self.head
                while node.next != self.tail: # Cari gerbong sebelum gerbong terakhir
                    node = node.next
                node.next = self.head    # Sambungkan langsung ke depan
                self.tail = node         # Jadikan gerbong ini yang terakhir
        else:                            # Hapus gerbong di tengah
            tempNode = self.head
            index = 0
            while index < location - 1:  # Cari gerbong sebelum yang mau dihapus
                tempNode = tempNode.next
                index += 1
            tempNode.next = tempNode.next.next # "Lompati" gerbong yang mau dihapus
        return "Node berhasil dihapus"

    def deleteEntireCSLL(self):
        self.head = None                 # Buang penanda gerbong pertama
        if self.tail:
            self.tail.next = None        # Putus tali melingkarnya
            self.tail = None             # Buang penanda gerbong terakhir

# --- CONTOH JALANNYA KODE ---
listMelingkar = CircularSinglyLinkedList()
listMelingkar.createCSLL(0)              # Bikin gerbong 0
listMelingkar.insertCSLL(1, 1)           # Tambah gerbong 1 di belakang
listMelingkar.insertCSLL(2, 1)           # Tambah gerbong 2 di belakang
listMelingkar.insertCSLL(3, 1)           # Tambah gerbong 3 di belakang

print([node.value for node in listMelingkar]) # Tampilkan semua gerbong
listMelingkar.deleteEntireCSLL()         # Hapus semua gerbong
print([node.value for node in listMelingkar]) # Tampilkan lagi (hasilnya kosong)

"""
OUTPUT:
[0, 1, 2, 3]
[]
"""