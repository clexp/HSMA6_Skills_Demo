
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Generate random dataset
x = np.random.normal(50, 10, (1000,2))

scaler = MinMaxScaler() # Create scaler object
x_norm = scaler.fit_transform(x) # Normalise the data and store in x_norm

print ("Original Data")
print (x)

print ("Normalised Data")
print (x_norm)

