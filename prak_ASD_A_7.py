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

#.4.#
import re
f = open("KEI.htm","r",encoding="latin1")
teks = f.read()
f.close()
cocok = r'([\w+]+)</a></td>\
<td>\d\.\d\d</td>\
<td>\d\.\d\d</td>\
<td>\d\.\d\d</td>\
<td>([\d.\d\d]+)'
output = re.findall(cocok,teks)
print(output)
