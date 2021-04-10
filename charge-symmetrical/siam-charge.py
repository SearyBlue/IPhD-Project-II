#!/bin/python


import itertools
from math import sqrt

import matplotlib
import numpy as np
from matplotlib import pyplot as plt

font = {'family' : 'Source Code Pro',
        'size'   : 15}

matplotlib.rc('font', **font)
matplotlib.rcParams['text.usetex'] = True


def den(w, D, U, K):
    ''' Defines and evaluates all the
    denominators in the problem.'''

    d1 = w - 0.5 * D + U/2
    d2 = w - 0.5 * D - U/2 + K/4
    d3 = w - 0.5 * D + K/8

    return d1, d2, d3


def rg(w, D, U, V, K):
    '''Evaluates the change in each coupling 
    at a particular RG step.'''

    dens = den(w, D, U, K)

    deltaU = 4 * V**2 * (1/dens[0] - 1/dens[1]) + (3 * K**2 / 4) * D * (1 / dens[2])
    deltaV = (-3/8) * K * V * (1/dens[0] + 1/dens[2])
    deltaK = -K**4 * 1/dens[2]

    U = 0 if (U + deltaU) * U <= 0 else U + deltaU
    V = 0 if (V + deltaV) * V <= 0 else V + deltaV
    K = 0 if (K + deltaK) * K <= 0 else K + deltaK

    return U, V, K


def all_flow():
    '''master function to call other functions'''
    for Dmax in [10]:
        for U in [1]:
            w = -Dmax/5
            N = 10*Dmax
            V = 1
            K = Dmax/2
            plt.title(r'Bare values: $V={}, K = Dmax/2, U={}, \omega=-Dmax/5$'.format(V, U))
            old_den = den(w, Dmax, U, K)[2]
            flag = False
            X = []
            Y = []
            Z = []
            step = N
            for D in np.linspace(Dmax, 0, N):
                X.append(step)
                Y.append(K)
                Z.append(U)
                new_den = den(w, D, U, K)[2]
                if old_den * new_den <= 0: 
                    break
                old_den = new_den

                U, V, K = rg(w, D, U, V, K)
                step -= 1
            x.append(np.log10(Dmax))
            y.append(np.log10(K))
            #ax.plot(X, Y, color='brown')
            #ax.set_xlabel(r'$\leftarrow$ RG steps')
            #ax.set_ylabel(r'$K$', color='brown')
            #ax2.plot(X, Z, color='blue')
            #ax2.set_ylabel(r'$\epsilon_d$', color='blue')
            #ax.scatter(X[0], Y[0], color='black', label="start")
            #ax.scatter(X[-1], Y[-1], color='g', label="end")
            #ax.legend()
            #plt.show()

fig, ax = plt.subplots()
#ax2 = ax.twinx()
x, y = [], []
all_flow()
plt.scatter(x, y, label="fixed points")
plt.xlabel(r'$\log_{10}D$')
plt.ylabel(r'$\log_{10}K^*$')
linear_model=np.polyfit(x,y,1)
linear_model_fn=np.poly1d(linear_model)
x_s=np.arange(1,7,1)
plt.plot(x_s,linear_model_fn(x_s),label="best fit", color="green")
plt.legend()
plt.show()