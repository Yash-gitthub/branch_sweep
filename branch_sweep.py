import subprocess
def main():
    print("branch-sweep starting ...")
    result = subprocess.run(["git","branch","--merged","master"], capture_output=True, text=True)
    print(result.stdout)
if __name__ == "__main__":
    main()