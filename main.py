import json
import yaml
import os
import toml

def guess_file_language(file):
    """Devine le langage du fichier à partir de son extension"""
    
    filename_splitted = os.path.split(file)
    print(filename_splitted)

guess_file_language("music.json")
