# executable-toolbox

Compiles executable files to run conversion and manipulation for pdf, image, and zip files 

Developed for windows machines. Has not been tested on Unix or MacOS

## Steps for Use

1. Set up virtual environment in the cloned repository by following the steps below.
2. Run the `compile_executables.bat` file to compile all executable files.
3. Use an executable file by moving it to within the folder containing files to manipulate.
4. Run the executable file.

## Setting up virtual environment

Good step by step guides are found at the links below: 
- [Virtual Environments for Absolute Beginners: What Is It and How to Create One (Examples)](https://towardsdatascience.com/virtual-environments-for-absolute-beginners-what-is-it-and-how-to-create-one-examples-a48da8982d4b)
- [Virtual Environments](https://towardsdatascience.com/virtual-environments-104c62d48c54)

In short, not using a virtual environment for your project means that all Python packages you have imported are shared across all projects. This can lead to several issues and conflicts, especially when projects are shared between multiple engineers or when you are working on multiple projects simultaneously. In the context of creating executables, it results in all your packages being bundled into unnecessarily large executables with slow load times.

It is best practice to create a virtual environment for each Python project you are working on.

### Creating a Virtual Environment

First, create a virtual environment. Make sure you add venv/ to your `.gitignore` file if you are using Git:
```
python -m venv venv
```
### Activating your Virtual Environment

Activate your environment. On Windows, use:
```
venv\scripts\activate
```
On Unix or MacOS, use:
```
source venv/bin/activate
```
### Viewing Installed Packages

You can see your Python packages in the virtual environment at any time by typing:
```
pip list
```
### Installing Required Packages

Install all packages from the updated requirements file:
```
pip install -r requirements.txt
```
If you run into a error related to a conflict between pathlib and PyInstaller, run the following command:
```
pip uninstall pathlib
```


### Recording Project Details

Record the python version you are using and the complete project requirements:
```
python --version > user_python_version.txt
```
