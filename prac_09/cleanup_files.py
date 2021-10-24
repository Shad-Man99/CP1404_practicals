import os


def main():
    """Cleanup inconsistent song lyrics file name"""
    # Change to desired directory
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("Contains Subdirectories:", subdirectories)
        print("And Files:", filenames)
        print("Current working directory is: {}".format(os.getcwd()))

        for filename in filenames:
            new_name = get_fixed_filename(filename)
            print("Rename: {} to {}".format(filename, new_name))

            full_name = os.path.join(directory_name, filename)
            new_name = os.path.join(directory_name, new_name)
            os.rename(full_name, new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    return new_name


main()