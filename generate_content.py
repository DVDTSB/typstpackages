# generate_content.py
import os

def main():
    # Create the 'content/' folder if it doesn't exist
    os.makedirs("content", exist_ok=True)

    # Get folder names in 'packages' directory
    packages_dir = "packages"
    folder_names = [f for f in os.listdir(packages_dir) if os.path.isdir(os.path.join(packages_dir, f))]

    # Generate content and write to 'content/folders.md'
    content = "# Folders in 'packages' Directory\n\n"
    for folder_name in folder_names:
        content += f"- {folder_name}\n"

    with open("content/folders.md", "w") as file:
        file.write(content)

if __name__ == "__main__":
    main()
