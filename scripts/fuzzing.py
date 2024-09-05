import threading
import subprocess

threads = []
def run(id: int, args: str):
    cmd = f"./test.sh {id} {id} {args}"
    res = subprocess.run(cmd, shell=True, text=True, capture_output=True)
    print(res.stdout, res.stderr)
def main():
    for t in range(0, 5):
        thread = threading.Thread(target=run, args=[t])
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
