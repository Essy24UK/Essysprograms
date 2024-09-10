import os
import subprocess
import sys
import zipfile

# Function to locate the current directory where the executables are extracted (for PyInstaller)
def resource_path(relative_path):
    """Get the absolute path to the resource, used for PyInstaller packaging."""
    try:
        # PyInstaller creates a temporary folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Function to run XToolbox executable
def run_xtoolbox():
    xtoolbox_path = resource_path("xtoolbox.exe")
    print(f"Running XToolbox: {xtoolbox_path}")
    subprocess.run([xtoolbox_path])

# Function to run Driver Booster executable
def run_driver_booster():
    driver_booster_path = resource_path("driver_booster.exe")
    print(f"Running Driver Booster: {driver_booster_path}")
    subprocess.run([driver_booster_path])

# Function to run Malwarebytes executable
def run_malwarebytes():
    malwarebytes_path = resource_path("malwarebytes.exe")
    print(f"Running Malwarebytes: {malwarebytes_path}")
    subprocess.run([malwarebytes_path])

# Function to extract Atlas OS Wizard files from a ZIP archive
def extract_atlas_wizard():
    zip_path = resource_path("atlas_os_wizard.zip")  # Your Atlas OS Wizard .zip file
    extract_dir = resource_path("atlas_os_wizard_extracted")  # Directory to extract the files to
    print(f"Extracting Atlas OS Wizard files from: {zip_path}")

    # Check if the extraction directory already exists, if not, create it
    if not os.path.exists(extract_dir):
        os.makedirs(extract_dir)

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)
    
    print(f"Atlas OS Wizard files extracted to: {extract_dir}")

# Function to extract Atlas OS files from a ZIP archive
def extract_atlas_os_files():
    zip_path = resource_path("atlas_os_files.zip")  # Your Atlas OS Files .zip file
    extract_dir = resource_path("atlas_os_files_extracted")  # Directory to extract the files to
    print(f"Extracting Atlas OS files from: {zip_path}")

    # Check if the extraction directory already exists, if not, create it
    if not os.path.exists(extract_dir):
        os.makedirs(extract_dir)

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)
    
    print(f"Atlas OS files extracted to: {extract_dir}")

# Function to open a text file (with default system editor, e.g., Notepad on Windows)
def open_text_file():
    text_file_path = resource_path("file.txt")  # Your .txt file
    print(f"Opening text file: {text_file_path}")
    subprocess.run(["notepad.exe", text_file_path])

# Main menu for the optimization options
def main_menu():
    while True:
        print("\n=== Essy's PC Optimization Menu ===")
        print("1. Run XToolbox")
        print("2. Run Driver Booster")
        print("3. Run Malwarebytes")
        print("4. Extract Atlas OS Wizard")
        print("5. Extract Atlas OS Files")
        print("6. Powershell Optimisation Script")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            run_xtoolbox()
        elif choice == "2":
            run_driver_booster()
        elif choice == "3":
            run_malwarebytes()
        elif choice == "4":
            extract_atlas_wizard()
        elif choice == "5":
            extract_atlas_os_files()
        elif choice == "6":
            open_text_file()
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select an option between 1 and 7.")

if __name__ == "__main__":
    main_menu()
