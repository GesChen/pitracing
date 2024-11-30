import numpy as np
import random

def rand():
    return random.uniform(0,1)

def length(v):
    return np.linalg.norm(v)
def normalize(v):
    l = length(v)
    if l == 0: return v
    return v / l
def cross(a,b):
    return np.cross(a,b)

def vec2(x,y):
    return np.array([x,y])
def vec3(x,y,z):
    return np.array([x,y,z])
def mat3(a,b,c):
    return np.vstack((a,b,c))
