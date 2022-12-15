import bpy

# function to convert degrees to euler radians
def deg2rad(deg):
    return deg * (3.141592653589793 / 180)

# delete the default cube and camera and lamp
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# create some color materials
red = bpy.data.materials.new(name="Red")
red.diffuse_color = (1, 0, 0, 1)

green = bpy.data.materials.new(name="Green")
green.diffuse_color = (0, 1, 0, 1)

blue = bpy.data.materials.new(name="Blue")
blue.diffuse_color = (0, 0, 1, 1)

yellow = bpy.data.materials.new(name="Yellow")
yellow.diffuse_color = (1, 1, 0, 1)

purple = bpy.data.materials.new(name="Purple")
purple.diffuse_color = (1, 0, 1, 1)


# create a red cube
bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0))
bpy.data.objects["Cube"].name = "RedCube"
bpy.data.objects["RedCube"].scale = (1, 1, 1)
bpy.data.objects["RedCube"].rotation_euler = (0, 0, 0)
bpy.data.objects["RedCube"].data.materials.append(red)

# create a green cube
bpy.ops.mesh.primitive_cube_add(location=(0, 0, 2))
bpy.data.objects["Cube"].name = "GreenCube"
bpy.data.objects["GreenCube"].scale = (1, 1, 1)
bpy.data.objects["GreenCube"].rotation_euler = (0, 0, 0)
bpy.data.objects["GreenCube"].data.materials.append(green)

# create a blue cube
bpy.ops.mesh.primitive_cube_add(location=(0, 0, 4))
bpy.data.objects["Cube"].name = "BlueCube"
bpy.data.objects["BlueCube"].scale = (1, 1, 1)
bpy.data.objects["BlueCube"].rotation_euler = (0, 0, 0)
bpy.data.objects["BlueCube"].data.materials.append(blue)

# create a yellow cube
bpy.ops.mesh.primitive_cube_add(location=(0, 0, 6))
bpy.data.objects["Cube"].name = "YellowCube"
bpy.data.objects["YellowCube"].scale = (1, 1, 1)
bpy.data.objects["YellowCube"].rotation_euler = (0, 0, 0)
bpy.data.objects["YellowCube"].data.materials.append(yellow)

# create a purple cube
bpy.ops.mesh.primitive_cube_add(location=(0, 0, 8))
bpy.data.objects["Cube"].name = "PurpleCube"
bpy.data.objects["PurpleCube"].scale = (1, 1, 1)
bpy.data.objects["PurpleCube"].rotation_euler = (0, 0, 0)
bpy.data.objects["PurpleCube"].data.materials.append(purple)

# create a camera named Camera
bpy.ops.object.camera_add(location=(20.3198, -23.7548, 17.7938))
bpy.data.objects["Camera"].name = "Camera"

# camera x rotation is 65.3602 degrees, y rotation is 0 degrees, z rotation 40.32 degrees using euler radians
bpy.data.objects["Camera"].rotation_euler = (deg2rad(65.3602), 0, deg2rad(40.32))

# create a light named Lamp
bpy.ops.object.light_add(type='POINT', radius=1, align='WORLD', location=(0, 0, 10), scale=(1, 1, 1))
bpy.data.objects["Point"].name = "Lamp"
