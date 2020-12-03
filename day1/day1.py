

def get_file_as_list_lines(filepath):
    input_file = open(filepath)
    line_list = []
    for line in input_file:
        line_list.append(int(line.strip()))
    return line_list

def part_one(lin):
    for x in lin:
        for y in lin[::-1]:
            if x + y == 2020:
                print("Solution: {xs} + {ys} = 2020, {xs} * {ys} = {sol}".format(xs=x, ys=y, sol=x*y))

def part_two(lin):
    for x in lin:
        for y in lin[::-1]:
            for z in lin[::-1]:
                if x + y + z == 2020:
                    print("Solution: {xs} + {ys} + {zs} = 2020, {xs} * {ys} * {zs} = {sol}".format(xs=x, ys=y, zs=z, sol=x*y*z))

if  __name__ == "__main__":
    lin = get_file_as_list_lines("./input.txt")
    part_two(lin)
