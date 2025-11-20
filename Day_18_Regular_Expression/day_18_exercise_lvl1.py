#What is the most frequent word in the following paragraph?
import re

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

words = re.findall(r'\w+', paragraph.lower())

freq = {}
for w in words:
    if w in freq:
        freq[w] += 1
    else:
        freq[w] = 1
print(freq)
# Find the most frequent word
most_frequent = max(freq, key=freq.get)

print("Most frequent word:", most_frequent)
print("Frequency:", freq[most_frequent])

#The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.
points = ['-12', '-4', '-3', '-1', '0', '4', '8']

num=[int(x) for x in points]
print(num)

min_point=min(num)
max_point=max(num)

distance=max_point-min_point
print("The distance between the two furthest particles is:", distance)