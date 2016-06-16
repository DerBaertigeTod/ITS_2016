import math

def get_color_name(r,g,b):
    deltas = {}
    i = 0
    colors ={'red':[255,0,0],'orange':[255,165,0],'yellow':[255,255,0],'green':[0,255,0],'blue':[0,0,255],'violett':[238,130,238]}
    for c_key, c_val in enumerate(colors):
        deltas[c_val] =  colors[c_val][0] - r
        deltas[c_val] += colors[c_val][1] - g
        deltas[c_val] += colors[c_val][2] - b
        i =i+1
    for key, val in enumerate(colors):
        deltas[val] = math.sqrt(deltas[val]*deltas[val]) 
    print deltas
    return deltas
    

color = get_color_name(0,255,0)
red=color['red']
orange=color['orange']
yellow=color['yellow']
green= color['green']
blue=color['blue']
violett=color['violett']

lowest_value= red
name='red'
if lowest_value > orange:
    lowest_value=orange
    name='orange'
if lowest_value > yellow:
    lowest_value=yellow
    name='yellow'
if lowest_value > yellow:
    lowest_value=green 
    name='green'
if lowest_value > blue:
    lowest_value=blue
    name='blue'
if lowest_value > violett:
    lowest_value=violett
    name='violett'
print lowest_value
print name
