import anvil

region = anvil.Region.from_file('region_testdata/r.-2.-1.mca')

for x in range(32):
        for z in range(32):
            try:
                chunk = anvil.Chunk.from_region(region, x, z)

                block = chunk.get_block(0, 0, 0)

                print(block) # <Block(minecraft:air)>
                print(block.id) # air
                print(block.properties) # {}
            except:
                print("error")