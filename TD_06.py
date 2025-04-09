from random import randint
N = 10
L_orig = [{0:randint(10, 1000), 1:i} for i in range(N)]
L = L_orig.copy() # pareil que L = [L_orig[i] for i in range(len(L_orig))]
