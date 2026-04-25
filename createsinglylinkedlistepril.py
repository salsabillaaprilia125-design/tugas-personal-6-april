class Node:
    def __init__(self, value=None):
        self.value = value                # Isi data gerbong
        self.next = None                 # Sambungan ke gerbong berikutnya

class SLinkedList:
    def __init__(self):
        self.head = None                 # Kepala (awal) list
        self.tail = None                 # Ekor (akhir) list

    def __iter__(self):
        node = self.head                 # Mulai dari kepala
        while node:                      # Selama masih ada gerbong
            yield node                   # Ambil datanya
            node = node.next             # Geser ke sambungan berikutnya

    def insertSLL(self, value, location):
        newNode = Node(value)            # Bikin gerbong baru
        if self.head is None:            # Jika list masih kosong
            self.head = newNode          # Set jadi kepala
            self.tail = newNode          # Set jadi ekor
        else:
            if location == 0:            # Jika mau ditaruh di paling depan
                newNode.next = self.head # Sambungkan baru ke kepala lama
                self.head = newNode      # Ganti kepala lama dengan yang baru
            elif location == 1:          # Jika mau ditaruh di paling belakang
                newNode.next = None      # Akhiri sambungan
                self.tail.next = newNode # Sambungkan ekor lama ke baru
                self.tail = newNode      # Ganti ekor lama dengan yang baru
            else:                        # Jika mau disisipkan di tengah
                tempNode = self.head     # Cari dari kepala
                index = 0                # Mulai hitung
                while index < location - 1: # Cari posisi sebelum titik sisip
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next # Simpan gerbong depan
                tempNode.next = newNode  # Gerbong sebelum sambungkan ke baru
                newNode.next = nextNode  # Gerbong baru sambungkan ke depan

    def traverseList(self):
        if self.head is None:            # Jika list kosong
            print("SLL tidak ada")
        else:
            node = self.head
            while node is not None:
                print(node.value)        # Intip isi tiap gerbong
                node = node.next

    def searchSLL(self, nodeValue):
        if self.head is None:            # Jika list kosong
            print("SLL tidak ada")
        else:
            node = self.head
            while node is not None:
                if node.value == nodeValue: # Jika isi ketemu
                    return node.value
                node = node.next
            return "Node tidak ketemu"

    def deleteNode(self, location):
        if self.head is None:            # Jika list kosong
            return "SLL tidak ada"
        else:
            if location == 0:            # Hapus paling depan
                if self.head == self.tail: # Jika cuma tinggal satu gerbong
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next # Kepala pindah ke gerbong kedua
            elif location == 1:          # Hapus paling belakang
                if self.head == self.tail: # Jika cuma tinggal satu
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail: # Cari satu gerbong sebelum ekor
                            break
                        node = node.next
                    node.next = None     # Putus sambungan ke ekor
                    self.tail = node     # Gerbong ini jadi ekor baru
            else:                        # Hapus gerbong di tengah
                tempNode = self.head
                index = 0
                while index < location-1: # Cari gerbong sebelum target
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next # Target yang mau dihapus
                tempNode.next = nextNode.next # "Lompati" targetnya

    def deleteEntireSLL(self):
        if self.head is None:            # Jika sudah kosong
            print("SLL tidak ada")
        else:
            self.head = None             # Putus akses kepala
            self.tail = None             # Putus akses ekor

# --- EKSEKUSI ---
singlyLinkedList = SLinkedList()         # Buat list baru
singlyLinkedList.insertSLL(44,6)         # Masukkan 44 (otomatis jadi head)
print([node.value for node in singlyLinkedList]) 

singlyLinkedList.insertSLL(3,1)          # Masukkan 3 di akhir
singlyLinkedList.insertSLL(4,1)          # Masukkan 4 di akhir
print([node.value for node in singlyLinkedList]) 

singlyLinkedList.insertSLL(5,3)          # Masukkan 5 di lokasi indeks ke-3
print([node.value for node in singlyLinkedList]) 

"""
OUTPUT:
[44]
[44, 3, 4]
[44, 3, 4, 5]
"""