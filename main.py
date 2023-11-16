import json
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
                for block in anvil.Chunk.stream_chunk(chunk):
                    if block.id != 'minecraft:air':
                        block_counts[block.id] += 1
            except:
                pass
    return block_counts

def main():
    filenames = os.listdir("region_testdata/")
    print(filenames)
    with Pool(processes=20) as pool:
        results = pool.map(count_blocks, ['region_testdata/' + filename for filename in filenames])
        total_counts = Counter()
    for result in results:
        total_counts += result

    print(f"Block counts in the region: {dict(total_counts)}")
    with open("out.json", "w+") as f:
        json.dump(dict(total_counts), f)

if __name__ == "__main__":
    main()
