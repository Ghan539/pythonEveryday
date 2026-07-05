import os
from datetime import datetime

print("Welcome to PythonEveryday 🚀")

# Change this only once (the day you started the challenge)
START_DATE = datetime(2026, 7, 5).date()

# Today's date
today = datetime.today().date()

# Calculate current day number
day_number = (today - START_DATE).days + 1

# Folder name
folder_name = f"Day-{day_number:03d}"

# Create folder if it doesn't exist
if os.path.exists(folder_name):
    print(f"📂 {folder_name} already exists.")
else:
    os.mkdir(folder_name)
    print("=" * 40)
    print(f"✅ {folder_name} created successfully!")
    print("🚀 Happy Coding!")
    print("=" * 40)