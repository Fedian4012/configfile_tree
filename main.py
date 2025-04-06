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

def main():
    file = "data.toml"
    language_of_file = guess_file_language(file)     
    print(read_file_by_language(file, language_of_file))

if __name__ == "__main__":
    main()
