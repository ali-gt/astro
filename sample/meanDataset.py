import numpy as np

def mean_datasets(filenames):
  n = len(filenames)
  if n > 0:
    data = np.loadtxt(filenames[0], delimiter=',')
    for i in range(1,n):
      data += np.loadtxt(filenames[i], delimiter=',')
    
    # Mean across all files:
    data_mean = data/n
     
    return np.round(data_mean, 1)

