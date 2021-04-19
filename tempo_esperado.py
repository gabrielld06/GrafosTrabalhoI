# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 12:46:44 2021

@author: Gabriel
"""

# kruskal e prim
total = 0
n = [250, 500, 750, 1000, 1250, 1500, 1750, 2000]
fon = [1, 4.5, 2.3, 1.8, 1.6, 1.47, 1.38, 1.32]
exectime = 27 # tempo de execução do 250
#7544
for i in range(len(fon)):
    exectime = exectime * fon[i]
    print('{} = {:.0f} segundos == {:.2f} minutos'.format(n[i], exectime, exectime/60))
    total += exectime
print('Tempo total esperado: {:.0f} segundos == {:.0f} minutos'.format(total, total/60))