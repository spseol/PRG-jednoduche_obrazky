#!/usr/bin/env python3
# Datum:   25.01.2018 12:57
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL
############################################################################
from pylab import imshow, show, figure


data = [[1, 2, 3, 4],
        [5, 6, 7, 8]]

figure()
imshow(data)

figure()
imshow(data, interpolation='none', cmap='binary')

figure()
imshow(data, interpolation='none', cmap='binary_r')

############################################################################
show()
