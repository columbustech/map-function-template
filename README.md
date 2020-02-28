## How to use this repo

Clone this repo:
```
git clone https://www.github.com/columbustech/map-function-template
```

Cd into the repo and run gen\_container.py. gen\_container.py will create the folder structure required for building
a map function container.
gen\_container.py takes in 5 arguments:

1. -n, --name :  Name of the output folder. Defaults to mapfn-foo
2. -f, --profiler : Path to a python file containing a 'process' function. The function will take a URL as input and 
return a pandas dataframe. A sample file, process.py has been provided in this repo. This file uses a local module and
a local pip package.
3. -r, --requirements : A requirements.txt file specifying pip packages. To specify a local package, preface with -e.
A sample requirements.txt has been provided in this repo.
4. -m, --modules : Path to folder containing some python files. This folder will be copied to the same location as the
file containing 'process' function, so the 'process' function can refer to functions defined within this folder.
5. -l, --local : Path to a folder containing pip packages to be installed locally. An example pip\_packages folder has
been provided in the repo. The folder contains one package named local\_package.

Sample usage:
```
python gen_container.py -n map1 -f process.py -r requirements.txt -m modules -l pip_packages
```

This will create a folder named map1 (or whatever you pass to the n flag). Cd into map1 and build the image:
```
docker build -t IMAGE_NAME .
```

Assume that Columbus is running at COLUMBUS\_URL. A private image registry will be hosted at 
https://registry.COLUMBUS_URL by the Kubernetes cluster.
Next, you can tag the image accordingly:
```
docker tag IMAGE_NAME registry.COLUMBUS_URL/USERNAME/IMAGE_NAME:latest
```

Then push the image to the image registry:
```
docker push registry.COLUMBUS_URL/USERNAME/IMAGE_NAME:latest
```
