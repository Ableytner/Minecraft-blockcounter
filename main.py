import os
import anvil
from multiprocessing import Pool
from collections import Counter

def count_blocks(region_file):
    block_counts = Counter()
    region = anvil.Region.from_file(region_file)
    
    for x in range(32):
        for z in range(32):
            try:
                chunk = anvil.Chunk.from_region(region, x, z)
                for y in range(-64, 321):
                    for dx in range(16):
                        for dz in range(16):
                            block = chunk.get_block(dx, y, dz)
                            if block.id != 'minecraft:air':
                                block_counts[block.id] += 1
            except:
                pass
    return block_counts

def main():
    filenames = os.listdir("region_testdata/")
    print(filenames)
    with Pool(processes=11) as pool:
        results = pool.map(count_blocks, ['region_testdata/' + filename for filename in filenames])
        total_counts = Counter()
        for result in results:
            total_counts += result
        print(f"Block counts in the region: {dict(total_counts)}")

if __name__ == "__main__":
    main()
