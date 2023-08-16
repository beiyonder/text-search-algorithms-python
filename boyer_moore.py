def bad_character_table(pattern):
    """
    Create a bad character table for the Boyer-Moore algorithm.

    Args:
        pattern (str): The pattern for which the table needs to be created.

    Returns:
        dict: The bad character table with characters as keys and shifts as values.
    """
    table = {}
    m = len(pattern)
    for i in range(m - 1):
        table[pattern[i]] = m - 1 - i
    return table

def boyer_moore_search(pattern, text):
    """
    Perform substring search using the Boyer-Moore algorithm.

    Args:
        pattern (str): The pattern to search for.
        text (str): The text in which to search for the pattern.

    Returns:
        bool: True if pattern is found, False otherwise.
    """
    m = len(pattern)
    n = len(text)
    bc_table = bad_character_table(pattern)  # Create the bad character table

    i = m - 1  # Index for the text
    j = m - 1  # Index for the pattern

    while i < n:
        # If characters match, move both pointers towards the beginning
        if pattern[j] == text[i]:
            if j == 0:
                return True  # Pattern found
            i -= 1
            j -= 1
        else:
            # Calculate the shift based on the bad character table
            if text[i] in bc_table:
                shift = bc_table[text[i]]
            else:
                shift = m
            i += shift
            j = m - 1

    return False  # Pattern not found in the text

def execute_boyer_moore(pat, text):
    """
    Execute the Boyer-Moore substring search and return the result.

    Args:
        pat (str): The pattern to search for.
        text (str): The text in which to search for the pattern.

    Returns:
        bool: True if pattern is found, False otherwise.
    """
    result = boyer_moore_search(pat, text)
    return result

# Main program
# text = "This is an example text."
# pattern = "exale"

# result = execute_boyer_moore(pattern, text)

# if result:
#     print("Pattern found in the text.")
# else:
#     print("Pattern not found in the text.")
