import numpy as np
import random

FILE_PATH = "data/generated_data.csv"
random.seed(27)
np.random.seed(27)

# w: Robot speed/velocity (optimized parameter)
# x: Leg 1 pulse width
# y: Leg 2 pulse width
# z: Waveform offset

# Sample 4D paraboloid
w = lambda x, y, z: -(((x-200)**2 + (y-150)**2 + (z-25)**2)) + 20 + random.randint(-10, 10)*0.01  # Vertex at (200, 150, 25) give or take

mean = np.array([200, 150, 25]) # Vertex
std = np.array([70, 70, 70])    # Std deviation

inputs = np.random.normal(loc=mean, scale=std, size=(500, 3))   # 500 random datapoints from the normal distibution (more points around the vertex)
inputs = np.clip(inputs, 0, 500).astype(int)    # Constrain between 0–500 because Gaussian can go outside range

outputs = np.expand_dims(a=w(inputs[:, 0],inputs[:, 1], inputs[:, 2]), axis=1)

data = np.concatenate((inputs, outputs), axis=1)

print("==========DATA==========")
print(data)

with open(FILE_PATH, "wb") as f:
    np.savetxt(f, data, delimiter=",")
    print(f"Saved to {FILE_PATH}")
