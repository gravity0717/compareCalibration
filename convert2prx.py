import numpy as np 
import pandas as pd 
import json 

img_width, img_height = (1920, 1080)

with open("groundtruth/cameras_210821.json", 'r' ,encoding='utf-8') as f:
    
    js = json.loads(f.read())

#Calculate vFov from focal length of 

fovs=[]
for config in js:
    f = config["focal"] 
    fov = 2* np.arctan(img_height/ (2*f[0])) 
    fovs.append(fov)

print(fovs)
