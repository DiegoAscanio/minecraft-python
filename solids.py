import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

def cube(x, y, z, side, material):
	for i in range (0,side):
		for j in range (0,side):
			for k in range (0,side):
				mc.setBlock(x+i,y+j,z+k,material)

def sphere(x, y, z, radius, material):
	for i in range(-radius,radius):
		for j in range(-radius,radius):
			for k in range(-radius,radius):
				if (i**2 + j**2 + k**2) < radius ** 2:
					mc.setBlock(x+i,y+j,z+k,material)
