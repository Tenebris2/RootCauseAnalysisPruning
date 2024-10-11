import sys
import re
from enum import Enum


class SelectionMethod(Enum):
    BEGIN = 1
    MIDDLE = 2
    END = 3


#
# def extract_addresses(filepath, outpath):
#     addresses = []
#     with open(filepath, "r") as file:
#         lines = file.readlines()
#
#     for i in range(1, len(lines)):
#         if "/home/" in lines[i] or "/Aurora/" in lines[i]:
#             # Extract the address from the line before
#             match = re.search(r"([0-9a-fA-F]+):", lines[i - 1])
#             if match:
#                 addresses.append(match.group(1))
#
#     with open(outpath, "w") as outfile:
#         for address in addresses: outfile.write(address + "\n")
def extract_addresses(filepath, target):
    addresses = []
    addr = []
    with open(filepath, "r") as file:
        lines = file.readlines()
    begin = False
    for i in range(1, len(lines) - 1):
        if begin == True:
            match = re.search(r"([0-9a-fA-F]+):", lines[i])
            if match:
                addr.append(match.group(1))

        if (
            "/home/" in lines[i + 1]
            or "/Aurora/" in lines[i + 1]
            or "/evaluation" in lines[i + 1]
        ):
            begin = True
            if "c" in addr:
                addr = addr[1:]
            else:
                addr = addr[:]
            addresses.append(addr)
            addr = []
            # Extract the address from the line before
    for a in addresses:
        if target in a:
            return a
    return [0, 0]


def classifier(addresses, target):
    size = len(addresses)

    if size >= 3:
        begin = addresses[0 : size // 3]
        middle = addresses[size // 3 : 2 * size // 3]
        end = addresses[2 * size // 3 :]
    elif size == 2:
        begin = addresses[0]
        end = addresses[1]
        middle = addresses[1]
    else:
        begin = addresses[0]
        end = 0
        middle = 0
    print("BEGIN: ", begin)
    print("MIDDLE: ", middle)
    print("END: ", end)
    if target in begin:
        print("BEGIN")
    elif target in middle:
        print("MIDDLE")
    else:
        print("END")


# Example usage
filepath = sys.argv[1]
target = sys.argv[2]
addresses = extract_addresses(filepath, target)
classifier(addresses, target)
