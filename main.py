import datetime
from os import listdir
from os.path import isfile, join
# Python scripts runner for various files

DATA_LOCATION = ".\data"
OUTPUT_LOCATION = ".\output"

def main():
    now = datetime.datetime.now()
    print("Hash Code Runner - Welcome to Hash Code", now.year)

    while True:
        print("Please choose an option:")
        files = [f for f in listdir(DATA_LOCATION) if isfile(join(DATA_LOCATION, f))]
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
        action = options[int(choice)-1]
        
        if action == "allFiles":
            for a_file in files:
                runForFile(join(DATA_LOCATION, a_file), OUTPUT_LOCATION)
        elif action == "zip":
            zipProject(OUTPUT_LOCATION)
        elif action == "allFilesAndZip":
            for a_file in files:
                runForFile(join(DATA_LOCATION, a_file), OUTPUT_LOCATION)
            zipProject(OUTPUT_LOCATION)
        else:
            runForFile(join(DATA_LOCATION, action), OUTPUT_LOCATION)


def runForFile(file_location, output_location):
    print("Running hash code entry against", file_location)


def zipProject(output_location):
    print("Zipping project and saving to", output_location)


# When run from the terminal
if __name__ == '__main__':
    main()