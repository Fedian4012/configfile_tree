#!/usr/bin/python3

import json
import os
import sys
import yaml

def guess_file_language(file):
    """Devine le langage du fichier à partir de son extension"""
    
    extension = os.path.splitext(file)[1].lower()
    match extension:
        case ".json":
            language = "json"
        case ".yaml"|".yml":
            language = "yaml"
        case _:
            language = "inconnu"
    return language

def read_file_by_language(file, language):
    """Lit le fichier en fonction de son langage"""
    
    with open(file, "r") as input_file:
        match language:
            case "json":
                data = json.load(input_file)
            case "yaml":
                data = yaml.safe_load(input_file)
    return data

def print_tree(data, prefix=""):
    """Affiche l'arborescence du dictionnaire"""
    if isinstance(data, dict):
        keys = list(data.keys())
        for index, key in enumerate(keys):
            is_last = index == len(keys) - 1
            connector = "└── " if is_last else "├── "
            print(prefix + connector + str(key) + ":")
            next_prefix = prefix + ("    " if is_last else "│   ")
            print_tree(data[key], prefix=next_prefix)

    elif isinstance(data, list):
        for index, item in enumerate(data):
            is_last = index == len(data) - 1
            connector = "└── " if is_last else "├── "
            print(prefix + connector + f"[{index}]")
            next_prefix = prefix + ("    " if is_last else "│   ")
            print_tree(item, prefix=next_prefix)

    else:
        print(prefix + str(data))

def main():
    file = sys.argv[1]
    language_of_file = guess_file_language(file)
    
    if language_of_file == "inconnu":
        raise SystemExit("Langage non supporté")     
    data = read_file_by_language(file, language_of_file)
    print_tree(data)

if __name__ == "__main__":
    main()
