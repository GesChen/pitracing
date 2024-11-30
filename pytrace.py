from helperfunctions import *
from structs import *
from consts import *
import pygame
import numpy as np
from numpy import sin, cos, tan, radians

width, height = 600, 400
resolution = vec2(width, height)

camPos = vec3(0, 0, 0)
camRot = vec3(1, 0, 0)
fov = 70
nearPlane = .01

def new_camera(pos, rot, fov, near_plane):
    aspect = height / width  # height / width
    plane_height = near_plane * tan(radians(fov) * 0.5) * 2.0
    plane_width = plane_height * aspect
    
    return Camera(
        pos=pos,
        rot=rot,
        fov=fov,
        near_clip_plane=near_plane,
        aspect=aspect,
        plane_width=plane_width,
        plane_height=plane_height
    )

def camera_to_target(cam, target, coord):
    p = (-resolution + 2 * coord) / resolution[1]

    ww = normalize(target - cam.pos)
    uu = normalize(np.cross(ww, np.array([0, 1, 0])))
    vv = normalize(np.cross(uu, ww))
    rd = normalize(p[0] * uu + p[1] * vv + 2 * ww)
    
    return Ray(o=cam.pos, d=rd, color=np.array([1, 1, 1]), incoming_light=np.array([0, 0, 0]))

def pixel(coord, camera):
    for s in range(SAMPLES):
        variance = vec2(rand(), rand()) - .5

        ray = 

    return 

camera = new_camera(camPos, camRot, fov, nearPlane)

image = np.zeros((height, width, 3), dtype=np.float32)
for y in range(height):
    for x in range(width):
        image[y][x] = pixel(vec2(x, y), camera)

def display():
    pygame.init()
    display = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Black Image (0-1 scale)")

    Z_255 = (image * 255).astype(np.uint8)

    surf = pygame.surfarray.make_surface(Z_255)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        display.blit(surf, (0, 0))
        pygame.display.update()

    pygame.quit()
