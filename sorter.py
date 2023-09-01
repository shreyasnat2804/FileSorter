import os
import shutil

# Specify the source folder (Downloads) and destination folders (Desktop)
downloads_folder = os.path.expanduser("~/Downloads")
desktop_folder = os.path.expanduser("/Users/shreyasnatarajan/Desktop/Resume Stuff")

# Create target folders for Cover Letters and Resumes on the desktop
cover_letter_folder = os.path.join(desktop_folder, "Cover Letters")
resume_folder = os.path.join(desktop_folder, "Resumes")

# Ensure the target folders exist or create them if they don't
for folder in [cover_letter_folder, resume_folder]:
    if not os.path.exists(folder):
        os.makedirs(folder)

# Iterate through the files in the Downloads folder
for filename in os.listdir(downloads_folder):
    source_path = os.path.join(downloads_folder, filename)

    if filename.startswith("Cover Letter"):
        destination_path = os.path.join(cover_letter_folder, filename)
    elif filename.startswith("Resume"):
        destination_path = os.path.join(resume_folder, filename)
    else:
        # Skip files that don't match either criteria
        continue

    try:
        # Move the file to the appropriate folder
        shutil.move(source_path, destination_path)
        print(f"Moved '{filename}' to '{destination_path}'")
    except Exception as e:
        print(f"Error moving '{filename}': {e}")
