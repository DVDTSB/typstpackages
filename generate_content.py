# generate_content.py
import os

def main():
    # Create the 'content/' folder if it doesn't exist
    os.makedirs("content", exist_ok=True)

    # Generate content and write to 'content/text.md'
    content = "# Generated Content\n\nThis is some generated content."
    with open("content/text.md", "w") as file:
        file.write(content)

if __name__ == "__main__":
    main()
