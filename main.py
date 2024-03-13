def main():
    book_path = "books/frankenstein.txt"
    report(book_path)


def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()


def count_words(text):
    return len(text.split())


def count_letters(text):
    lowercase_text = text.lower()
    answer = {}
    lowercase_text = lowercase_text.replace(" ", "")
    for letter in lowercase_text:
        if letter in answer:
            answer[letter] += 1
        else:
            answer[letter] = 1
    return answer


def dict_to_list(d):
    return [{"letter": k, "count": v} for k, v in d.items()]


def sort_on(dict):
    return dict["count"]


def report(book_path):
    text = get_book_text(book_path)
    number_of_words = count_words(text)
    letters_dict = count_letters(text)
    letters_list = dict_to_list(letters_dict)
    sorted_list = sorted(letters_list, key=sort_on, reverse=True)
    print(f"--- Begin report of {book_path} ---")
    print(f"{number_of_words} words found in the document")
    print("\n")
    for obj in sorted_list:
        if obj["letter"].isalpha():
            print(f"The {obj["letter"]} character was found {
                  obj["count"]} times")

    print(f"--- End of report of {book_path} ---")


main()
