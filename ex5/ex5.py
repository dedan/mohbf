
#Write a function that simulates a signal detection experiment for an observer that follows the assumptions of the high threshold model.


# S is what we present
# X is the internal variable
# R is the response

# S == 0 ==> X = 0
# S == 1 ==> (certain P) X = 1
# X == 1 ==> R = 1
# X == 0 can guess R = 1

import numpy as np
import pylab as pl



def experiment(p,gr, n_trials, n_noise_trials):
    """docstring for experiment"""
    
    s = np.ones(n_trials)
    s[0:n_noise_trials] = 0
    x       = np.zeros(n_trials)
    r       = np.zeros(n_trials)
    rand4p  = np.random.rand(n_trials)
    rand4gr = np.random.rand(n_trials)
    x[s == 1 & (rand4p < p)]    = 1
    r[x == 1 | (rand4gr < gr)]  = 1
    p_hit   = np.sum(r)/float(np.sum(s))
    p_fa    = np.sum((r ==1 & s == 0))/float(n_noise_trials)
    return (p_fa, p_hit)
    
if __name__ == "__main__":
    n_trials    = 600
    n_noise_trials = 300
    ps = [0.3, 0.5, 0.8]
    grs = [0.01, 0.1, 0.2, 0.3, 0.6, 0.7, 0.9] 
    
    for i, p in enumerate(ps):
        pl.figure(i)
        for gr in grs:
            (p_fa, p_hit) = experiment(p,gr,n_trials,n_noise_trials)
            pl.plot(p_fa, p_hit, '.')
            print (p_fa, p_hit)
    pl.show()
    