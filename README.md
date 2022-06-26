# PICO PROJECT BUILDER

Pico project builder can be used to easily create a C/C++ project for raspberry pi pico.

## Requirements

Following items must be preinstalled for running project builder and using the created project. The installation steps are platform dependent.

* python3
* cmake
* git

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