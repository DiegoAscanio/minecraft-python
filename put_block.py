import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()

# coloca um bloco de pedra 3 blocos acima da cabeça do jogador
[x,y,z] = mc.player.getPos()
mc.setBlock(x,y+3,z,block.STONE)

