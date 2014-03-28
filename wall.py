import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()

# desenha uma parede de 5 x 8 à frente do jogador
[x,y,z] = mc.player.getPos()
i = 0
while i < 5:
	j = 0
	while j < 8:
		mc.setBlock(x+i,y+j,z+3,block.STONE)
		j += 1
	i += 1

