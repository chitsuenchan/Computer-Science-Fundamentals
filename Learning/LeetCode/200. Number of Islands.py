"""
    Passes 48/49
    Didn't pass final test due to time exceeded

    Chat GPT says it's 0(n*m) time complexity and space complexity

"""

def numIslands(grid):
    islands = {
    }


    islands_count = 1


    def neighboursPartOfIsland(islands, neighbours):
        for key, value in islands.items():
            if any(neighbour in value for neighbour in neighbours):
                return key
        return -1


    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print("current row:", grid[i])
            print("current hashmap:", islands)
            print("current coordinate: ", (i,j))
            print("current value: ", grid[i][j])

            if grid[i][j] == "1":

                # Getting set of neighbours
                neighbours = set()
                neighbours.add((i, j))

                # Top coordinate
                if i > 0:
                    print("top coordinate is:", (i - 1, j))
                    print("top value is:", grid[i - 1][j])
                    if grid[i - 1][j] == "1":
                        neighbours.add((i - 1, j))

                # Bottom coordinate
                if i < len(grid) - 1:
                    print("bottom coordinate is:", (i + 1, j))
                    print("bottom value is:", grid[i + 1][j])
                    if grid[i + 1][j] == "1":
                        neighbours.add((i + 1, j))

                # Left coordinate
                if j > 0:
                    print("left coordinate is:", (i, j - 1))
                    print("left value is:", grid[i][j - 1])
                    if grid[i][j - 1] == "1":
                        neighbours.add((i, j - 1))

                # Right neighbour
                if j < len(grid[0]) - 1:
                    print("right coordinate is:", (i, j + 1))
                    print("right value is:", grid[i][j + 1])
                    if grid[i][j + 1] == "1":
                        neighbours.add((i, j + 1))

                print("current neighbour set is", neighbours)
                part_of_existing_island = neighboursPartOfIsland(islands, neighbours)
                print("neighbour set part of island:", part_of_existing_island)

                # New Island
                if part_of_existing_island == -1:
                    print("NEW ISLAND")

                    islands[islands_count] = neighbours
                    islands_count += 1
                else:
                    print("PART OF EXISTING ISLAND")

                    print("Updating island:",neighbours)
                    islands[part_of_existing_island].update(neighbours)
                print("")
            else:
                print("Skip, its a zero")
                print("")

        print("FINISHED")
        print(islands)

        def merge_keys(hashmap):
            merged = {}
            for key, values in hashmap.items():
                merged_key = None
                for k, v in merged.items():
                    if any(t in v for t in values):
                        merged_key = k
                        break
                if merged_key is None:
                    merged_key = key
                else:
                    merged[merged_key] |= values
                if merged_key in merged:  # Check if the key already exists
                    merged[merged_key].update(values)
                else:
                    merged[merged_key] = set(values)
            return merged

        islands = merge_keys(islands)
        print(islands)

    return len(islands)

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]]

grid = [
    ["1","0","1","1","1"],
    ["1","0","1","0","1"],
    ["1","1","1","0","1"]
]

print(numIslands(grid))