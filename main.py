
def get_file(fname):
    with open(fname) as f:
        text = f.read()
    return text

def get_num_words(text):
    return len(text.split())

def get_freqs(text):
    char_freq = { }
    for c in text:
        if not c.isalpha(): 
            continue 
        elif char_freq.get(c) is None:
            char_freq[c] = 1
        else:
            char_freq[c] += 1
    return char_freq

def print_report(textfile):
    print(f'--- Begin report of {textfile} ---')
    text = get_file(textfile)
    print(f"{get_num_words(text)} words found in the document")
    print()
    freqs = get_freqs(text.lower())
    sorted_freqs = sorted(freqs.items(), key=lambda x: x[1], reverse=True)
    for c, freq in sorted_freqs:
        print(f"the '{c}' character was found {freq} times")
    print('--- End report ---')

print_report('books/frankenstein.txt')
    