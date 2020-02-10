import datetime
import os
import importlib
import timeit

import src.main as hashCodeImpl
# Python scripts runner for various files

DATA_LOCATION = ".\data"
OUTPUT_LOCATION = ".\output"

def run():
    now = datetime.datetime.now()
    print("Hash Code Runner - Welcome to Hash Code", now.year)

    while True:
        print("Please choose an option:")
        files = [f for f in os.listdir(DATA_LOCATION) if os.path.isfile(os.path.join(DATA_LOCATION, f))]
        action = getAction(files)
        importlib.reload(hashCodeImpl)
        
        if action == "allFiles":
            for a_file in files:
                runForFile(os.path.join(DATA_LOCATION, a_file), OUTPUT_LOCATION)
        elif action == "zip":
            zipProject(OUTPUT_LOCATION)
        elif action == "allFilesAndZip":
            for a_file in files:
                runForFile(os.path.join(DATA_LOCATION, a_file), OUTPUT_LOCATION)
            zipProject(OUTPUT_LOCATION)
        elif action == "blank":
            print("")
            continue
        else:
            runForFile(os.path.join(DATA_LOCATION, action), OUTPUT_LOCATION)


def getAction(files):
    options = files.copy()
    count = 1
    for a_file in files:
        print("[" + str(count) + "]", a_file)
        count += 1
    print("[" + str(count) + "]", "All Files")
    options.append("allFiles")
    count += 1
    print("[" + str(count) + "]", "Zip Code")
    options.append("zip")
    count += 1
    print("[" + str(count) + "]", "All files and Zip Code")
    options.append("allFilesAndZip")
    print("")

    choice = input()
    if choice == "":
        return "blank"
    action = options[int(choice)-1]
    return action


def runForFile(file_location, output_location):
    print("Running hash code entry against", file_location)
    start = timeit.timeit()
    hashCodeImpl.main(file_location, output_location)
    end = timeit.timeit()
    print("Ran in:", end - start, "seconds")


def zipProject(output_location):
    print("Zipping project and saving to", output_location)


# When run from the terminal
if __name__ == '__main__':
    run()