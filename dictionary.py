import requests
import os
from dotenv import load_dotenv
import requests

# Load environment variables from .env file
load_dotenv()


def search_word_in_dictionary(word: str) -> str:
    api_key = os.getenv("DICTIONARY_TOKEN")
    url = f"https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}"
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if isinstance(data, list):
            if data:
                # Result is the JSON.
                result = data[0]
                return result
            else:
                return "No definition found for the word."
        else:
            return "Invalid response from the API."
    else:
        return "Failed to retrieve data from the API."


def extract_information(word_info: str) -> str:
    word_type = word_info.get("fl", "N/A")
    definitions = []
    sample_sentences = []

    # Extract one definition
    for definition in word_info.get("def", []):
        for sense in definition.get("sseq", []):
            for item in sense:
                if isinstance(item, list) and len(item) >= 2 and item[0] == "sense":
                    for dt in item[1].get("dt", []):
                        if isinstance(dt, list) and len(dt) >= 2 and dt[0] == "text":
                            definitions.append(dt[1])
                            break  # Stop after grabbing one definition
                if len(definitions) >= 1:
                    break
            if len(definitions) >= 1:
                break
        if len(definitions) >= 1:
            break

   
    for sense in word_info.get("def", []):
        for item in sense.get("sseq", []):
            if isinstance(item, list):
                for sub_item in item:
                    if isinstance(sub_item, list) and len(sub_item) >= 2 and sub_item[0] == "sense":
                        if "dt" in sub_item[1] and isinstance(sub_item[1]["dt"], list):
                            for dt in sub_item[1]["dt"]:
                                if isinstance(dt, list) and len(dt) >= 2 and dt[0] == "vis":
                                    for vis in dt[1]:
                                        if isinstance(vis, dict) and "t" in vis:
                                            sample_sentences.append(vis["t"])
                                            if len(sample_sentences) == 2:
                                                break  # Stop after grabbing two sample sentences
                    if len(sample_sentences) == 2:
                        break
            if len(sample_sentences) == 2:
                break

    definitions = ''.join(definitions)
    sample_sentences = ''.join(sample_sentences)

    return word_type, definitions, sample_sentences


# Test main
# def main():
#     word = input("Enter a word to search in the Merriam-Webster Dictionary: ")
#     word_info = search_word_in_dictionary(word)
#     if word_info:
#         word_type, definitions, sample_sentences = extract_information(word_info)
#         print(f"Word Type: {word_type}")
#         print("Definitions:")
#         for definition in definitions:
#             print("-", definition)
#         print("Sample Sentences:")
#         for sentence in sample_sentences:
#             print("-", sentence)
#     else:
#         print("No information found for the word.")

# if __name__ == "__main__":
#     main()
