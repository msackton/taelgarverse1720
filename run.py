import subprocess
import time
import platform
import psutil
import json
from pathlib import Path
import shutil

# Load config

configfile = "website.json"
with open((configfile), 'r', 2048, "utf-8") as f:
    data = json.load(f)

obs_json_path = 'obsidian-template-config.json'  # Replace with the actual path to obs.json
target_data_path = Path('taelgar', '.obsidian', 'plugins', 'templater-obsidian', 'data.json')  # Replace with the target path

shutil.copy(obs_json_path, target_data_path)

vault_id = data["obsidian_vault_id"]

url_or_file_to_open = 'obsidian://open?vault=' + vault_id
if platform.system() == 'Darwin':  # Checking if the system is macOS
    subprocess.Popen(['open', url_or_file_to_open])
else:
    subprocess.Popen(['start', '', url_or_file_to_open], shell=True)

# Step 2: Wait for the default application to exit
while True:
    try:
        # Check if the process is still running
        if not any(p.name().lower() == 'obsidian.exe' for p in psutil.process_iter(['name'])):
            # The default application has exited
            break
        else:
            time.sleep(1)  # Wait for 1 second before checking again
    except KeyboardInterrupt:
        # Handle keyboard interrupt (Ctrl+C) to exit the script
        break

# Step 3: Run another Python script (export_vault.py)
export_script_path = 'taelgarverse-site-generator/scripts/export_vault.py'  # Replace with the actual path to export_vault.py
subprocess.run(['python', export_script_path])
