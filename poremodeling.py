import numpy as np
import random
# get the index of each pore
pore_index = np.arange(125).reshape(5,5,5)
print pore_index

# get random radius of each pore
pore_radius = np.random.rand(125).reshape(5,5,5)


pore_cn = np.empty(pore_index.shape, dtype='uint16')

# find the connected number of each pore
for i in range(5):
    for j in range(5):
        for k in range(5):
            if i==0 or i==4:
                pore_cn[i, j, k] = 5
            elif j == 0 or j == 4:
                pore_cn[i, j, k] = 5
            elif k ==0 or k ==4 :
                pore_cn[i, j, k] = 5
            else:
                pore_cn[i, j, k] = 6
for i in range(5):
    pore_cn[i, 0, 0] = 4
    pore_cn[i, 0, 4] = 4
    pore_cn[i, 4, 0] = 4
    pore_cn[i, 4, 4] = 4
for j in range(5):
    pore_cn[0, j, 0] = 4
    pore_cn[0, j, 4] = 4
    pore_cn[4, j, 0] = 4
    pore_cn[4, j, 4] = 4
for k in range(5):
    pore_cn[0, 0, k] = 4
    pore_cn[0, 4, k] = 4
    pore_cn[4, 4, k] = 4
    pore_cn[4, 0, k] = 4
for i in range(0,5,4):
    for j in range(0, 5, 4):
        for k in range(0, 5, 4):
            pore_cn[i,j,k] = 3


# find the connected pores' index
pore_ci = []
for i in range(5):
    for j in range(5):
        for k in range(5):
            if i != 4:
                pore_ci.append(pore_index[i+1, j, k])
            else:
                # -1 represent outlet
                pore_ci.append(-1)
            if i != 0:
                pore_ci.append(pore_index[i-1, j, k])
            else:
                # -2 represent inlet
                pore_ci.append(-2)
            if j != 4:
                pore_ci.append(pore_index[i, j+1, k])
            else:
                pore_ci.append(-3)
            if j != 0:
                pore_ci.append(pore_index[i, j-1, k])
            else:
                pore_ci.append(-3)
            if k !=4:
                pore_ci.append(pore_index[i, j, k+1])
            else:
                pore_ci.append(-3)
            if k !=0:
                pore_ci.append(pore_index[i, j, k-1])
            else:
                pore_ci.append(-3)

pore_cia= np.asarray(pore_ci).reshape(5,5,5,6)
print 'pore connectd index is', pore_ci


# create a list for the index of throat.
# this index is corresponding to the connected pore index
# the negative value means there is no link.
n=1
link_index=[]
for i in range(len(pore_ci)):
    if pore_ci[i] >= 0:
        link_index.append(n)
        n=n+1
    else:
        link_index.append(pore_ci[i])

print 'link_index is ' , link_index

# pore 1 index for link1 dat file
pore_1_index=[]
for i in range(len(link_index)):
    if link_index[i] > 0:
        pore_1_index.append(i/6)

print 'pore_1_index is ', pore_1_index

# pore 2 index for link1 dat file
pore_2_index = []
for i in range(len(link_index)):
    if link_index[i] > 0:
        pore_2_index.append(pore_ci[i])

print 'pore_2_index is',pore_2_index

# throat radius
link_r = np.random.rand(len(pore_1_index))
print len(link_r)








