###############################
##
# HASH CODE ENTRY
##
# Usage: python main.py <path_to_source_file> <output_location>
##
###############################
import os
import sys

# Import additional files by saving them in this folder and importing
# them relative to this file. e.g: from myFile import my_function

def get_file_name_from_location(file_location):
    # 
    # Give the input file location, return the file name
    # excluding the file type identifier
    #  
    return os.path.basename(file_location).split(".")[0]


def run(file_location, output_location):
    print("Running Hash Code Entry")
    # Hash Code here :)
    
    # ----- SAMPLE: Read the input file -----
    # input_file = open(file_location, "r")
    # for line in input_file:
    #     # Do Something
    # input_file.close()
    # ---------------------------------------


    # ----- SAMPLE: Write out results -----
    # output_file = open(output_location, "w")
    # # Write to file here
    # output_file.write(f"{"Something"}\n")
    # output_file.close()
    # ------------------------------------


# When run from the terminal
if __name__ == '__main__':
    run(sys.argv[1], sys.argv[2])
