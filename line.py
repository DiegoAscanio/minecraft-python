import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()

# desenha uma linha de 5 blocos de pedra à frente do jogador
[x,y,z] = mc.player.getPos()
i = 0
while i < 5:
	mc.setBlock(x+i,y,z+3,block.STONE)
	i += 1

