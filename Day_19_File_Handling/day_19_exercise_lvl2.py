#Extract all incoming email addresses as a list from the email_exchange_big.txt file.
import re

with open('./DATA/email_exchanges_big.txt','r',encoding='utf-8') as f1:
    data=f1.read()
    emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', data)
    for item in emails:
        print(item)

#Find the most common words in the English language. Call the name of your function find_most_common_words, it will take two parameters - a string or a file and a positive integer, indicating the number of words. Your function will return an array of tuples in descending order. Check the output
def find_most_common_words(file_name,num):
    with open(file_name,'r',encoding='utf-8') as f2:
        data=f2.read().lower()
        words = re.findall(r'\b[a-zA-Z0-9]+\b', data)
        
    word_count = {}

    for w in words:
            word_count[w] = word_count.get(w, 0) + 1
        
    sorted_word=sorted(word_count.items(),key=lambda x:x[1],reverse=True)
    
    return sorted_word[:num]
    
#Use the function, find_most_frequent_words to find: 
# a) The ten most frequent words used in Obama's speech 
result=find_most_common_words('./DATA/obama_speech.txt',10)
print("the ten most frequent word  in obama_speech.txt are")
for word, count in result:
    print(f"{word} → {count}")

# b) The ten most frequent words used in Michelle's speech 
result=find_most_common_words('./DATA/michelle_obama_speech.txt',10)
print("the ten most frequent word  in michelle_obama_speech.txt are")
for word, count in result:
    print(f"{word} → {count}")

# c) The ten most frequent words used in Trump's speech 
result=find_most_common_words('./DATA/donald_speech.txt',10)
print("the ten most frequent word  in donald_speech.txt are")
for word, count in result:
    print(f"{word} → {count}")

# d) The ten most frequent words used in Melina's speech
result=find_most_common_words('./DATA/melina_trump_speech.txt',10)
print("the ten most frequent word  in melina_trump_speech.txt are")
for word, count in result:
    print(f"{word} → {count}")

#Write a python application that checks similarity between two texts.
# It takes a file or a string as a parameter and it will evaluate the similarity of the two texts. 
# For instance check the similarity between the transcripts of Michelle's and Melina's speech. 
# You may need a couple of functions, function to clean the text(clean_text), function to remove support words(remove_support_words) and finally to check the similarity(check_text_similarity). 
# List of stop words are in the data directory

from difflib import SequenceMatcher

# -------------------------
# 1. CLEAN TEXT
# -------------------------
def clean_text(text):
    # Convert to lower case
    text = text.lower()

    # Keep only letters and numbers
    text = re.sub(r'[^a-z0-9\s]', ' ', text)

    # Collapse extra spaces
    text = re.sub(r'\s+', ' ', text).strip()

    return text


# -------------------------
# 2. REMOVE STOP WORDS
# -------------------------
def remove_support_words(text, stop_word_file='./DATA/stop_words.py'):
    # Load stop words (python file containing a list)
    with open(stop_word_file, 'r', encoding='utf-8') as f:
        stopwords = eval(f.read().split("=")[1])

    words = text.split()
    words = [w for w in words if w not in stopwords]

    return " ".join(words)


# -------------------------
# 3. MAIN SIMILARITY FUNCTION
# -------------------------
def check_text_similarity(text1, text2):
    # 1. Clean both texts
    t1 = clean_text(text1)
    t2 = clean_text(text2)

    # 2. Remove stopwords
    t1 = remove_support_words(t1)
    t2 = remove_support_words(t2)

    # 3. Jaccard similarity
    set1 = set(t1.split())
    set2 = set(t2.split())
    jaccard = len(set1 & set2) / len(set1 | set2)

    # 4. Sequence similarity
    seq_sim = SequenceMatcher(None, t1, t2).ratio()

    return {
        "jaccard_similarity": round(jaccard, 4),
        "sequence_similarity": round(seq_sim, 4)
    }


# ---------------------------------------------------------
# Helper function: read file OR accept string automatically
# ---------------------------------------------------------
def read_input(data):
    # If input looks like a file
    try:
        with open(data, 'r', encoding='utf-8') as f:
            return f.read()
    except:
        return data  # It is not a file path, treat as raw string


# ---------------------------------------------------------
# EXAMPLE USAGE
# ---------------------------------------------------------

# Compare Michelle Obama vs Melania Trump speeches
text_a = read_input('./DATA/michelle_obama_speech.txt')
text_b = read_input('./DATA/melina_trump_speech.txt')

result = check_text_similarity(text_a, text_b)

print("Similarity Results:")
print(result)

#Find the 10 most repeated words in the romeo_and_juliet.txt
result=find_most_common_words('./DATA/romeo_and_juliet.txt',10)
print("the ten most frequent word  in romeo_and_juliet.txt are")
for word, count in result:
    print(f"{word} → {count}")

#Read the hacker news csv file and find out: a) Count the number of lines containing python or Python 
# b) Count the number lines containing JavaScript, javascript or Javascript 
# c) Count the number lines containing Java and not JavaScript
import csv
with open('./DATA/hacker_news.csv','r',encoding='utf-8') as f3:
    csv_reader=csv.reader(f3,delimiter=',')
    python_count=0
    javascript_count=0
    java_count=0
    for row in csv_reader:
        if any('python' in cell.lower() for cell in row):
            python_count += 1
        if any('javascript' in cell.lower() for cell in row):
            javascript_count += 1
        if any('java' in cell.lower() for cell in row ) and not any('javascript' in cell.lower() for cell in row) :
            java_count+=1
print(f'Number of lines containing python is :  {python_count}')
print(f'Number of lines containing javascript is :  {javascript_count}')
print(f'Number of lines containing java is :  {java_count}')
