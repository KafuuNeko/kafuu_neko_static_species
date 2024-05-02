import os

def scan_directory(directory_path):
    if not os.path.exists(directory_path):
        print(f"Directory does not exist: {directory_path}")
        return
    for filename in os.listdir(directory_path):
        if os.path.isfile(os.path.join(directory_path, filename)):
            base_name, extension = os.path.splitext(filename)
            print(f"portrait{base_name}")

def scan_directory2(directory_path):
    if not os.path.exists(directory_path):
        print(f"Directory does not exist: {directory_path}")
        return
    for filename in os.listdir(directory_path):
        if os.path.isfile(os.path.join(directory_path, filename)):
            base_name, extension = os.path.splitext(filename)
            print(f"portrait{base_name} = {{")
            print(f"    texturefile = \"gfx/models/portraits/maid/{base_name}.dds\"")
            print(f"    clothes_selector = \"no_texture\"")
            print(f"    hair_selector = \"no_texture\"")
            print(f"    greeting_sound = \"human_female_greetings_08\"")
            print(f"}}")

scan_directory('./gfx/models/portraits/maid')
scan_directory2('./gfx/models/portraits/maid')

