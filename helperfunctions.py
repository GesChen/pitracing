from consts import *
from structs import *
import numpy as np
from numpy import sin, cos, tan
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
def dot(a,b):
    return np.dot(a,b)
def sqrt(x):
    return np.sqrt(x)
def sign(x):
    return np.sign(x)

def step(edge, x):
    return np.where(x < edge, 0.0, 1.0)
def smoothstep(edge0, edge1, x):
    t = np.clip((x - edge0) / (edge1 - edge0), 0.0, 1.0)
    return t * t * (3 - 2 * t)
def mix(a, b, t):
    return (1 - t) * a + t * b
def reflect(i, n):
    n = normalize(n)
    dot_product = dot(i, n)
    reflection_vector = i - 2 * dot_product * n
    return reflection_vector

def rotationMatrixXYZ(euler):
    cx = cos(euler[0]);
    sx = sin(euler[0]);
    cy = cos(euler[1]);
    sy = sin(euler[1]);
    cz = cos(euler[2]);
    sz = sin(euler[2]);

    return mat3(
        vec3(cy * cz,  cx * sz + sx * sy * cz,  sx * sz - cx * sy * cz  ),
        vec3(-cy * sz, cx * cz - sx * sy * sz,  sx * cz + cx * sy * sz  ),
        vec3(sy,      -sx * cy,                 cx * cy                 )
    )
    
def cos_weighted_random_hemisphere_direction(n):
    r = vec2(rand(), rand())
    uu = normalize(cross(n, vec3(1, 0, 0) if abs(n[1]) > .5 else vec3(0, 0, 1)))
    vv = cross(uu, n)

    ra = sqrt(r[1])
    rx = ra * cos(TWOPI * r[0])
    ry = ra * sin(TWOPI * r[0])
    rz = sqrt(1 - r[1])

    rr = rx * uu + ry * vv + rz * n
    return normalize(rr)