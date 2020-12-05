import re
from collections import defaultdict


wanted_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"}
regexp = re.compile(r'#[\w\d]{6}')
eyecolors = ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")

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
    for doc_key, doc_dict in list(lin.items()):
        continue_flag = False
        for field in wanted_fields:
            if is_general_valid(field, doc_dict):
                continue_flag = True
                continue
        if continue_flag:
            continue
        valid_doc += 1
    print("Sol. {}".format(valid_doc))


def part_two(lin):
    valid_doc = 0
    for doc_key, doc_dict in list(lin.items()):
        continue_flag = False
        for field in wanted_fields:
            if is_general_valid(field, doc_dict):
                continue_flag = True
                continue
        if continue_flag:
            continue
        if is_birthyear_valid(doc_dict['byr']) and \
           is_issueyear_valid(doc_dict['iyr']) and \
           is_expirationyear_valid(doc_dict['eyr']) and \
           is_height_valid(doc_dict['hgt']) and \
           is_haircolor_valid(doc_dict['hcl']) and \
           is_eyecolor_valid(doc_dict['ecl']) and \
           is_passportid_valid(doc_dict['pid']):
            valid_doc += 1
    print("Sol. {}".format(valid_doc))

def is_passportid_valid(pid): #sorry, but sins must be done
    for char in pid:
        if not char.isdigit():
            return False
    return len(pid)==9  

def is_eyecolor_valid(ecl):
    return ecl in eyecolors

def is_haircolor_valid(hcl):
    return regexp.search(hcl)

def is_height_valid(hgt):
    suff = hgt[-2:]
    num = hgt[:-2]
    if suff == "in":
        return 59 <= int(num) <= 76
    if suff == "cm":
        return 150 <= int(num) <= 193
    return False

def is_general_valid(field, doc_dict):
    return field not in doc_dict.keys() and field != "cid"

def is_birthyear_valid(byr):
    return check_date(1920, 2002, byr)

def is_issueyear_valid(byr):
    return check_date(2010, 2020, byr)

def is_expirationyear_valid(byr):
    return check_date(2020, 2030, byr)

def check_date(begin, end, date):
    try:
        return begin <= int(date) <= end
    except Exception:
        return False



if  __name__ == "__main__":
    lin = get_file_as_doc_dict("./input.txt")
    part_two(lin)
