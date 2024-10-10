import os
from colorama import Fore, Style

# Import colorama and initialize it
import colorama
colorama.init()

# Dictionary of file signatures and their corresponding file types
signatures_dict = {
    "gif": ["47494638", "474946383761", "474946383961", "4749463839", "4749463837"],
    "jpg": ["FFD8FFDB", "FFD8FFE0", "FFD8FFEE", "FFD8FFE000"],
    "zip": ["504B0304", "504B0506", "504B0708"],
    "pdf": ["255044462D", "25504446"],
    "wav": ["52494646"],
    "mp3": ["FFFB", "FFF3", "FFF2", "494433"],
    "bmp": ["424D", "424D38040C"],
    "iso": ["4344303031"],
    "midi": ["4D546864"],
    "dmg": ["6B6F6C79"],
    "gzip": ["1F8B"],
    "xml": ["3C3F786D6C20"],
    "rtf": ["7B5C72746631"],
    "mpg": ["000001B3"],
    "dat": ["72656766"],
    "png": ["89504E470D"],
    "doc": ["D0CF", "D0CF11E0A1B11AE100", "D0CF11E0A1"],
    "eml": ["46726F6D"],
    "exe": ["4D5A", "4D5A500002"],
    "webm": ["1A45DFA3"],
    "mov": ["736B6970", "0000001466"],
    "mp4": ["0000001C66"],
    "docx": ["504B030414"],
    "odt": ["504B030414"],
    "txt": ["5457205365"],
    "pages": ["504B030414"],
    "pptx": ["504B030414"],
    "py": ["696D706F72"]
}

# Function to compare actual and expected signatures and print results with color
def compare_signatures(filepath, actual_signature, expected_signatures, match_status):
    if match_status == "N/A":
        print(f"{Fore.MAGENTA}{filepath}\nActual: {actual_signature}\nExpected: {', '.join(expected_signatures)}\nMatch: {match_status}{Style.RESET_ALL}\n")
    elif match_status == "True":
        print(f"{Fore.GREEN}{filepath}\nActual: {actual_signature}\nExpected: {', '.join(expected_signatures)}\nMatch: {match_status}{Style.RESET_ALL}\n")
    else:
        print(f"{Fore.RED}{filepath}\nActual: {actual_signature}\nExpected: {', '.join(expected_signatures)}\nMatch: {match_status}{Style.RESET_ALL}\n")

# Prompt the user for the drive letter/directory
drive_letter = input("Enter the drive letter (e.g., C:) or directory path to search through: ")

# Walk through the directory and subdirectories
for subdir, dirs, files in os.walk(drive_letter):
    for file in files:
        filepath = os.path.join(subdir, file)

        # Open the file in binary mode
        with open(filepath, 'rb') as fp:
            hex_list = fp.read()

            # Convert the first 5 bytes to hexadecimal format
            out_hex = ''.join(f"{b:02X}" for b in hex_list[:5])

            # Get the file extension from the file name
            file_extension = os.path.splitext(file)[1].lstrip(".")

            # Check if the file extension corresponds to a signature in the dictionary
            expected_signatures = signatures_dict.get(file_extension, [])

            # Check if the actual signature matches any of the expected signatures
            match_status = "N/A" if not expected_signatures else "True" if out_hex in expected_signatures else "False"
            compare_signatures(filepath, out_hex, expected_signatures, match_status)

            fp.close()
