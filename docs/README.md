import os
import sys

def get_version():
    """Returns the version number from the `version.py` file."""
    version_file = os.path.join(os.path.dirname(__file__), 'version.py')
    with open(version_file, 'r') as f:
        exec(f.read())
    return version

def get_long_description():
    """Returns the long description from the `README.md` file."""
    with open('README.md', 'r') as f:
        return f.read()

def main():
    """Prints the version number and long description."""
    print(f"cache-redis-config version {get_version()}")
    print(get_long_description())

if __name__ == "__main__":
    main()