import re
import sys
import pprint
args = sys.argv;

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
            data = [x.split(' ')[len(x.split(' ')) - 1] for x in file.readlines()]
        for line in data:
            if target in line:
                break
            if 'c' in line:
                temporary_data.add(line)
        
        data = temporary_data
        
        pprint.pprint(temporary_data)
        print(f"Line ranking at: {len(data) + 1}")

main()
