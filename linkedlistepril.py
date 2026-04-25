from random import randint

class Node:
    def __init__(self, value=None):
        self.value = value                # Isi data pada node
        self.next = None                 # Penunjuk ke node selanjutnya
        self.prev = None                 # Penunjuk ke node sebelumnya (opsional)
    
    def __str__(self):
        return str(self.value)           # Mengubah nilai node menjadi string saat dipanggil

class LinkedList:
    def __init__(self, values = None):
        self.head = None                 # Inisialisasi awal kepala list
        self.tail = None                 # Inisialisasi awal ekor list

    def __iter__(self):
        curNode = self.head              # Mulai iterasi dari head
        while curNode:                   # Selama node tidak None
            yield curNode                # Mengembalikan node satu per satu
            curNode = curNode.next       # Geser ke node berikutnya
    
    def __str__(self):
        values = [str(x.value) for x in self] # Mengambil semua nilai node ke dalam list
        return ' -> '.join(values)       # Menggabungkan nilai dengan simbol panah
    
    def __len__(self):
        result = 0                       # Counter untuk menghitung jumlah node
        node = self.head                 # Mulai dari head
        while node:                      # Selama node tersedia
            result += 1                  # Tambah hitungan
            node = node.next             # Geser ke node berikutnya
        return result                    # Mengembalikan total panjang list
    
    def add(self, value):
        if self.head is None:            # Jika list masih kosong
            newNode = Node(value)        # Buat node baru
            self.head = newNode          # Node baru jadi head
            self.tail = newNode          # Node baru juga jadi tail
        else:                            # Jika list sudah ada isinya
            self.tail.next = Node(value) # Ekor lama menunjuk ke node baru
            self.tail = self.tail.next   # Update tail ke node yang baru dibuat
        return self.tail                 # Mengembalikan posisi ekor terbaru
    
    def generate(self, n, min_value, max_value):
        self.head = None                 # Reset head untuk generate baru
        self.tail = None                 # Reset tail untuk generate baru
        for i in range(n):               # Looping sebanyak n kali
            self.add(randint(min_value,max_value)) # Tambah angka acak ke list
        return self                      # Mengembalikan objek list utuh

# --- EKSEKUSI ---
customLL = LinkedList()                  # Membuat objek LinkedList
customLL.generate(10, 0, 99)             # Generate 10 angka acak (0-99)
print(customLL)                          # Mencetak visualisasi list
print(len(customLL))                     # Mencetak panjang list

"""
OUTPUT:
0 -> 2 -> 99 -> 19 -> 88 -> 4 -> 21 -> 56 -> 67 -> 83
10
"""