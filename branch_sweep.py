import subprocess
def main():
    print("branch-sweep starting ...")
    result = subprocess.run(["git","branch","--merged","master"], capture_output=True, text=True)
    non_deletable = []
    current_branch = None
    r = result.stdout.splitlines()
    for i in range(len(r)):
        r[i] = r[i].strip()
        if r[i].startswith("* "):
            r[i] = r[i][2:]
            current_branch = r[i]
    non_deletable.append(current_branch)
    if "master" not in non_deletable:
        non_deletable.append("master")
    if "main" not in non_deletable:
        non_deletable.append("main")
    print(r)
if __name__ == "__main__":
    main()