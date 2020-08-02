import hashlib
import re
from collections import Counter

flag_file = open("flag.txt", 'r').read()
vendor_file = open("mac-vendor.txt", 'r', encoding="utf8")


def get_hash(mac_vendor_file, flag_data_file):
    # write your algorithm here
    match = re.findall("[A-Z0-9]{2}:[A-Z0-9]{2}:[A-Z0-9]{2}:[A-Z0-9]{2}:[A-Z0-9]{2}:[A-Z0-9]{2}", flag_data_file)
    array, macVendors, output = [], [], ""
    for elem in match:
        array.append(elem.replace(":", "")[0:6])
    for line in mac_vendor_file.readlines():
        macVendors.append(line)
    for key, value in sorted(Counter(array).items(), key=lambda item: item[1], reverse=True):
        for line in macVendors:
            if line[0:6] == key:
                output += line[7:10] + ":"
    return hashlib.md5(output[0:len(output) - 1].encode()).hexdigest()


print(get_hash(vendor_file, flag_file))
