import numpy as np 
from numpy import genfromtxt
import subprocess

def test_file():
    data_input = np.zeros((20,20))
    data_input[-1,:] = 1
    np.savetxt("brain_sample.csv", data_input, fmt='%d', delimiter=',') #overwrite the brain_sample f ile 

    #run the file 
    subprocess.run(["python", "sagital_brain.py"])

    average_data = genfromtxt('brain_average.csv', delimiter=',') #get the data 

    assert sum(average_data) == 1.0


