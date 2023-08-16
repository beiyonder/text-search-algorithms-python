def compute_lps(pat):
    """
    Compute the Longest Prefix Suffix (LPS) array for the given pattern.

    Args:
        pat (str): The pattern for which LPS array needs to be computed.

    Returns:
        list: The computed LPS array.
    """
    m = len(pat)
    lps = [0] * m  # Initialize the LPS array with zeros
    j = 0  # Length of the previous longest prefix suffix

    for i in range(1, m):
        # Update j based on matching or mismatching characters
        while j > 0 and pat[i] != pat[j]:
            j = lps[j - 1]
        if pat[i] == pat[j]:
            j += 1
        lps[i] = j

    return lps

def kmp_search(pat, text):
    """
    Perform substring search using the Knuth-Morris-Pratt (KMP) algorithm.

    Args:
        pat (str): The pattern to search for.
        text (str): The text in which to search for the pattern.

    Returns:
        bool: True if pattern is found, False otherwise.
    """
    m = len(pat)
    n = len(text)
    lps = compute_lps(pat)  # Calculate the LPS array for the pattern

    i = 0  # Index for the text
    j = 0  # Index for the pattern

    while i < n:
        # If characters match, advance both pointers
        if pat[j] == text[i]:
            i += 1
            j += 1
            # If the entire pattern is found, return True
            if j == m:
                return True
        else:
            # If there is a mismatch, update j based on the LPS array
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return False  # Pattern not found in the text

def execute_kmp(pat, text):
    """
    Execute the KMP substring search and return the result.

    Args:
        pat (str): The pattern to search for.
        text (str): The text in which to search for the pattern.

    Returns:
        bool: True if pattern is found, False otherwise.
    """
    result = kmp_search(pat, text)
    return result

# local Testing of the above functions:  
# text = "This is an example text."
# pattern = "example"

# result = execute_kmp(pattern, text)

# if result:
#     print("Pattern found in the text.")
# else:
#     print("Pattern not found in the text.")
