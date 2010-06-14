
from pypsignifit import *
dir()
nafc = 2
stimulus_intensities = [0.0,2.0,4.0,6.0,8.0,10.0]
number_of_correct = [34,32,40,48,50,48]
number_of_trials  = [50]*len(stimulus_intensities)
data = zip(stimulus_intensities,number_of_correct,number_of_trials)

constraints = ( 'unconstrained', 'unconstrained', 'Uniform(0,0.1)' )

