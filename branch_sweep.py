import subprocess
def main():
    print("branch-sweep starting ...")
    result = subprocess.run(["git","branch","--merged","main"], capture_output=True, text=True, cwd="/home/yash-bodake/Desktop/iit_proj/eventsphere")
    print(result.stdout)
if __name__ == "__main__":
    main()