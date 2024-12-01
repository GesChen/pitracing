from helperfunctions import *
from structs import *
from consts import *
from intersectors import *
import pygame
import numpy as np
from numpy import sin, cos, tan, radians
import time
import cv2

width, height = 100, 100
resolution = vec2(width, height)

cam_pos = vec3(-.2, .2, 0)
cam_rot = vec3(-20, 0, 0)
fov = 70
nearPlane = .01

dp = False

world = [
    Box(vec3(0,0,.3), vec3(.1,.1,.1), Material(vec3(.5,.5,.5), 0, 0))
]

def save(image):
    image = (image * 255).astype(np.uint8)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    cv2.imwrite('test.jpg', image)

def display():
    pygame.init()
    display = pygame.display.set_mode((width, height))

    Z_255 = (image * 255).astype(np.uint8)
    Z_255 = np.flipud(Z_255)
    
    surf = pygame.surfarray.make_surface(Z_255)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        display.blit(surf, (0, 0))
        pygame.display.update()

    pygame.quit()

def new_camera(pos, rot, fov, near_plane):
    aspect = height / width  # height / width
    plane_height = near_plane * tan(radians(fov) * 0.5) * 2.0
    plane_width = plane_height * aspect

    rotmatrix = rotationMatrixXYZ(np.radians(rot))
    
    return Camera(
        pos=pos,
        rot=rot,
        rotation_matrix = rotmatrix,
        fov=fov,
        near_clip_plane=near_plane,
        aspect=aspect,
        plane_width=plane_width,
        plane_height=plane_height
    )

    p = (-resolution + 2 * coord) / resolution[1]

    ww = normalize(target - cam.pos)
    uu = normalize(np.cross(ww, np.array([0, 1, 0])))
    vv = normalize(np.cross(uu, ww))
    rd = normalize(p[0] * uu + p[1] * vv + 2 * ww)
    
    return Ray(o=cam.pos, d=rd, color=np.array([1, 1, 1]), incoming_light=np.array([0, 0, 0]))

def camera_ray(cam, uv):
    ndc = (uv * 2) - 1;
    
    aspect_ratio = cam.plane_width / cam.plane_height;
    
    fov_scale = tan(radians(cam.fov) * .5);
    
    ray_dir = normalize(vec3(ndc[0] * aspect_ratio * fov_scale, 
                            ndc[1] * fov_scale, 
                            -1));
    
    # idk why but negating it seems to work. really, idk why . like wtf
    rotated_ray_dir = -np.matmul(cam.rotation_matrix, ray_dir)
    
    
    return Ray(cam.pos, normalize(rotated_ray_dir), vec3(1, 1, 1), vec3(0, 0, 0));

def world_intersect(ray):
    closest = MAXHIT;
    for obj in world:
        hit = global_intersect(obj, ray)
        
        if hit.didhit and hit.dist < closest.dist:
            closest = hit
    
    return closest

def sky_color(ray):
    if ray.d[1] < 0:
        return vec3(0, 0, 0)
    
    factor = smoothstep(0, 1, .5 * (ray.d[1] + 1))
    return mix(vec3(1, 1, 1), vec3(.3, .5, .7), factor)


def pixel(coord, camera):
    accum = vec3(0, 0, 0)
    for s in range(SAMPLES):
        variance = vec2(rand(), rand()) - .5
        uv = (coord + variance) / resolution;
        ray = camera_ray(camera, uv)
        
        bounce = 0
        while bounce < MAX_BOUNCES:
            hit = world_intersect(ray)
            
            if not hit.didhit:
                ray.incoming_light += sky_color(ray)
                break
            
            ray.o = hit.point
            
            mat = hit.mat
            specular_dir = reflect(ray.d, hit.normal)
            
            if mat.smoothness == 1:
                ray.d = specular_dir
            else:
                diffuse_dir = cos_weighted_random_hemisphere_direction(hit.normal)
                
                ray.d = mix(diffuse_dir, specular_dir, 1 if mat.smoothness > rand() else 0)
                
            ray.color *= mat.color
            ray.incoming_light += ray.color * mat.color * mat.emission

            if mat.emission > 0: break
            
            bounce += 1
    
        accum += ray.color * ray.incoming_light
    
    return accum / SAMPLES

camera = new_camera(cam_pos, cam_rot, fov, nearPlane)

print(camera_ray(camera, vec2(.5, .5)).d)

starttime = time.time()
image = np.zeros((width, height, 3), dtype=np.float32)
for y in range(height):
    for x in range(width):
        image[x][y] = pixel(vec2(x, y), camera)
print(f'total time: {time.time() - starttime}')

save(image)
display()