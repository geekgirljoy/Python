# This algorithm computes a Sigmoid Curve
# Then outputs the computed range
# For more information: https://en.wikipedia.org/wiki/Sigmoid_function

import math;

def sigmoid(t):
    return 1 / (1 + math.exp(-t));

current = -6.0;
max = abs(current);

while current <= max:
    print(sigmoid(current));
    current+=0.1;
