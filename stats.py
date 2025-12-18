from collections import defaultdict
def get_num_words(words):
    word_split = words.split()
    word_count = 0
    for word in word_split:
        word_count += 1 
    print("----------- Word Count ----------")
    print(f'Found {word_count} total words')

def letter_count(words):
    dic = defaultdict(int)

    for word in words:
        for letter in word:
            llower = letter.lower()
            dic[llower] += 1 
    
    return dic

def analyze(words):
    dic = letter_count(words)
    pairs = []
    for k,v in dic.items():
        if k.isalpha():
            pairs.append((k,v))

    pairs.sort(key=lambda x: x[1], reverse = True)
    print("--------- Character Count -------")
    for key,value in pairs:
        print(f"{key}: {value}")
    