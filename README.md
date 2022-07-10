# PICO PROJECT BUILDER

Pico project builder can be used to easily create a C/C++ project for raspberry pi pico.

## Requirements

Following items must be preinstalled for running project builder and using the created project. The installation steps are platform dependent.

* python3
* cmake
* git
* Visual Studio (for windows)

Except for the above requirements, no other setup steps are required. The projects created using this project builder contain all the required components - the SDK, the compiler toolchain etc.

## Usage 

You can easily setup a basic pico project using this script. Here is how to use this script :

1. Clone the repository using the below command; you must have git installed on your system. Alternately you may simply download the repository on to your system.

```
git clone https://github.com/parmAshu/pico_project_builder
```

2. Now open a terminal and navigate to the repository. Run the script using the below command; the script will ask you to enter a few details like the directory where you want to create the project and the project name.

```
python3 generate_pico_project.py
```

That's it, you now have a basic pico project ready to be used for any kind of application development.

**Use Visual Studio terminal for running the commands in windows**

## Project Directory Structure

project_root_dir
|
|__inc : This directory contains all user header files
|
|__src : This directory contains all user source files
|
|__output : This directory contains all the build output files
|
|__build : This directory contains build files
|
|__gcc-arm.. : This directory contains the ARM toolchain to build the project

## How to add source files to project ?

1. Add the source file to **src** directory and the header file to **inc** directory.
2. Open the file **src/CMakeLists.txt** and update the **add_executable(main main.c)** to **add_executable( main main.c new_source_file.c)**
3. Now run **python3 build_fresh.py** from the project root directory.

Note : Run the build_fresh once after you add or remove any source files.