# Determine Andromeda location in ra/dec degrees

# from wikipedia
ra = '00:42:44.3'
dec = '41:16:09'

# convert to decimal degrees
from math import *

# .split method splits a string into a list, ':' specifies to split using colons
d, m, s = dec.split(':')
dec = int(d)+int(m)/60+float(s)/3600

h, m, s = ra.split(':')
ra = 15*(int(h)+int(m)/60+float(s)/3600)

# account for correction in ra 
# this is due to the error introduced from projecting a 3D plane onto a 2D plane.
# the higher the object is up to <90 deg in dec or the lower it is down to <-90 deg, the greater the correction required
# this is because the width of the grids will get narrower and narrower the further away from the equator
# no corrections required when dec = 0 or 90 deg 
ra = ra/cos(dec*pi/180)

nsrc = 1_000_000

# make 1000 stars within 1 degree of Andromeda
from random import *
ras = []
decs = []
for i in range(nsrc):
    ras.append(ra + uniform(-1,1))
    decs.append(dec + uniform(-1,1))


# now write these to a csv file for use by my other program
f = open('catalog.csv','w')
print("id,ra,dec", file=f)
for i in range(nsrc):
    print("{0:07d}, {1:12f}, {2:12f}".format(i, ras[i], decs[i]), file=f)

