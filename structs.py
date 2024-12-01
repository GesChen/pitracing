import numpy as np


def vec2(x,y):
    return np.array([x,y], dtype=float)
def vec3(x,y,z):
    return np.array([x,y,z], dtype=float)
def mat3(a,b,c):
    return np.vstack((a,b,c))

class Material:
    def __init__(self, color, smoothness, emission):
        self.color = np.array(color, dtype=float)
        self.smoothness = float(smoothness)
        self.emission = float(emission)

class Hit:
    def __init__(self, didhit, dist, point, normal, mat):
        self.didhit = bool(didhit)
        self.dist = float(dist)
        self.point = np.array(point, dtype=float)
        self.normal = np.array(normal, dtype=float)
        self.mat = mat

class Ray:
    def __init__(self, o, d, color, incoming_light):
        self.o = np.array(o, dtype=float)
        self.d = np.array(d, dtype=float)
        self.color = np.array(color, dtype=float)
        self.incoming_light = np.array(incoming_light, dtype=float)

class Camera:
    def __init__(self, pos, rot, rotation_matrix, fov, near_clip_plane, aspect, plane_width, plane_height):
        self.pos = np.array(pos, dtype=float)
        self.rot = np.array(rot, dtype=float)
        self.rotation_matrix = rotation_matrix
        self.fov = float(fov)
        self.near_clip_plane = float(near_clip_plane)
        self.aspect = float(aspect)
        self.plane_width = float(plane_width)
        self.plane_height = float(plane_height)

class Triangle:
    def __init__(self, p0, p1, p2, mat):
        self.p0 = np.array(p0, dtype=float)
        self.p1 = np.array(p1, dtype=float)
        self.p2 = np.array(p2, dtype=float)
        self.mat = mat

class Sphere:
    def __init__(self, pos, rad, mat):
        self.pos = np.array(pos, dtype=float)
        self.rad = float(rad)
        self.mat = mat

class Plane:
    def __init__(self, pos, normal, mat):
        self.pos = np.array(pos, dtype=float)
        self.normal = np.array(normal, dtype=float)
        self.mat = mat

class Box:
    def __init__(self, center, size, mat):
        self.center = np.array(center, dtype=float)
        self.size = np.array(size, dtype=float)
        self.mat = mat
