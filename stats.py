def total_words(text):
    y = 0
    x = text.split()
    for i in x:
        y += 1
    #print(f"Found {y} total words") 	
    return y

def each_char(text):
    char_count = {}
    x = text.lower()

    for char in x:
        if char == " ":
           continue

        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    #print(char_count)
    return char_count

def sorted_list(print_char):
    filtered = {k: v for k, v in print_char.items() if k.islower()}
    sorted_filtered = dict(sorted(filtered.items()))
    for key, value in sorted_filtered.items():
        print(f"{key}: {value}")
    return None
