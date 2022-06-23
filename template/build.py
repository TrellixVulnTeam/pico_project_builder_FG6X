import os, time, shutil

# Get the project directory
project_dir = os.getcwd()

for fl in os.listdir( os.path.join( project_dir, "output" ) ):
    os.remove( os.path.join( project_dir, "output", fl ) )

os.chdir( os.path.join( project_dir, "build" ) )

# Set the environment variable
os.environ["PICO_SDK_PATH"] = "!!**PICO_SDK_PATH**!!"

# Build the project
os.system( "cmake .." )
os.system( "make" )

for fl in os.listdir( os.path.join( project_dir, "build", "src" ) ):
    if fl.endswith( ".elf") or fl.endswith( ".bin" ) or fl.endswith( ".uf2" ):
        sourceFile = os.path.join( project_dir, "build", "src", fl )
        destinationFile = os.path.join( project_dir, "output", fl )
        shutil.copy( sourceFile, destinationFile )