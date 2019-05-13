#Nama : sugiyo
#NIM :l200170002
#Kelas : A
#LAPORAN PRAKTIKUM ALGORITMA STRUKTUR DATA
#.1.#
import re
f = open('indonesia.txt', 'r', encoding='latin1')
teks = f.read()
f.close()
p = r'me[\w]+'
tupple = re.findall(p, teks)
print(tupple,'\n')

#.2.#
f = open('indonesia.txt', 'r', encoding='latin1')
teks = f.read()
f.close()
p = r'di[\w]+'
tupple = re.findall(p, teks)
print(tupple,'\n')

#.3.#
f = open('indonesia.txt', 'r', encoding='latin1')
teks = f.read()
f.close()
p = r'di [\w]+'
tupple = re.findall(p, teks)
print(tupple,'\n')

#.4A.#

f = open('KEI.html', 'r', encoding = 'latin1')
teks = f.read()
f.close()
pola = r'(\w+)</a></td>'
tampil = re.findall(pola,teks)
print(tampil)

pola = r'(\d+)</a></td><td>'
tampil = re.findall(pola,teks)
print(tampil)

#.4B.#
f = open('KEI.html','r', encoding='latin1')
teks = f.read()
f.close()
tampil = re.findall(r'title="([\w+]+)">',teks)
tampil = re.findall(r'">([\w+]+)</a></td>\n<td>([0-9.]+)</td>',teks)
a = []
for i in tampil :
    a.append((i[0], float(i[1])))
print(a)