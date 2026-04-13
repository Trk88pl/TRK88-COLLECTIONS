 import os

# Supported file extensions
EXTENSIONS = ('.png', '.jpg', '.jpeg', '.gif', '.webp')
README_FILE = 'README.md'
START_MARKER = ''
END_MARKER = ''

def generate_gallery():
    # List files in the root directory
    files = [f for f in os.listdir('.') if f.lower().endswith(EXTENSIONS)]
    files.sort() # Sort alphabetically
    
    gallery_content = "\n"
    
    for f in files:
        repo_name = os.getenv('GITHUB_REPOSITORY')
        # Direct link to the image
        raw_url = f"https://raw.githubusercontent.com/{repo_name}/main/{f}"
        
        gallery_content += f"### File: {f}\n"
        gallery_content += f"![{f}]({f})\n\n"
        gallery_content += f"**Direct Link:**\n`{raw_url}`\n\n"
        gallery_content += "---\n\n"
    
    return gallery_content

if os.path.exists(README_FILE):
    with open(README_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    if START_MARKER in content and END_MARKER in content:
        start_idx = content.find(START_MARKER) + len(START_MARKER)
        end_idx = content.find(END_MARKER)
        new_content = content[:start_idx] + generate_gallery() + content[end_idx:]
        
        with open(README_FILE, 'w', encoding='utf-8') as f:
            f.write(new_content)

