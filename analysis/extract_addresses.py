import sys
import re

def extract_addresses(filepath, outpath):
    addresses = []
    with open(filepath, 'r') as file:
        lines = file.readlines()
    
    for i in range(1, len(lines)):
        if '/home/tenebris/' in lines[i] or '/Aurora/evaluation/' in lines[i]:
            # Extract the address from the line before
            match = re.search(r'([0-9a-fA-F]+):', lines[i-1])
            if match:
                addresses.append(match.group(1))
    
    with open(outpath, 'w') as outfile:
        for address in addresses:
            outfile.write(address + '\n')

# Example usage
filepath = sys.argv[1]
outpath = 'addresses'
addresses = extract_addresses(filepath, outpath)
