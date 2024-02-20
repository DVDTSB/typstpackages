# generate_content.py

def main():
    content = "# Generated Content\n\nThis is some generated content."
    with open("content/text.md", "w") as file:
        file.write(content)

if __name__ == "__main__":
    main()
