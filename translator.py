
from letters import letters


digits_to_letter = {v: k for k, v in letters.items()}

async def encode(string: str) -> str:
    return "  ".join(
        " ".join(letters[c] for c in word.lower() if c in letters)
        for word in string.split()
    )

async def decode(encoded: str) -> str:
    words = encoded.split("  ")
    decoded_words = []
    for word in words:
        letters_list = word.split()
        decoded_word = "".join(digits_to_letter.get(code, "?") for code in letters_list)
        decoded_words.append(decoded_word)
    return " ".join(decoded_words)
