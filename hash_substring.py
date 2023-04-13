# python3

def read_input():
    input_type = input()

    if input_type == "F":
        file_name = "tests/06"
        with open(file_name) as f:
            text1 = f.readlines()
            pattern = text1[0].strip()
            text = text1[1].strip()
    elif input_type == "I":
        pattern = input().strip()
        text = input().strip()
    else:
        print("Invalid input type.")
        return
    return pattern, text

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    d = 256
    q = 1000000007
    p_len = len(pattern)
    t_len = len(text)

    p_hash = sum([ord(pattern[i]) * pow(d, p_len-i-1, q) for i in range(p_len)]) % q
    t_hash = sum([ord(text[i]) * pow(d, p_len-i-1, q) for i in range(p_len)]) % q

    result = []
    for i in range(t_len - p_len + 1):
        if p_hash == t_hash and pattern == text[i:i+p_len]:
            result.append(i)
        if i < t_len - p_len:
            t_hash = ((t_hash - ord(text[i]) * pow(d, p_len-1, q)) * d + ord(text[i+p_len])) % q

    return result

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

