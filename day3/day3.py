from functools import reduce

def get_file_as_list_lines(filepath):
    input_file = open(filepath)
    line_list = []
    for line in input_file:
        line_list.append(line.strip())
    return line_list

def part_one(lin):
    height = len(lin)
    pwidth = len(lin[-1])
    tree_counter = 0
    j = 0
    for i in range(height):
        if lin[i][j] == '#':
            tree_counter += 1
        j = (j + 3) % pwidth
    print("Sol. {}".format(tree_counter))


def part_two(lin):
    height = len(lin)
    pwidth = len(lin[-1])
    tree_counters = [0,0,0,0,0]
    for idx , steps in enumerate([(1,1),(3,1),(5,1),(7,1),(1,2)]):
        j = 0
        rstep = steps[0]
        dstep = steps[1]
        for i in range(0, height, dstep):
            if lin[i][j] == '#':
                tree_counters[idx] += 1
            j = (j + rstep) % pwidth
    print("Sol. {}".format(reduce((lambda x, y: x* y), tree_counters)))

if  __name__ == "__main__":
    lin = get_file_as_list_lines("./input.txt")
    part_two(lin)