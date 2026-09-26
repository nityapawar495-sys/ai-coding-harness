"""General string manipulation utilities."""

from __future__ import annotations

import re
import unicodedata


def reverse_string(s: str) -> str:
    """Reverse the given string.

    Args:
        s: Input string.

    Returns:
        The reversed string.

    Raises:
        TypeError: If input is not a string.
    """
    if not isinstance(s, str):
        raise TypeError(f"Expected str, got {type(s).__name__}")
    return s[::-1]


def is_palindrome(s: str, ignore_case: bool = True, alphanumeric_only: bool = True) -> bool:
    """Check if the given string is a palindrome.

    Args:
        s: Input string to test.
        ignore_case: Whether to disregard case sensitivity.
        alphanumeric_only: Whether to disregard non-alphanumeric characters.

    Returns:
        True if string is a palindrome, False otherwise.

    Raises:
        TypeError: If input is not a string.
    """
    if not isinstance(s, str):
        raise TypeError(f"Expected str, got {type(s).__name__}")

    processed = s
    if alphanumeric_only:
        processed = "".join(ch for ch in processed if ch.isalnum())
    if ignore_case:
        processed = processed.lower()

    return processed == processed[::-1]


def to_snake_case(s: str) -> str:
    """Convert camelCase, PascalCase, or kebab-case to snake_case.

    Args:
        s: Input string.

    Returns:
        The snake_case formatted string.

    Raises:
        TypeError: If input is not a string.
    """
    if not isinstance(s, str):
        raise TypeError(f"Expected str, got {type(s).__name__}")

    if not s:
        return ""

    # Replace hyphens and spaces with underscores
    cleaned = re.sub(r"[\s\-]+", "_", s)
    # Insert underscore between lower/digit and upper
    cleaned = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", cleaned)
    # Insert underscore before trailing sequence of capitals (e.g., XMLParser -> xml_parser)
    cleaned = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", cleaned)
    # Collapse consecutive underscores and strip leading/trailing underscores
    cleaned = re.sub(r"_+", "_", cleaned)
    return cleaned.strip("_").lower()


def to_camel_case(s: str, pascal: bool = False) -> str:
    """Convert snake_case, kebab-case, or spaced strings to camelCase or PascalCase.

    Args:
        s: Input string.
        pascal: If True, returns PascalCase; otherwise camelCase.

    Returns:
        Formatted camelCase or PascalCase string.

    Raises:
        TypeError: If input is not a string.
    """
    if not isinstance(s, str):
        raise TypeError(f"Expected str, got {type(s).__name__}")

    tokens = [token for token in re.split(r"[\s_\-]+", s) if token]
    if not tokens:
        return ""

    capitalized = [token.capitalize() for token in tokens]
    if not pascal:
        capitalized[0] = capitalized[0].lower()

    return "".join(capitalized)


def truncate(s: str, max_length: int, suffix: str = "...") -> str:
    """Truncate a string to a specified length including suffix length.

    Args:
        s: Input string.
        max_length: Maximum allowed length of returned string.
        suffix: Suffix appended when truncation occurs (default: '...').

    Returns:
        Truncated string.

    Raises:
        TypeError: If s or suffix is not a string, or max_length is not an integer.
        ValueError: If max_length is less than the length of suffix.
    """
    if not isinstance(s, str):
        raise TypeError(f"Expected str for 's', got {type(s).__name__}")
    if not isinstance(suffix, str):
        raise TypeError(f"Expected str for 'suffix', got {type(suffix).__name__}")
    if not isinstance(max_length, int):
        raise TypeError(f"Expected int for 'max_length', got {type(max_length).__name__}")

    if max_length < len(suffix):
        raise ValueError(
            f"max_length ({max_length}) cannot be smaller than suffix length ({len(suffix)})"
        )

    if len(s) <= max_length:
        return s

    cut_index = max_length - len(suffix)
    return s[:cut_index] + suffix


def slugify(s: str) -> str:
    """Generate an ASCII-only URL-safe slug from a string.

    Args:
        s: Input string.

    Returns:
        Normalized URL slug.

    Raises:
        TypeError: If input is not a string.
    """
    if not isinstance(s, str):
        raise TypeError(f"Expected str, got {type(s).__name__}")

    # Normalize unicode to decomposed form (NFKD) and encode to ASCII
    normalized = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode("ascii")
    # Replace non-word characters with hyphen
    cleaned = re.sub(r"[^\w\s-]", "", normalized).strip().lower()
    # Replace spaces/underscores with hyphens and collapse multiple hyphens
    return re.sub(r"[-\s_]+", "-", cleaned).strip("-")