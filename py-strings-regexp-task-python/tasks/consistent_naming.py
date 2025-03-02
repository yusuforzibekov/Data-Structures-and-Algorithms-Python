"""Template for programming assignment: Make naming consistent"""
import re
import keyword

def make_naming_consistent(code: str) -> str:
    """
    Converts the naming of identifiers in Python code
    to the prevailing naming style (snake case or camel case).

    Args:
        code: str, Python code
    Returns:
        str, Python code with consistent naming style
    """
    def is_snake_case(s: str) -> bool:
        return '_' in s  # treat any identifier with '_' as snake case

    def is_camel_case(s: str) -> bool:
        # Consider an identifier camel if it has no underscores and contains uppercase letters or digits.
        return ('_' not in s) and s and (any(c.isupper() for c in s) or any(c.isdigit() for c in s))

    def to_snake_case(s: str) -> str:
        # Handle camelCase patterns
        s = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', s)
        # Handle consecutive capitals
        s = re.sub(r'([A-Z])([A-Z][a-z])', r'\1_\2', s)
        # Handle numbers
        s = re.sub(r'(\d+)', r'_\1_', s)
        return re.sub(r'_+', '_', s).lower().strip('_')

    def to_camel_case(s: str) -> str:
        words = [w for w in s.strip('_').split('_') if w]
        if not words:
            return s
        return words[0].lower() + ''.join(w.capitalize() for w in words[1:])
    
    # Use a list (with duplicates) so frequency is preserved.
    all_ids = re.findall(r'\b[a-zA-Z_]\w*\b', code)
    filtered = [i for i in all_ids if not keyword.iskeyword(i) and (is_snake_case(i) or is_camel_case(i))]
    snake_count = sum(1 for i in filtered if is_snake_case(i))
    camel_count = sum(1 for i in filtered if is_camel_case(i))
    
    # Default to snake if counts are equal
    use_snake = snake_count >= camel_count

    result = code
    # Get unique identifiers from the filtered list
    unique_ids = set(filtered)
    # Sort by length descending to avoid overlapping substring issues.
    for ident in sorted(unique_ids, key=len, reverse=True):
        if use_snake and is_camel_case(ident):
            new_id = to_snake_case(ident)
            pattern = r'(?<!\w)' + re.escape(ident) + r'(?!\w)'
            result = re.sub(pattern, new_id, result)
        elif not use_snake and is_snake_case(ident):
            new_id = to_camel_case(ident)
            pattern = r'(?<!\w)' + re.escape(ident) + r'(?!\w)'
            result = re.sub(pattern, new_id, result)
    
    return result
