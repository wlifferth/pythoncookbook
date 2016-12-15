s = 'pýtĥöñ\fis\tawesome\r\n'

print(s)
remap = {
        ord('\t'): ' ',
        ord('\f'): ' ',
        ord('\r'): None
        }
a = s.translate(remap)
print(a)

import unicodedata
import sys
cmb_chars = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))
b = unicodedata.normalize('NFD', a)
print(b)
print(b.translate(cmb_chars))

digitmap = {c: ord('0') + unicodedata.digit(chr(c)) for c in range(sys.maxunicode) if unicodedata.category(chr(c)) == 'Nd' }

print(digitmap)
print(len(digitmap))

x = '\u0661\u0662\u0663'
print(x.translate(digitmap))
