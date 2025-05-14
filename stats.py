from collections import defaultdict


def count_words(book_text: str) -> int:
    word_list = book_text.split()
    return len(word_list)


def count_char_freq(book_text: str) -> defaultdict[str, int]:
    char_freq: defaultdict[str, int] = defaultdict(int)
    for c in book_text:
        c = c.lower()
        char_freq[c] += 1
    return char_freq


def sorted_char_freq_dict(book_char_dict: defaultdict[str, int]):
    sorted_book_char_dict_list: list[dict[str, str | int]] = []
    for k, v in book_char_dict.items():
        sorted_book_char_dict_list.append({"char": k, "num": v})

    sorted_book_char_dict_list.sort(key=lambda x: x["num"], reverse=True)
    return sorted_book_char_dict_list
