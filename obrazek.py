#!/usr/bin/env python3
# Datum:   25.01.2018 12:57
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL
############################################################################
from pylab import imshow, show


data = []

for i in range(64):
    radek = []
    for j in range(64):
        if i < 10 or j < 10:
            radek.append(0)
        else:
            radek.append(1)
    data.append(radek)

imshow(data, interpolation='none', cmap='binary_r')

############################################################################
show()
