
from letters import letters

async def translate(string: str) -> str:
    encoded_words = []
    for word in string.split():
        encoded_word = " ".join(letters[c] for c in word.lower() if c in letters)
        encoded_words.append(encoded_word)
    return "    ".join(encoded_words)