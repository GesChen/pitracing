from helperfunctions import *
import numpy as np
from consts import *

def global_intersect(any, ray):
    if isinstance(any, Triangle): return intersect_triangle(any, ray)
    if isinstance(any, Sphere): return intersect_sphere(any, ray)
    if isinstance(any, Box):   return intersect_box(any, ray)
    return NOHIT

def intersect_triangle(tri, ray):
    v1v0 = tri.p1 - tri.p0
    v2v0 = tri.p2 - tri.p0
    rov0 = ray.o - tri.p0
    n = cross(v1v0, v2v0)
    q = cross(rov0, ray.d)
    d = 1 / dot(ray.d, n)
    u = d * dot(-q, v2v0)
    v = d * dot(q, v1v0)
    t = d * dot(-n, rov0)

    if u < 0.0 or v < 0.0 or (u + v) > 1.0 or t < 0.001:
        return NOHIT
    
    return Hit(True, t, ray.o + ray.d * t, n, tri.mat)

# Sphere Intersection
def intersect_sphere(sph, ray):
    oc = sph.pos - ray.o
    l = dot(ray.d, oc)
    det = l**2 - dot(oc, oc) + sph.rad**2

    if det < 0.0:
        return NOHIT

    # Find the closer of two solutions
    t = l - sqrt(det)
    if t < 0.001:
        t = l + sqrt(det)
    
    if t < 0.001:
        return NOHIT
    
    return Hit(True, t, ray.o + ray.d * t,
               normalize(ray.o + ray.d * t - sph.pos), sph.mat)

# Plane Intersection
def intersect_plane(pln, ray):
    t = -dot(ray.o - pln.pos, pln.normal) / dot(ray.d, pln.normal)
    
    if t < 0.001:
        return NOHIT
    
    return Hit(True, t, ray.o + ray.d * t, pln.normal, pln.mat)

# Box Intersection
def intersect_box(box, ray):
    # Center the box at the origin by adjusting the ray origin
    ray.o -= box.center

    m = sign(ray.d) / np.maximum(abs(ray.d), 1e-8)
    n = m * ray.o
    k = abs(m) * box.size

    t1 = -n - k
    t2 = -n + k

    tN = np.maximum(np.maximum(t1[0], t1[1]), t1[2])
    tF = np.minimum(np.minimum(t2[0], t2[1]), t2[2])

    if tN > tF or tF <= 0.:
        return NOHIT

    normal = -sign(ray.d) * step(vec3(t1[1],t1[2],t1[0]), t1) * step(vec3(t1[2],t1[1],t1[0]), t1)
    
    return Hit(True, tN, ray.o + ray.d * tN, normal, box.mat)