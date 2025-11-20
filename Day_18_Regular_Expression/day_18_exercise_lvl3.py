#Clean the following text. After cleaning, count three most frequent words in the string.
import re
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

pattren=r'!@#$%^&*'

def clean_text(sentence):
    cleaned = re.sub(r'[^A-Za-z ]', '', sentence)
    words = cleaned.split()
    freq = {}
    for w in words:
        if w in freq:
            freq[w] += 1
        else:
            freq[w] = 1

    sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    top_three = sorted_words[:3]

    print("Cleaned sentence:\n", cleaned)
    print("\nTop three most frequent words:")
    for word, count in top_three:
        print(word, "→", count)

clean_text(sentence)

