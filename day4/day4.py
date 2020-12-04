from functools import reduce
from collections import defaultdict


wanted_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"} #, "cid"


def get_file_as_doc_dict(filepath):
    input_file = open(filepath)
    doc_dict = defaultdict(dict)
    counter_id = 0
    for doc in input_file.read().split("\n\n"):
        for field_val in doc.split():
            splitted = field_val.split(":")
            field = splitted[0]
            val = splitted[1]
            doc_dict[counter_id][field] = val
        counter_id += 1
    input_file.close()
    return doc_dict


def part_one(lin):
    valid_doc = 0
    for doc_dict in list(lin.values()):
        try:
            doc_set =set(doc_dict.keys()).remove("cid")
        except KeyError:
            doc_set=set(doc_dict.keys())
        if not doc_set:
            continue
        if doc_set.issubset(wanted_fields):
                valid_doc += 1
    print("Sol. {}".format(valid_doc))

if  __name__ == "__main__":
    lin = get_file_as_doc_dict("./input.txt")
    part_one(lin)
