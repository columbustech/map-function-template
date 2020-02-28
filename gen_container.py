import argparse, os, subprocess

folder_name = "mapfn-foo"

parser = argparse.ArgumentParser(description="Generate Dockerfile for container")
parser.add_argument("-n", "--name", help="Folder name")
parser.add_argument("-f", "--profiler", help="Profiling function")
parser.add_argument("-r", "--requirements", help="Pip requirements file")
parser.add_argument("-m", "--modules", help="Additional python modules folder")
parser.add_argument("-l", "--local", help="Path to local pip packages")
options = parser.parse_args()

base_path = os.path.join(os.path.join(options.name, "src"), "foo")

project_name = None
if options.name is not None:
    project_name = options.name

subprocess.call(["git", "clone", "https://www.github.com/columbustech/mapfn-test"])
subprocess.call(["mv", "mapfn-test", options.name])
subprocess.call(["cp", options.profiler, os.path.join(base_path, "process.py")])

if options.modules is not None:
    subprocess.call(["cp", "-r", options.modules, base_path])

if options.requirements is not None:
    req = None
    with open(options.requirements, "r") as f:
        req = f.read()
    with open(os.path.join(options.name, "requirements.txt"), "a") as f:
        f.write(req)

if options.local is not None:
    subprocess.call(["cp", "-r", options.local, options.name])
