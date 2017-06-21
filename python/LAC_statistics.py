# -*- coding: utf-8 -*-
import numpy as np
import os
#th = float(input('input threshold: '))
th = 0
#dr = input('input directory: ')
#dr = 'G:\csvfiles'
dt = 'LAC'
dr1 = '/media/guitar79/8T/rooknpown/'
dr = dr1+'csv'+dt+'/'

for i in sorted(os.listdir(dr)):
	if i[-4:] == '.csv':
	        f = open(dr+i, 'r').read().split('\n')
	        f = f[1:]
	        f = filter(lambda x: '\t' in x, f)
	        f = np.array(list(map(lambda x: x.split('\t'), f)))
	        f = np.array(list(filter(lambda x: x[1] != 'NaN' and float(x[1]) > th, f)))
	        vsum = np.sum(f[:,1].astype(np.float))
	        vavg = np.mean(f[:,1].astype(np.float))
	        vmed = np.median(f[:,1].astype(np.float))
	        vstd = np.std(f[:,1].astype(np.float))
	        vvar = np.var(f[:,1].astype(np.float))
	        vmax = np.amax(f[:,1].astype(np.float))
	        vmin = np.amin(f[:,1].astype(np.float))
	        with open(dr1+'python_programs/over'+dt+'.txt', 'a') as o:
	            print(i, vsum, vavg, vmed, vstd, vvar, vmax, vmin, file=o)
