"""Unit tests for string_utils module."""

import unittest
from string_utils import (
    is_palindrome,
    reverse_string,
    slugify,
    to_camel_case,
    to_snake_case,
    truncate,
)


class TestReverseString(unittest.TestCase):
    def test_standard_strings(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("Python 3!"), "!3 nohtyP")

    def test_empty_string(self):
        self.assertEqual(reverse_string(""), "")

    def test_palindrome_remains_same(self):
        self.assertEqual(reverse_string("radar"), "radar")

    def test_invalid_type_raises_error(self):
        with self.assertRaises(TypeError):
            reverse_string(123)  # type: ignore


class TestIsPalindrome(unittest.TestCase):
    def test_simple_palindromes(self):
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("Madam"))

    def test_phrase_palindromes(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama!"))

    def test_non_palindromes(self):
        self.assertFalse(is_palindrome("python"))
        self.assertFalse(is_palindrome("OpenAI"))

    def test_strict_flags(self):
        self.assertFalse(is_palindrome("Madam", ignore_case=False))
        self.assertFalse(is_palindrome("race car", alphanumeric_only=False))

    def test_empty_string(self):
        self.assertTrue(is_palindrome(""))

    def test_invalid_type_raises_error(self):
        with self.assertRaises(TypeError):
            is_palindrome(None)  # type: ignore


class TestToSnakeCase(unittest.TestCase):
    def test_camel_and_pascal(self):
        self.assertEqual(to_snake_case("camelCase"), "camel_case")
        self.assertEqual(to_snake_case("PascalCase"), "pascal_case")

    def test_acronyms(self):
        self.assertEqual(to_snake_case("getHTTPResponseCode"), "get_http_response_code")
        self.assertEqual(to_snake_case("XMLParser"), "xml_parser")

    def test_hyphenated_and_spaced(self):
        self.assertEqual(to_snake_case("hello-world"), "hello_world")
        self.assertEqual(to_snake_case("hello world"), "hello_world")

    def test_already_snake_case(self):
        self.assertEqual(to_snake_case("already_snake_case"), "already_snake_case")

    def test_empty_string(self):
        self.assertEqual(to_snake_case(""), "")

    def test_invalid_type(self):
        with self.assertRaises(TypeError):
            to_snake_case(42)  # type: ignore


class TestToCamelCase(unittest.TestCase):
    def test_snake_case_conversion(self):
        self.assertEqual(to_camel_case("snake_case_string"), "snakeCaseString")
        self.assertEqual(to_camel_case("snake_case_string", pascal=True), "SnakeCaseString")

    def test_kebab_and_spaces(self):
        self.assertEqual(to_camel_case("convert-this-string"), "convertThisString")
        self.assertEqual(to_camel_case("convert this string", pascal=True), "ConvertThisString")

    def test_empty_string(self):
        self.assertEqual(to_camel_case(""), "")

    def test_invalid_type(self):
        with self.assertRaises(TypeError):
            to_camel_case(["not", "a", "string"])  # type: ignore


class TestTruncate(unittest.TestCase):
    def test_within_limit(self):
        self.assertEqual(truncate("Short string", 20), "Short string")

    def test_exact_length(self):
        self.assertEqual(truncate("Exact length", 12), "Exact length")

    def test_truncation_applied(self):
        self.assertEqual(truncate("This is a long sentence.", 10), "This is...")
        self.assertEqual(truncate("Custom suffix test", 10, suffix="~"), "Custom su~")

    def test_invalid_length(self):
        with self.assertRaises(ValueError):
            truncate("Text", 2, suffix="...")

    def test_invalid_types(self):
        with self.assertRaises(TypeError):
            truncate(12345, 10)  # type: ignore
        with self.assertRaises(TypeError):
            truncate("Text", "10")  # type: ignore
        with self.assertRaises(TypeError):
            truncate("Text", 10, suffix=1)  # type: ignore


class TestSlugify(unittest.TestCase):
    def test_standard_slugify(self):
        self.assertEqual(slugify("Hello World!"), "hello-world")

    def test_unicode_normalization(self):
        self.assertEqual(slugify("Café & Résumé"), "cafe-resume")

    def test_special_characters_and_repeated_hyphens(self):
        self.assertEqual(slugify("---Special___Chars---"), "special-chars")
        self.assertEqual(slugify("Multiple   spaces  and---dashes"), "multiple-spaces-and-dashes")

    def test_empty_string(self):
        self.assertEqual(slugify(""), "")

    def test_invalid_type(self):
        with self.assertRaises(TypeError):
            slugify({"key": "val"})  # type: ignore


if __name__ == "__main__":
    unittest.main()