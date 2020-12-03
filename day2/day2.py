

def get_file_as_list_lines(filepath):
    input_file = open(filepath)
    line_list = []
    for line in input_file:
        line_list.append(line.strip())
    return line_list

def get_list_of_modeled_lines(lin):
    mlin = []
    for line in lin:
        splitted_line = line.split()
        interval = splitted_line[0].split('-')
        interval = (int(interval[0]), int(interval[1]))
        letter = splitted_line[1][:1]
        password = splitted_line[2]
        mlin.append((interval, letter, password))
    return mlin

def part_one(mlin):
    counter = 0
    for inst in mlin:
        if inst[0][0] <= inst[2].count(inst[1]) <= inst[0][1]:
            counter += 1
    print(counter)

def part_two(lin):
    counter = 0
    for inst in mlin:
        fpos = inst[0][0] - 1
        spos = inst[0][1] - 1
        letter = inst[1]
        passw = inst[2] 
        if (passw[fpos] == letter and passw[spos] != letter) or\
           (passw[fpos] != letter and passw[spos] == letter):
            counter += 1
    print(counter)


if  __name__ == "__main__":
    lin = get_file_as_list_lines("./input.txt")
    mlin = get_list_of_modeled_lines(lin)
    part_two(mlin)