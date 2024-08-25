import re
import sys
import pprint
args = sys.argv;

def extract_after_at(arr):
    for i in range(len(arr)):
        if arr[i] == 'at':
            return arr[i + 1]

    return "\n"
def main():
    if len(args) < 3:
        print("extract_line_ranking.py [path] [target]")
        return 0
    else:
        path = args[1]
        target = args[2]

        data = []
        
        temporary_data = set()

        with open(path, "r") as file:
            data = [extract_after_at(x.split(' ')).strip() for x in file.readlines()]
        for line in data:
            print(line, target)
            if line == target:
                print("TRUE")
                break
            if '.c' in line:
                temporary_data.add(line)
        
        data = temporary_data
        print(data)
        # pprint.pprint(temporary_data)
        print(f"Line ranking at: {len(data) + 1}")

main()
