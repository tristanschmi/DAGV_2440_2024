import maya.cmds as cmds
import math

# Clear any existing scene elements
cmds.file(new=True, force=True)

# Create the stem of the flower
stem = cmds.polyCylinder(r=0.1, h=5, name='stem')[0]
cmds.move(0, 2.5, 0, stem)

# Create the center of the flower
center = cmds.polySphere(r=0.3, name='center')[0]
cmds.move(0, 5, 0, center)

# Petal settings
petal_radius = 0.3
petal_distance = 0.5  # Distance from center (radius of circular pattern)
petal_scale_y = 0.2  # Flattening factor for petals

# Create petals around the center
num_petals = 8
for i in range(num_petals):
    angle_deg = (360 / num_petals) * i
    angle_rad = math.radians(angle_deg)  # Convert angle to radians
    x = petal_distance * math.cos(angle_rad)
    z = petal_distance * math.sin(angle_rad)
    
    # Create petal and flatten it
    petal = cmds.polySphere(r=petal_radius, name=f'petal_{i+1}')[0]
    cmds.scale(1, petal_scale_y, 1, petal)  # Scale Y-axis to flatten

    # Move petal to calculated position and rotate to face outward
    cmds.move(x, 5, z, petal)
    cmds.rotate(0, angle_deg, 0, petal)

# Leaf settings
leaf_length = 1.0
leaf_width = 0.3
leaf_thickness = 0.1

# Create the first leaf on the left side
leaf1 = cmds.polyCube(w=leaf_length, h=leaf_thickness, d=leaf_width, name='leaf1')[0]
cmds.move(-0.6, 1.5, 0, leaf1)  # Position it along the stem
cmds.rotate(0, 0, 45, leaf1)  # Slightly rotate

# Create the second leaf on the right side
leaf2 = cmds.polyCube(w=leaf_length, h=leaf_thickness, d=leaf_width, name='leaf2')[0]
cmds.move(0.6, 1.5, 0, leaf2)
cmds.rotate(0, 0, -45, leaf2)

# Group everything into a single flower structure
flower = cmds.group(stem, center, *[f'petal_{i+1}' for i in range(num_petals)], leaf1, leaf2, name='Flower')

