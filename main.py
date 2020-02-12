import datetime
import os
import importlib
import timeit
import zipfile

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
        
        if action == "allFiles":
            for a_file in files:
                runForFile(os.path.join(DATA_LOCATION, a_file), OUTPUT_LOCATION)
        elif action == "zip":
            zipProject(OUTPUT_LOCATION)
        elif action == "allFilesAndZip":
            for a_file in files:
                runForFile(os.path.join(DATA_LOCATION, a_file), OUTPUT_LOCATION)
            zipProject(OUTPUT_LOCATION)
        else:
            runForFile(os.path.join(DATA_LOCATION, action), OUTPUT_LOCATION)


def getAction(files):
    options = files.copy()
    count = 1
    for a_file in files:
        print("[" + str(count) + "]", a_file)
        count += 1
    print("[" + str(count) + "]", "Run for all Files")
    options.append("allFiles")
    count += 1
    print("[" + str(count) + "]", "Zip source")
    options.append("zip")
    count += 1
    print("[" + str(count) + "]", "Run for all files and zip source")
    options.append("allFilesAndZip")

    choice = ""
    while choice == "":
       print("")
       # Reload our source incase we have made any changes
       importlib.reload(hashCodeImpl)
       choice = input()
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
    now = datetime.datetime.now()

    zipf = zipfile.ZipFile(OUTPUT_LOCATION + "\hashCode" + str(now.year) + ".zip", "w", zipfile.ZIP_DEFLATED)
    # Add our Pipfile, so any deps can be downloaded
    zipf.write(".\Pipfile")
    zipf.write(".\Pipfile.lock")
    for root, dirs, files in os.walk(".\src"):
        for file in files:
            filename = os.path.join(root, file)
            # Ignore the top level init file, as this is only needed by the code runner
            if filename != ".\src\__init__.py":
                zipf.write(filename, filename.replace(".\src\\", ".\\"))
    zipf.close()


# When run from the terminal
if __name__ == '__main__':
    run()