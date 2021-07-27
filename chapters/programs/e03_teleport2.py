
from mcpi.minecraft import *

mc = Minecraft.create()

# CHANGE THESE NUMBERS TO THE CO-ORDS OF YOUR TELEPORTERS

teleporter_x = 742
teleporter_z = 955

destination_x = 735
destination_z = 956

while True:
    # Get player position
    pos = mc.player.getTilePos()
    print(pos)

    # Check whether your player is standing on the teleport
    if pos.x == teleporter_x and pos.z == teleporter_z:
        mc.postToChat("teleport!")
        pos.x = destination_x
        pos.z = destination_z
        mc.player.setTilePos(pos)
