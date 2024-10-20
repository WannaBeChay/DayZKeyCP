import os
import shutil

# Define source and destination directories
addon_base_dir = 'D:\SteamLibrary\steamapps\common\DayZServer'  # Use double backslashes to avoid escape character issues
keys_dir = os.path.join(addon_base_dir, 'keys')   # The 'keys' folder inside your server directory

# Create 'keys' folder if it doesn't exist
if not os.path.exists(keys_dir):
    os.makedirs(keys_dir)

# Loop through all folders in the addon base directory
for folder_name in os.listdir(addon_base_dir):
    folder_path = os.path.join(addon_base_dir, folder_name)
    
    # Only process if it is a directory (like @modname)
    if os.path.isdir(folder_path):
        # Walk through each addon folder and look for .bikey files
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.endswith('.bikey'):
                    # Full path to the .bikey file
                    file_path = os.path.join(root, file)
                    # Full destination path for the file
                    dest_path = os.path.join(keys_dir, file)

                    # Check if the file already exists in the destination
                    if not os.path.exists(dest_path):
                        # Copy the .bikey file to the 'keys' folder
                        shutil.copy2(file_path, keys_dir)
                        print(f"Copied: \033[92m{file}\033[0m from \033[91m{folder_name}\033[0m")
                    else:
                        print(f"Skipped: \033[92m{file}\033[0m \033[94m(already exists in keys)\033[0m")

print("All .bikey files have been processed.")
