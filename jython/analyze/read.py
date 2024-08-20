import subprocess
import sys
LIMIT_SECTION = ' --section=.text'
FLAG = ' -dGl'
CMD = 'objdump' + FLAG
OFFSET = '0010'

def captureDump(file):
    FIN_CMD = CMD + ' ' + file
    print(FIN_CMD)
    result = subprocess.run(FIN_CMD, shell=True, capture_output=True, text=True)

    return result.stdout
def getAddrFromDump(dump):
    lines = dump.split('\n')
    addr = []
    for line_no, line in enumerate(lines, start=1):
        current_line = line.strip()
        next_line = lines[line_no].strip() if line_no < len(lines) else 'No next line'
        if '/home' in next_line:
            addr.append(current_line.split('\t'))
    return addr
def getAddrFromFile(file):
    addr = []
    with open(file, 'r') as f:
        lines = f.readlines()
        for line_no, line in enumerate(lines, 1):
            current_line = line.strip()
            next_line = lines[line_no].strip() if line_no < len(lines) else 'No next line'
            if ('/home' in next_line):
                addr.append(current_line.split('\t'))
    return addr
def printAddr(addr):
    for a in (addr):
        if ('()' in a[0][:-1]):
            print(f'Function: {a[0][:-1]}')
        else:
            print(f'{OFFSET}{a[0][:-1]} ---------------- {a[len(a) - 1]}')
def extractAddr(addr):
    instruction_addresses = []
    for a in addr:
        if ('()' not in a[0]):
            instruction_addresses.append(OFFSET + a[0][:-1])
    return instruction_addresses

def main():
    if len(sys.argv) < 2:
        print("Execute: python3 read.py [file]")
        sys.exit(1)

    file = sys.argv[1]
    
    dump = captureDump(file)
    
    addr = getAddrFromDump(dump)

    printAddr(addr)
    last_exec_instructions = extractAddr(addr)

    
if __name__ == '__main__':
    main()


