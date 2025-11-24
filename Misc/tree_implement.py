dct = { 
    "Desktop": ["practice_folder", "tests"],
    "Documents": ["workfiles", "home_files"],
    "practice_folder": ["xyz.png", "resume.txt"]
}

def print_tree(key, indent=""):
    print(indent + "-" + key) 
    

    if key in dct:
        for item in dct[key]:
            print_tree(item, indent + "-")  

for root in dct:
    is_sub = any(root in v for v in dct.values())
    if not is_sub:
        print_tree(root)
