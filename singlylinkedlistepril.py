class Node:
    def __init__(self, value=None):
        self.value = value                # Menyimpan data di dalam kotak/node
        self.next = None                 # Tali penyambung ke kotak berikutnya

class SLinkedList:
    def __init__(self):
        self.head = None                 # Penunjuk kotak pertama
        self.tail = None                 # Penunjuk kotak terakhir

    def __iter__(self):
        node = self.head                 # Mulai jalan dari kotak pertama
        while node:                      # Selama kotak masih ada
            yield node                   # Berikan data kotak saat ini
            node = node.next             # Geser ke kotak berikutnya

    def insertSLL(self, value, location):
        newNode = Node(value)            # Siapkan kotak baru
        if self.head is None:            # Jika list masih kosong
            self.head = newNode          # Kotak baru jadi yang pertama
            self.tail = newNode          # Kotak baru juga jadi yang terakhir
        else:
            if location == 0:            # Jika mau ditaruh di paling depan (indeks 0)
                newNode.next = self.head # Sambungkan kotak baru ke kepala lama
                self.head = newNode      # Jadikan kotak baru sebagai kepala
            elif location == -1:         # Jika mau ditaruh di paling belakang
                newNode.next = None      # Pastikan ujungnya tidak menunjuk ke mana-mana
                self.tail.next = newNode # Sambungkan ekor lama ke kotak baru
                self.tail = newNode      # Jadikan kotak baru sebagai ekor
            else:                        # Jika mau ditaruh di tengah/posisi tertentu
                tempNode = self.head     # Mulai cari dari depan
                index = 0                # Hitung langkah
                while index < location - 1: # Berhenti satu kotak sebelum lokasi tujuan
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next # Simpan alamat kotak di depannya
                tempNode.next = newNode  # Sambungkan kotak sebelumnya ke kotak baru
                newNode.next = nextNode  # Sambungkan kotak baru ke kotak depannya
                if tempNode == self.tail: # Jika ternyata menyisip tepat di posisi ekor
                    self.tail = newNode  # Update penanda ekor

    def traverseSLL(self):
        if self.head is None:            # Cek jika list kosong
            print("The Singly Linked List does not exist")
        else:
            node = self.head             # Mulai dari depan
            while node is not None:      # Terus jalan sampai ujung
                print(node.value)        # Cetak isi kotak
                node = node.next         # Geser ke kotak depan

    def searchSLL(self, nodeValue):
        if self.head is None:            # Jika list kosong
           return "The list does not exist"
        else:
            node = self.head             # Mulai cari dari depan
            while node is not None:      # Telusuri tiap kotak
                if node.value == nodeValue: # Jika datanya cocok
                    return node.value    # Kembalikan datanya
                node = node.next         # Lanjut cari ke kotak depan
            return "The value does not exist in this list"

    def deleteNode(self, location):
        if self.head is None:            # Jika tidak ada yang bisa dihapus
            print("The SLL does not exist")
        else:
            if location == 0:            # Hapus kotak paling depan
                if self.head == self.tail: # Jika cuma tinggal satu kotak
                    self.head = None     # Kosongkan list
                    self.tail = None
                else:
                    self.head = self.head.next # Pindah kepala ke kotak kedua
            elif location == -1:         # Hapus kotak paling belakang
                if self.head == self.tail: # Jika cuma tinggal satu kotak
                    self.head = None
                    self.tail = None
                else:
                    node = self.head     # Cari dari depan
                    while node is not None:
                        if node.next == self.tail: # Berhenti di sebelum ekor
                            break
                        node = node.next
                    node.next = None     # Putus sambungan ke ekor lama
                    self.tail = node     # Jadikan kotak ini sebagai ekor baru
            else:                        # Hapus kotak di tengah
                tempNode = self.head
                index = 0
                while index < location - 1: # Cari kotak sebelum target hapus
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next # Kotak yang mau dibuang
                tempNode.next = nextNode.next # Sambungkan lompati kotak target

    def deleteEntireSLL(self):
        if self.head is None:            # Jika memang sudah kosong
            print("The SLL does not exist")
        else:
            self.head = None             # Putus akses utama (kepala)
            self.tail = None             # Putus akses ekor

# --- EKSEKUSI ---
singlyLinkedList = SLinkedList()         # Inisialisasi
singlyLinkedList.insertSLL(1, 1)         # Masuk angka 1 (head & tail)
singlyLinkedList.insertSLL(2, 1)         # Sisip angka 2 setelah angka 1
singlyLinkedList.insertSLL(3, 1)         # Sisip angka 3 setelah angka 1
singlyLinkedList.insertSLL(4, 1)         # Sisip angka 4 setelah angka 1
singlyLinkedList.insertSLL(5, -1)        # Tambah angka 5 di paling akhir

print([node.value for node in singlyLinkedList]) # Tampilkan hasil akhir

"""
OUTPUT:
[1, 4, 3, 2, 5]
"""