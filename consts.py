from structs import *
from helperfunctions import *

PI = 3.14159265359
TWOPI = 6.283185
SAMPLES = 20
MAX_BOUNCES = 7
DEFAULTMAT = Material(vec3(0, 0 ,0), 0, 0)
NOHIT = Hit(False, 0, vec3(0, 0, 0), vec3(0, 0, 0), DEFAULTMAT) 
MAXHIT = Hit(False, 1000000000., vec3(0, 0, 0), vec3(0, 0, 0), DEFAULTMAT)