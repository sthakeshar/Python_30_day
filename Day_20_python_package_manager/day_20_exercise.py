import requests

#Read this url and find the 10 most frequent words. romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'
cat_api='https://api.thecatapi.com/v1/breeds'

response = requests.get(cat_api) # opening a network and fetching a data
print(response.status_code) # status code, success:200
cats_data=response.json()
print(cats_data[-1])
weights=[]
for cat in cats_data:
    weight_range=cat['weight']['metric']
    try:
        min_w,max_w=weight_range.split('-')
        avg_weight = (float(min_w) + float(max_w)) / 2  # average weight
        weights.append(avg_weight)
    except: 
        continue

def mean(lst):
    return sum(lst) / len(lst)

def median(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid = n // 2

    if n % 2 == 0:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    else:
        return sorted_lst[mid]
    
def std_dev(lst):
    mu = mean(lst)
    variance = sum((x - mu) ** 2 for x in lst) / len(lst)
    return variance ** 0.5
#the min, max, mean, median, standard deviation of cats' weight in metric units.
min_weight = min(weights)
max_weight = max(weights)
mean_weight = mean(weights)
median_weight = median(weights)
std_weight = std_dev(weights)

# ---- OUTPUT ---- #
print(f"Min weight: {min_weight} kg")
print(f"Max weight: {max_weight} kg")
print(f"Mean weight: {mean_weight:.2f} kg")
print(f"Median weight: {median_weight} kg")
print(f"Standard deviation: {std_weight:.2f} kg")

#the min, max, mean, median, standard deviation of cats' lifespan in years.
lifespan=[]
for cats in cats_data:
    lifespan_range=cats['life_span']
    try:
        min_lifespan,max_lifespan=lifespan_range.split('-')
        avg_span = (float(min_lifespan) + float(max_lifespan)) / 2  # average weight
        lifespan.append(avg_span)
    except:
        continue

min_life = min(lifespan)
max_life = max(lifespan)
mean_life = mean(lifespan)
median_life = median(lifespan)
std_life = std_dev(lifespan)

# ---- OUTPUT ---- #
print(f"Min life: {min_life} year")
print(f"Max life: {max_life} year")
print(f"Mean life: {mean_life:.2f} year")
print(f"Median life: {median_life} year")
print(f"Standard deviation: {std_life:.2f} year")

#Create a frequency table of country and breed of cats
country_to_breeds = {}

for breed in cats_data:
    origin = breed.get("origin", "").strip()
    name = breed.get("name", "").strip()

    if origin:                      # ignore blanks
        if origin not in country_to_breeds:
            country_to_breeds[origin] = []
        country_to_breeds[origin].append(name)

# 3. Create count table
country_counts = {country: len(breeds) for country, breeds in country_to_breeds.items()}

# 4. Sort by frequency (descending)
sorted_country_counts = sorted(country_counts.items(), key=lambda x: x[1], reverse=True)

# ---- OUTPUT ----
print("COUNTRY  →  NUMBER OF BREEDS")
for country, count in sorted_country_counts:
    print(f"{country}: {count}")

print("\nDETAILED BREED LIST BY COUNTRY")
for country, breeds in country_to_breeds.items():
    print(f"{country} ({len(breeds)}): {', '.join(breeds)}")

#Read the countries API and find
response1=requests.get('https://restcountries.eu/rest/v2/all')
print(response1.status_code)