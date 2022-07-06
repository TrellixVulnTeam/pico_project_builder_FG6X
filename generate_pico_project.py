"""
This script creates a pico C/C++ project
"""
import os, time, json, requests, platform, progressbar
from urllib import request

# LINK TO PICO SDK REPOSITORY
PICO_SDK_LINK = "https://github.com/raspberrypi/pico-sdk.git"
# LINK TO PICO GUIDE REPOSITORY
PICO_GUIDE_LINK = "https://github.com/parmAshu/pico-guide.git"
# GET THE SYSTEM
SYSTEM_OS = platform.system()

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

pbar = None

def show_progress(block_num, block_size, total_size):

    global pbar
    if pbar is None:
        pbar = progressbar.ProgressBar(maxval=total_size)
        pbar.start()

    downloaded = block_num * block_size
    if downloaded < total_size:
        pbar.update(downloaded)
    else:
        pbar.finish()
        pbar = None

try:
        
    print( "WELCOME TO PICO APP BUILDER..." )

    # Get the current working directory
    CURRENT_DIRECTORY = os.getcwd()

    # Get the location for project
    while True:
        print()
        print("Please provide the working directory: ")
        WORKING_DIRECTORY = input()
        if affirmative( input( "Are you sure ? (Y/N) : " ) ):
            break
    if os.path.exists( WORKING_DIRECTORY ) == False:
        print( "Invalid working directory!" )
        raise Exception

    # Get the project name
    project_name = ""
    while True:
        project_name = input( "What do you want to call your project ? " )
        if affirmative( input( "Are you sure ? (Y/N) : " ) ):
            break

    # Creating the project directory and navigating to it
    print( "Creating project directory : " )
    print( project_name )
    project_dir = os.path.join( WORKING_DIRECTORY , project_name )
    os.mkdir( project_dir )
    os.chdir( project_dir )

    # Parsing the guide
    guide_string = ""
    with open( os.path.join( CURRENT_DIRECTORY, "template", "guide.json" ) ) as guide_file:
        guide_string = guide_file.read()
    guide_obj = json.loads( guide_string )

    # Obtaining the toolchain links
    TOOLCHAIN_LINK_MAC = guide_obj["toolchain"]["darwin"]
    TOOLCHAIN_LINK_LIN = guide_obj["toolchain"]["linux"]
    TOOLCHAIN_LINK_WIN = guide_obj["toolchain"]["windows"]

    # Download the toolchain and extract it within the project directory
    print()
    print( "Downloading the toolchain; be patient, it takes time!" )
    download_file_name = ""
    download_link = ""
    extract_command = ""
    if "Win" in SYSTEM_OS:
        download_link = TOOLCHAIN_LINK_WIN
        download_file_name = TOOLCHAIN_LINK_WIN.split( "/" )[-1]
        extract_command = "powershell.exe Expand-Archive -LiteralPath " + download_file_name + " -DestinationPath " + download_file_name.split(".")[0]
    elif "Lin" in SYSTEM_OS:
        download_link = TOOLCHAIN_LINK_LIN
        download_file_name = TOOLCHAIN_LINK_LIN.split( "/" )[-1]
        extract_command = "tar -xvf " + download_file_name
    elif "Dar" in SYSTEM_OS:
        download_link = TOOLCHAIN_LINK_MAC
        download_file_name = TOOLCHAIN_LINK_MAC.split( "/" )[-1]
        extract_command = "tar -xvf " + download_file_name
    request.urlretrieve( download_link, download_file_name, show_progress )
    os.system( extract_command )
    TOOL_DIR = ""
    for item in os.listdir( project_dir ):
        if "arm" in item:
            TOOL_DIR = item
    os.remove( os.path.join( project_dir, download_file_name ) )

    # Cloning the PICO SDK
    print()
    print( "Getting the SDK..." )
    os.system( "git clone " + PICO_SDK_LINK )

    # Create the CMake files
    print()
    print( "Copying the cmake file from sdk..." )
    with open( os.path.join( project_dir, "pico-sdk", "external", "pico_sdk_import.cmake" ) ) as cmake_file:
        with open( os.path.join( project_dir, "pico_sdk_import.cmake" ), "w" ) as dest_file:
            dest_file.write( cmake_file.read() )
    
    # Creating the project structure 
    print()
    print( "Creating sub-directories..." )
    os.mkdir( os.path.join( project_dir, "build" ) )
    os.mkdir( os.path.join( project_dir, "inc" ) )
    os.mkdir( os.path.join( project_dir, "src" ) )
    os.mkdir( os.path.join( project_dir, "output" ) )
    for obj in guide_obj[ "files" ]:
        source_file_name = obj[ "template_name" ]
        dest_file_name = obj[ "dest_name" ]
        source_file = open( os.path.join( CURRENT_DIRECTORY, "template", source_file_name ) )
        dest_file = open( os.path.join( project_dir, dest_file_name ), "w" )
        
        source_string = source_file.read()
        for edit in obj["edit"]:
            edit_value = ""
            if edit[1] == "pico_sdk_path":
                edit_value = os.path.join( project_dir, "pico-sdk" )
            elif edit[1] == "project_name":
                edit_value = project_name
            elif edit[1] == "toolchain":
                edit_value = TOOL_DIR
            source_string = source_string.replace( edit[0], edit_value )

        dest_file.write( source_string )
        source_file.close()
        dest_file.close()

    print()
    print( "Done, happy building!!")

except Exception as e:
    raise e
finally:
    print( "Bye!!")