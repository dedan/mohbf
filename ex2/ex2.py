

from pypsignifit import *

execfile("data_june_14_2010.py")

n = 10
reversals = adaptive_data[diff(adaptive_data)[1:]*diff(adaptive_data)[:-1] == 0]

n_last = adaptive_data[len(adaptive_data)-n:len(adaptive_data),0]

geo_mean = reduce(lambda x, y : x*y, n_last)**(1./n)
ari_mean = np.sqrt(sum([elem**2 for elem in n_last]))
print ari_mean