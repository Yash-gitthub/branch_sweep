import subprocess
def main():
    print("branch-sweep starting ...")
    m_branch = subprocess.run(["git","branch"], capture_output=True, text=True)
    if "main" in m_branch.stdout:
        default_branch = "main"
    else:
        default_branch = "master"
    result = subprocess.run(["git","branch","--merged",default_branch], capture_output=True, text=True)
    protected = []
    deletable = []
    current_branch = None
    r = result.stdout.splitlines()
    for i in range(len(r)):
        r[i] = r[i].strip()
        if r[i].startswith("* "):
            r[i] = r[i][2:]
            current_branch = r[i]
    protected = [current_branch, default_branch]
    print(protected)
    for branch in r:
        if branch not in protected:
            deletable.append(branch)
    print("Deletable branches:")
    c=1
    for branch in deletable:
        print(f"{c}. {branch}")
        c+=1
    action = input("Delete these branches? (Y/n): ")
    if action.lower() in ["y", "yes"]:
        for branch in deletable:
            print("Deleted",branch)
            subprocess.run(["git", "branch", "-d", branch])
    elif action.lower() in ["n", "no"]:
        print("No branches deleted")
    else:
        print("no action recieved")
if __name__ == "__main__":
    main()