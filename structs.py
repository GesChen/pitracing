import numpy as np

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
    def __init__(self, pos, rot, fov, near_clip_plane, aspect, plane_width, plane_height):
        self.pos = np.array(pos, dtype=float)
        self.rot = np.array(rot, dtype=float)
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
    def __init__(self, c1, c2, mat):
        self.c1 = np.array(c1, dtype=float)
        self.c2 = np.array(c2, dtype=float)
        self.mat = mat
