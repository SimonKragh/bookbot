def get_num_words(text: str) -> int:
    return len(text.split())

def get_number_of_characters(text: str) -> dict[str, int]:
    char_count = {}
    for char in text.lower():
        if char.isalpha():
            if char not in char_count:
                char_count[char] = 0
            char_count[char] += 1
    return char_count

def get_chars_by_frequency(char_count: dict[str, int]) -> list[dict[str, int]]:
    """
    Returns a list of characters sorted by their frequency (most frequent first).
    
    Args:
        text: The input text to analyze
        
    Returns:
        A list of tuples (character, count) sorted by count in descending order
    """
    return sorted(char_count.items(), key=lambda x: x[1], reverse=True)