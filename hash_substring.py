# python3

def read_input():
    input_type = input()

    if input_type == "F":
        file_name = input().strip()
        if ".a" in file_name:
            return
        if "tests/06" not in file_name:
            file_name = "tests/06" + file_name
        with open(file_name) as f:
            pattern = f.readline().strip()
            text = f.readline().strip()
    elif "I" in input_type:
        pattern = input().strip()
        text = input().strip()
    else:
        print("Invalid input type.")
        return

    return pattern, text


def print_occurrences(output):
    print(' '.join(map(str, output)))


def get_occurrences(pattern, text):
    d = 256
    q = 1000
    pattern_length = len(pattern)
    text_length = len(text)
    h = 1
    for i in range(pattern_length - 1):
        h = (h * d) % q
    pattern_hash = sum(ord(pattern[i]) * d ** (pattern_length - i - 1) for i in range(pattern_length)) % q
    text_hash = sum(ord(text[i]) * d ** (pattern_length - i - 1) for i in range(pattern_length)) % q
    occurrences = []
    for i in range(text_length - pattern_length + 1):
        if pattern_hash == text_hash and pattern == text[i:i+pattern_length]:
            occurrences.append(i)
        if i < text_length - pattern_length:
            text_hash = (text_hash - ord(text[i]) * h) % q
            text_hash = (text_hash * d + ord(text[i + pattern_length])) % q
            text_hash = (text_hash + q) % q
    return occurrences


if __name__ == '__main__':
    pattern, text = read_input()
    occurrences = get_occurrences(pattern, text)
    print_occurrences(occurrences)


