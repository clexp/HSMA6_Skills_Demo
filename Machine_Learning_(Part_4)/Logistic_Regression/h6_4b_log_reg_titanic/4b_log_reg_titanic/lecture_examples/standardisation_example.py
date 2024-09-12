
import numpy as np
from sklearn.preprocessing import StandardScaler

# Generate random dataset
x = np.random.normal(50, 10, (1000, 2))

scaler = StandardScaler() # Create standardisation scaler object
x_stand = scaler.fit_transform(x) # Standardise the data and store in x_stand

