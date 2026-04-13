import os

EXTENSIONS = ('.png', '.jpg', '.jpeg', '.gif', '.webp')
README_FILE = 'README.md'
START_MARKER = ''
END_MARKER = ''

def generate_gallery():
    # Pobierz pliki, ignoruj skrypty i pliki systemowe
    files = [f for f in os.listdir('.') if f.lower().endswith(EXTENSIONS)]
    files.sort()
    
    gallery_content = "\n"
    
    # Pobieranie nazwy repozytorium z environment bota lub ręcznie
    repo = os.getenv('GITHUB_REPOSITORY', 'Trk88pl/TRK88-COLLECTIONS')
    
    for f in files:
        raw_url = f"https://raw.githubusercontent.com/{repo}/main/{f}"
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
    else:
        print("Błąd: Nie znaleziono znaczników w README.md")
else:
    print("Błąd: Nie znaleziono pliku README.md")
