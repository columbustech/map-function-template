## Instructions

### Creating the required folder structure

Clone this repo:
```
git clone https://www.github.com/columbustech/map-function-template
```

Cd into the repo and run gen\_container.py. gen\_container.py will create the folder structure required for building
a map function container.
gen\_container.py takes in 5 arguments:

1. -n, --name :  Name of the output folder. Defaults to mapfn-foo
2. -f, --profiler : Path to a python file containing a 'process' function. The function will take a URL as input and 
return a pandas dataframe. An example process.py is provided in the repo.
3. -r, --requirements : A requirements.txt file specifying pip packages. An example requirements.txt is provided in the repo.
4. -m, --modules : \[OPTIONAL\] Path to folder containing some python files. An example modules folder is provided in this repo.
5. -l, --local : \[OPTIONAL\] Path to a folder containing pip packages to be installed locally. An example pip\_packages folder has been provided in the repo with 2 packages inside it.

Sample usage:
```
python gen_container.py -n map1 -f process.py -r requirements.txt -m modules -l pip_packages
```

This will create a folder named map1 (or whatever you pass to the n flag). 

A sample 'process' function has been provided in the repo (defined inside process.py). This sample uses a local module and
two local packages. The 'process' function should take a URL as input and return a Pandas dataframe. Other than that, you
are free to write whatever you want in the 'process' function.

### Building and pushing the container image to a private registry

Cd into the folder map1 created by gen_container.py.

Assume that Columbus is running at COLUMBUS\_URL. A private image registry will be hosted at 
https://registry.COLUMBUS_URL by the Kubernetes cluster.

Build the image
```
docker build -t map1 .
```

Tag the image
```
docker tag map1 registry.COLUMBUS_URL/USERNAME/IMAGE_NAME:latest
```

Login into the registry
```
docker login https://registry.COLUMBUS_URL -u REGISTRY_USER -p REGISTRY_PASSWORD
```

Then push the image to the image registry:
```
docker push registry.COLUMBUS_URL/USERNAME/IMAGE_NAME:latest
```
And Done!

## Additional notes:

### Using a package from a .tar.gz or .wl archive
The local package, package2, in this example is built from a .tar.gz archive. To use it, here are the steps:

1. Move the .tar.gz file into a pip_packages folder.
2. Use -l flag while running gen_container.py (eg. -l pip_packages)
3. Add an entry to requirements.txt (Eg. ./pip_packages/package2-0.0.1.tar.gz)
4. Import it in process.py as 'import package2'.

The folder containing the packages does not need to be called pip_packages, it can have any name, but the path to it needs
to be specified in requirements.txt.

### Using a package from source files
The local package, package1, in this example is built from source as a pip package. The steps are same as above, except a
-e flag needs to be added in requirements.txt. (Eg. -e pip_packages/package1)

### Using a local module

1. Specify a folder containing some python files with the -m flag. (Eg. -m modules)
2. Import it in process.py assuming the modules folder is in the same directory as process.py (Eg. from .modules.local_module import test_local_module)
