import requests

def find_word_dictionary(word: str) -> str:
    
    url = f"https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key=your-api-key"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()

        if isinstance(data, list):
            if data:
                result = data[0]
                return result
            else:
                return "No definition found for the word."
        else:
            return "Invalid response from the API."
    else:
        return "Failed to retrieve data from the API."