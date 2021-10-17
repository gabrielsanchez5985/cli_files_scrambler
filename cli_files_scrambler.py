#!/usr/bin/env python3

"""
CLI files scrambler.


Scramble files by adding a random 5 characters string at the beginning of their names. Designed for CLI use. In pure Python.

File systems order files by their name. By adding a random generated string in each name, you scramble the files randomly. 
Why? Well, maybe you use an old music player that does not randomize music. Or you need to randomize the files for some reason.

Usage:

In Linux, you can run using Python 3 or you can chmod this file to make it executable and run it.

In Microsoft, run using Python 3. Same for MacOS.

Syntax

- Using Python 3
    ```
    > python3 cli_files_scrambler.py --folder "[absolute_folder_path]"
    ```

- chmod
    ```
    > chmod u+x cli_files_scrambler.py

    > ./cli_files_scrambler.py --folder "[absolute_folder_path]"
    ```

"""

from pathlib import Path
import argparse
import os
from random import choices
from string import ascii_letters

def generate_random_5_len_string():
    return "".join(choices(ascii_letters, k=5))

def _files_scrambler(folder: Path):
    """Scrable files in folder by adding a 5 char string at the beginning of their names."""
    
    if not folder.is_dir():
        raise NotADirectoryError(f"Value {folder} is not a directory.")

    os.chdir(folder.absolute())
    
    # Scramble 5 times to improve randomness.
    for file in folder.iterdir():
        _, file_name_and_extension = os.path.split(file.absolute())
        file.rename(generate_random_5_len_string() + "_" + file_name_and_extension)

def _get_args():
    """Get arguments from the CLI."""

    parser = argparse.ArgumentParser("Scramble files in folder by RENAMING them to UUIDs.")

    parser.add_argument(
        "--folder",
        type=Path,
        required=True,
        help="The path to the folder for parsing.",
    )

    return parser.parse_args()

def main():
    args = _get_args()

    # Cool name print
    print(
        """
  _______   ____   ____ __                                  __   __       
 / ___/ /  /  _/  / _(_) /__ ___    ___ ___________ ___ _  / /  / /__ ____
/ /__/ /___/ /   / _/ / / -_|_-<   (_-</ __/ __/ _ `/  ' \/ _ \/ / -_) __/
\___/____/___/  /_//_/_/\__/___/  /___/\__/_/  \_,_/_/_/_/_.__/_/\__/_/   
                                                                          
"""
        )

    _files_scrambler(args.folder)


if __name__ == "__main__":
    main()
