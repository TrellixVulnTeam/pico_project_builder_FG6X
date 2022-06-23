"""
This script is used to initialize the project for development
"""
import os, time

# LINK TO PICO SDK REPOSITORY
PICO_SDK_LINK = "https://github.com/raspberrypi/pico-sdk.git"
# LINK TO PICO GUIDE REPOSITORY
PICO_GUIDE_LINK = "https://github.com/parmAshu/pico-guide.git"

ACCEPTED_AFFIRMATIVE_RESPONSES = [ "Y", "y", "yes" ]

def affirmative( resp ):
    """
    This function determines if the passed parameter is a valid affirmative response

    Args:
        resp ( str ): response string from user

    Returns:
        Bool : If resp is affirmative response
    """
    if resp in ACCEPTED_AFFIRMATIVE_RESPONSES:
        return True
    else:
        return False

try:
        
    print( "WELCOME TO PICO DEMO APP ..." )

    # Get the current working directory
    CURRENT_DIRECTORY = os.getcwd()

    while True:
        print()
        print("Please provide the working directory: ")
        WORKING_DIRECTORY = input()
        if affirmative( input( "Are you sure ? (Y/N) : " ) ):
            break

    if os.path.exists( WORKING_DIRECTORY ) == False:
        print( "Invalid working directory!" )
        raise Exception

    project_name = ""
    while True:
        project_name = input( "What do you want to call your project ? " )
        if affirmative( input( "Are you sure ? (Y/N) : " ) ):
            break

    print( "Creating project directory : " )
    print( project_name )

    project_dir = os.path.join( WORKING_DIRECTORY , project_name )
    
    os.mkdir( project_dir )
    os.chdir( project_dir )

    print()
    print( "Cloning the required repositories in the project directory ..." )

    os.system( "git clone " + PICO_SDK_LINK )
    os.system( "git clone " + PICO_GUIDE_LINK )

    print()
    print( "Copying the cmake file from sdk..." )

    # Copy the import SDK file 
    with open( os.path.join( project_dir, "pico-sdk", "external", "pico_sdk_import.cmake" ) ) as cmake_file:
        with open( os.path.join( project_dir, "pico_sdk_import.cmake" ), "w" ) as dest_file:
            dest_file.write( cmake_file.read() )
    
    print()
    print( "Creating sub-directories..." )

    # Creating other required directories
    os.mkdir( os.path.join( project_dir, "build" ) )
    os.mkdir( os.path.join( project_dir, "inc" ) )
    os.mkdir( os.path.join( project_dir, "src" ) )
    os.mkdir( os.path.join( project_dir, "output" ) )
    os.mkdir( os.path.join( project_dir, ".vscode" ) )

    print()
    print( "Creating CMakeLists.txt files..." )

    # Creating the top-level cmake file
    with open( os.path.join( CURRENT_DIRECTORY, "template", "CMakeLists_toplevel_template.txt") ) as cmake_template_file:
        with open( os.path.join( project_dir, "CMakeLists.txt") , "w" ) as dest_file:
            dest_file.write( cmake_template_file.read().replace( "!!**PROJECT_NAME**!!", project_name ).replace( "!!**SDK_PATH**!!", os.path.join( project_dir, "pico-sdk" ) ) )

    # Creating inner cmake file
    with open( os.path.join( CURRENT_DIRECTORY, "template", "CMakeLists_src_template.txt") ) as cmake_template_file:
        with open( os.path.join( project_dir, "src", "CMakeLists.txt" ) , "w" ) as dest_file:
            dest_file.write( cmake_template_file.read() )

    print()
    print( "Creating source files..." )

    with open( os.path.join( CURRENT_DIRECTORY, "template", "main.c" ) ) as main_source_file:
        with open( os.path.join( project_dir, "src", "main.c" ), "w" ) as dest_file:
            dest_file.write( main_source_file.read() )

    with open( os.path.join( CURRENT_DIRECTORY, "template", "main.h") ) as main_header_file:
        with open( os.path.join( project_dir, "inc", "main.h" ), "w" ) as dest_file:
            dest_file.write( main_header_file.read() )

    print()
    print( "Creating build scripts..." )

    with open( os.path.join( CURRENT_DIRECTORY, "template", "build_fresh.py" ) ) as build_script:
        with open( os.path.join( project_dir, "build_fresh.py" ), "w" ) as dest_file:
            dest_file.write( build_script.read().replace( "!!**SDK_PATH**!!", os.path.join( project_dir, "pico-sdk" ) ) )
    
    with open( os.path.join( CURRENT_DIRECTORY, "template", "build.py" ) ) as build_script:
        with open( os.path.join( project_dir, "build.py" ), "w" ) as dest_file:
            dest_file.write( build_script.read().replace( "!!**SDK_PATH**!!", os.path.join( project_dir, "pico-sdk" ) ) )

    print()
    print( "Done, happy building!!")

except Exception as e:
    pass
except:
    print( "Bye!!")