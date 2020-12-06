from functools import reduce

def get_file_as_list_lines(filepath):
    input_file = open(filepath)
    line_list = []
    for line in input_file:
        line_list.append(line.strip())
    return line_list

def part_one(lin):
    boarding_passes = []
    for line in lin:
        boarding_passes.append([0,0])
        begin = 0
        end = 128
        row_inst = line[:7]
        col_inst = line[7:]
        for inst in row_inst:
            print(inst)
            if inst == 'F':
                end -= (end-begin) // 2
            elif inst == 'B':
                begin += ((end- begin) // 2)
            else:
                print('ERROR (char {} invalid)'.format(inst))
            print(begin, end)
        print("------------------")
        boarding_passes[-1][0] = begin
        begin = 0
        end = 8
        for inst in col_inst:
            if inst == 'L':
                end -= (end-begin) // 2
            elif inst == 'R':
                begin += ((end- begin) // 2)
            else:
                print('ERROR (char {} invalid)'.format(inst))
        boarding_passes[-1][1] = begin
    print(boarding_passes)
    max_id = -1
    for id in boarding_passes:
        if max_id < id[0]*8 + id[1]:
            max_id = id[0]*8 + id[1]
    print("Sol. {}".format(max_id))

def part_two(lin):
    boarding_passes = []
    for line in lin:
        matrix = [[0 for j in range(8)] for i in range(128)]
        boarding_passes.append([0,0])
        begin = 0
        end = 128
        row_inst = line[:7]
        col_inst = line[7:]
        for inst in row_inst:
            print(inst)
            if inst == 'F':
                end -= (end-begin) // 2
            elif inst == 'B':
                begin += ((end- begin) // 2)
            else:
                print('ERROR (char {} invalid)'.format(inst))
            print(begin, end)
        print("------------------")
        boarding_passes[-1][0] = begin
        begin = 0
        end = 8
        for inst in col_inst:
            if inst == 'L':
                end -= (end-begin) // 2
            elif inst == 'R':
                begin += ((end- begin) // 2)
            else:
                print('ERROR (char {} invalid)'.format(inst))
        boarding_passes[-1][1] = begin
    max_id = -1
    for id in boarding_passes:
        matrix[id[0]][id[1]] = 1
        if max_id < id[0]*8 + id[1]:
            max_id = id[0]*8 + id[1]
    for i, row in enumerate(matrix):
        print(i, row)

if  __name__ == "__main__":
    lin = get_file_as_list_lines("./input.txt")
    part_two(lin)