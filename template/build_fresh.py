import os, time, shutil

# Get the project directory
project_dir = os.getcwd()

toolchain_path = os.path.join( project_dir, "!!**TOOL**!!", "bin" )
if toolchain_path not in os.environ["PATH"]:
    os.environ["PATH"] += os.pathsep + toolchain_path

# Try to delete build directory
try:
    shutil.rmtree( "build" )
    shutil.rmtree( "output" )
except:
    pass
finally:
    os.mkdir( "build" )
    os.mkdir( "output" )

for fl in os.listdir( os.path.join( project_dir, "output" ) ):
    os.remove( os.path.join( project_dir, "output", fl ) )

os.chdir( os.path.join( project_dir, "build" ) )

# Set the environment variable
os.environ["PICO_SDK_PATH"] = os.path.join( project_dir, "pico-sdk" )

# Build the project
os.system( "cmake .." )
os.system( "make" )

for fl in os.listdir( os.path.join( project_dir, "build", "src" ) ):
    if fl.endswith( ".elf") or fl.endswith( ".bin" ) or fl.endswith( ".uf2" ):
        sourceFile = os.path.join( project_dir, "build", "src", fl )
        destinationFile = os.path.join( project_dir, "output", fl )
        shutil.copy( sourceFile, destinationFile )