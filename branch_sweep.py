import subprocess
def main():
    print("branch-sweep starting ...")
    result = subprocess.run(["git","branch","--merged","master"], capture_output=True, text=True)
    protected = []
    deletable = []
    current_branch = None
    r = result.stdout.splitlines()
    for i in range(len(r)):
        r[i] = r[i].strip()
        if r[i].startswith("* "):
            r[i] = r[i][2:]
            current_branch = r[i]
    protected = [current_branch, "master", "main"]
    for branch in r:
        if branch not in protected:
            deletable.append(branch)
    print(r)
    print(protected)
    print(deletable)
if __name__ == "__main__":
    main()