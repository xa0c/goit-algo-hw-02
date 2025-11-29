from collections import deque


def is_palindrome(text: str) -> bool:
    """Check if provided text value is palindrome.

    Args:
        text (str): Source text.

    Returns:
        bool: True if palindrome. False otherwise.
    """
    l = [ch for ch in text.lower() if ch != " "]
    q = deque(l)
    for _ in range(len(q) // 2):
        if q.pop() != q.popleft():
            return False
    return True


if __name__ == "__main__":
    texts = [
        "rotor",
        "Anna",
        "Step on no pets",
        "test",
        "І розморозь зором зорі",
    ]
    for text in texts:
        print(f"{text.ljust(40)} {"TRUE" if is_palindrome(text) else "FALSE"}")
