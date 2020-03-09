import argparse, os, subprocess, shutil

def main():
    folder_name = "mapfn-foo"

    parser = argparse.ArgumentParser(description="Generate Dockerfile for container")
    parser.add_argument("-n", "--name", help="Folder name")
    parser.add_argument("-f", "--profiler", help="Profiling function")
    parser.add_argument("-r", "--requirements", help="Pip requirements file")
    parser.add_argument("-m", "--modules", help="Additional python modules folder")
    parser.add_argument("-l", "--local", help="Path to local pip packages")
    options = parser.parse_args()

    if options.name is not None:
        folder_name = options.name
    base_path = os.path.join(os.path.join(folder_name, "src"), "foo")

    subprocess.call(["git", "clone", "https://www.github.com/columbustech/map-container-template"])
    shutil.move("map-container-template", folder_name)

    if options.profiler is None:
        print("Please provide a process function with the -f flag")

    shutil.copy(options.profiler, os.path.join(base_path, "process.py"))

    if options.modules is not None:
        shutil.copytree(options.modules, os.path.join(base_path, os.path.dirname(os.path.join(options.modules, ""))))

    if options.requirements is not None:
        req = None
        with open(options.requirements, "r") as f:
            req = f.read()
        with open(os.path.join(os.path.join(folder_name,"src"), "requirements.txt"), "a") as f:
            f.write(req)

    if options.local is not None:
        shutil.copytree(options.local, os.path.join(os.path.join(folder_name, "src"), os.path.dirname(os.path.join(options.local, ""))))

if __name__ == "__main__":
    main()
