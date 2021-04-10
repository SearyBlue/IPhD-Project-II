#!/usr/bin/python3

from matplotlib import pyplot as plt
import numpy as np
import matplotlib

font = {'family' : 'Source Code Pro',
        'size'   : 20}

matplotlib.rc('font', **font)
matplotlib.rcParams['text.usetex'] = True

def rg1(D,J):
    delta = 2 * J**2 /(D - J/2)
    if J * (J + delta) <= 0:
        return 0
    else:
        return J+delta

def rg2(w,D,J):
    delta = -J**2 /(w - D/2 + J/4)
    if J * (J + delta) <= 0:
        return 0
    else:
        return J+delta

#fig,ax = plt.subplots(1,2)
nr = 0
nc = 0
for w in np.arange(-10,10,0.1):
    for J0 in np.arange(0.1,10,0.1):
        J = J0
        Dmax = 20
        x, y = [], []
        N = 100
        den = w - Dmax/2 + J/2
        count = N
        plt.title(r'$\omega={}, D={}, J={}$'.format(w,Dmax,J))
        for D in np.linspace(Dmax,0.1,N):
            x.append(count)
            y.append(J)
            if den * (w - D/2 + J/4) <= 0 and J >= 0.1:
                if np.round(2 * D / J, 3) == 0.413:
                    print (w, J0, 2*D/J)
                    plt.plot(x,y)
                    plt.show()
                break
            den = w - D/2 + J/2
            J = rg2(w, D, J)
            count -= 1
    
#plt.xlabel(r'RG step')
#plt.ylabel(r'$J$')
#plt.tight_layout()
#plt.show()
#plt.savefig('/home/abhirup/IPhD-Project-II/kondo_num/rel2J.png')

#plt.scatter(np.log10(X), np.log10(Y), label="data")
#plt.xlabel(r'$\log_{10}D$')
#plt.ylabel(r'$\log_{10}J^*$')
##plt.legend()
#linear_model=np.polyfit(np.log10(X),np.log10(Y),1)
#linear_model_fn=np.poly1d(linear_model)
#x_s=np.arange(1,7,1)
#plt.plot(x_s,linear_model_fn(x_s),label="best fit", color="green")
#plt.legend()
#plt.show()
    #plt.savefig('match2.png',bbox_inches='tight', transparent="True", pad_inches=0)