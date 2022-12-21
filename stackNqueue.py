#STACK
tumpukan = [1,2,3,4,5,6]
print('data sekarang: ',tumpukan)

#memasukkan data baru
tumpukan.append(7)
print('data masuk: ',7)
print('data sekarang: ',tumpukan)
tumpukan.append(8)
print('data masuk: ',8)
print('data sekarang: ',tumpukan)

out = tumpukan.pop()
print('data keluar: ',out)
print('data sekarang: ',tumpukan)

#QUEUE
from collections import deque

antrian = deque([1,2,3,4,5])

print('data sekarang: ',antrian)

# menambahkan data
antrian.append(6)
print('data masuk: ',6)
print('data sekarang: ',antrian)

antrian.append(7)
print('data masuk: ',7)
print('data sekarang: ',antrian)

#mengurangi antrian
out = antrian.popleft()
print('data keluar: ',out)
print('data sekarang: ',antrian)

out = antrian.popleft()
print('data keluar: ',out)
print('data sekarang: ',antrian)

out = antrian.popleft()
print('data keluar: ',out)
print('data sekarang: ',antrian)

out = antrian.popleft()
print('data keluar: ',out)
print('data sekarang: ',antrian)