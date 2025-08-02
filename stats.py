def number_of_words (book_text):
    words = len(book_text.split())
    return words

def character_count (book_text):
    lower_case = book_text.lower()
    char_counts = {}
    for char in lower_case:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts
    
def sorted_list (char_dic):
    pairs = char_dic
    
    report = []
    for key, value in pairs.items():
        new_pair ={}
        #print ("Debug ", key)
        #print ("Debug ", value)
        new_pair["char"] = key
        new_pair["num"] = value
        #print("Debug ", new_pair)
        report += [new_pair]
        report.sort(key=lambda item: item['num'], reverse=True)
    return report
