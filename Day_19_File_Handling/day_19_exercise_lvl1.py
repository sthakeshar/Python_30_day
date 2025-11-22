#Write a function which count number of lines and number of words in a text. All the files are in the data the folder: 
# a) Read obama_speech.txt file and count number of lines and words 
# b) Read michelle_obama_speech.txt file and count number of lines and words 
# c) Read donald_speech.txt file and count number of lines and words 
# d) Read melina_trump_speech.txt file and count number of lines and words
import json
with open('./DATA/obama_speech.txt', encoding='utf-8') as f1:
    txt1 = f1.read()
    word_count = len(txt1)
    sentences = txt1.split('.')
    sentence_count = len(sentences)

print("The word count in obama_speech.txt is", word_count)
print("The sentence count in obama_speech.txt is", sentence_count)

with open('./DATA/michelle_obama_speech.txt', encoding='utf-8') as f2:
    txt2 = f2.read()
    word_count = len(txt2)
    sentences = txt2.split('.')
    sentence_count = len(sentences)

print("The word count in michelle_obama_speech.txt is", word_count)
print("The sentence count in michelle_obama_speech.txt is", sentence_count)

with open('./DATA/donald_speech.txt', encoding='utf-8') as f3:
    txt3 = f3.read()
    word_count = len(txt3)
    sentences = txt2.split('.')
    sentence_count = len(sentences)

print("The word count in donald_speech.txt file.txt is", word_count)
print("The sentence count in donald_speech.txt file.txt is", sentence_count)

with open('./DATA/melina_trump_speech.txt', encoding='utf-8') as f4:
    txt4 = f4.read()
    word_count = len(txt4)
    sentences = txt2.split('.')
    sentence_count = len(sentences)

print("The word count in melina_trump_speech.txt is", word_count)
print("The sentence count in melina_trump_speech.txt is", sentence_count)

#Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages
def most_spoken_language(file_name,num):
    with open(file_name, 'r', encoding='utf-8') as f:
        data = json.load(f)
        language_count = {}
        for country in data:
            for language in country['languages']:
                if language in language_count:
                    language_count[language] += 1
                else:
                    language_count[language] = 1
        sorted_languages = sorted(language_count.items(), key=lambda x: x[1], reverse=True)

        result=[
                {
                    language,count
                }
                for language,count in sorted_languages[::num]
        ]
    return result
    
print(most_spoken_language('./DATA/countries_data.json',10))

#Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries
def most_populated_countries(file_name,num):
    with open(file_name,'r',encoding='utf-8') as f:
        data=json.load(f)
        sorted_countries = sorted(
        data,
        key=lambda country: country['population'],
        reverse=True
    )

    # Prepare output format
    result = [
        {
            'country': country['name'],
            'population': country['population']
        }
        for country in sorted_countries[:num]
    ]

    return result

print(most_populated_countries('./DATA/countries_data.json',3))
