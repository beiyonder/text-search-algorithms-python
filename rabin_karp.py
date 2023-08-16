def rabin_karp_search(pattern, text):
    """
    Perform substring search using the Rabin-Karp algorithm.

    Args:
        pattern (str): The pattern to search for.
        text (str): The text in which to search for the pattern.

    Returns:
        bool: True if pattern is found, False otherwise.
    """
    d = 256  # Number of characters in the input alphabet
    q = 101  # A prime number for hash calculation
    m = len(pattern)
    n = len(text)
    p_hash = 0  # Hash value for the pattern
    t_hash = 0  # Hash value for the current window of text

    # Calculate the hash value of the pattern and the initial window of text
    for i in range(m):
        p_hash = (d * p_hash + ord(pattern[i])) % q
        t_hash = (d * t_hash + ord(text[i])) % q

    for i in range(n - m + 1):
        # Check if the hash values match, then verify character by character
        if p_hash == t_hash:
            if text[i:i + m] == pattern:
                return True
        # Update the hash value for the next window of text
        if i < n - m:
            t_hash = (d * (t_hash - ord(text[i]) * (d ** (m - 1))) + ord(text[i + m])) % q
            if t_hash < 0:
                t_hash += q

    return False  # Pattern not found in the text

def execute_rabin_karp(pat, text):
    """
    Execute the Rabin-Karp substring search and return the result.

    Args:
        pat (str): The pattern to search for.
        text (str): The text in which to search for the pattern.

    Returns:
        bool: True if pattern is found, False otherwise.
    """
    result = rabin_karp_search(pat, text)
    return result

# Main program
# text = "This is an example text."
# pattern = "example"

# result = execute_rabin_karp(pattern, text)

# if result:
#     print("Pattern found in the text.")
# else:
#     print("Pattern not found in the text.")
