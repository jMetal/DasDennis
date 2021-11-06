import numpy as np

H = 5
m = 4

# FIRST LEVEL

first_level = np.linspace(0,1,H+1).tolist()
print("First level: " + str(first_level))
step_size = 1 / H
print("Step size: " + str(step_size))

for i in range(0, H+1):
    print (i * step_size )

print([i*step_size for i in range(0,H+1)])