from collections import defaultdict

def get_file_as_list_lines(filepath):
    input_file = open(filepath)
    line_list = []
    for line in input_file.read().split("\n\n"):
        line_list.append([])
        for lin in line.strip().split("\n"):
            line_list[-1].append(lin.strip())
    return line_list

def part_one(lin):
    count = 0
    for qs in lin:
        qset = set()
        for q in qs:
            for char in q:
                qset.add(char)
        count += len(qset)
    print("Sol. {}".format(count))


def part_two(lin):
    count = 0
    for group in lin:
        qdict = defaultdict(int)
        for qs in group:
            print(group, qs)
            for char in qs:
                qdict[char] += 1
        for key, value in qdict.items():
            if value == len(group):
                count += 1
#        count += len(qset)
    print("Sol. {}".format(count))


if  __name__ == "__main__":
    lin = get_file_as_list_lines("./input.txt")
    part_two(lin)