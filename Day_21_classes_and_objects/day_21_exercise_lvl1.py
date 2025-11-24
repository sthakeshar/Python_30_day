#Python has the module called statistics and we can use this module to do all the statistical calculations. 
# However, to learn how to make function and reuse function let us try to develop a program, which calculates the measure of central tendency of a sample (mean, median, mode) and measure of variability (range, variance, standard deviation). 
# In addition to those measures, find the min, max, count, percentile, and frequency distribution of the sample. You can create a class called Statistics and create all the functions that do statistical calculations as methods for the Statistics class. 
# Check the output below.
class statistics:
    def __init__(self,data):
        self.data=sorted(data)
    
    def count(self):
        return len(self.data)
    
    def sum(self):
        total=0
        for n in self.data:
            total+=n
        return total
    
    def min(self):
        return self.data[0]
    
    def max(self):
        return self.data[-1]
    
    def range(self):
        return self.max()-self.min()

    def mean(self):
        return self.sum() / self.count()
    
    def median(self):
        n=self.count()
        mid = n // 2

        if n % 2 == 0:
            return (self.data[mid - 1] + self.data[mid]) / 2
        else:
            return self.data[mid]

    def mode(self):
        freq={}
        for item in self.data:
             freq[item] = freq.get(item, 0) + 1
        
        max_count = max(freq.values())
        # If multiple, return just the first (as per example)
        for number, count in freq.items():
            if count == max_count:
                return {"mode": number, "count": count}
    
    def var(self):
        mean = self.mean()
        total = 0
        for n in self.data:
            total += (n - mean) ** 2
        return total / self.count()

    def std(self):
        return self.var() ** 0.5

    # ---- Frequency Distribution ----
    def freq_dist(self):
        freq = {}
        for n in self.data:
            freq[n] = freq.get(n, 0) + 1

        # Convert to list of (percentage, value)
        result = []
        total = self.count()

        for num, count in freq.items():
            percent = (count / total) * 100
            result.append((percent, num))

        # sort descending by percent
        return sorted(result, reverse=True)

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data=statistics(ages)
print('Count:', data.count()) # 25
print('Sum: ', data.sum()) # 744
print('Min: ', data.min()) # 24
print('Max: ', data.max()) # 38
print('Range: ', data.range()) # 14
print('Mean: ', data.mean()) # 30
print('Median: ', data.median()) # 29
print('Mode: ', data.mode()) # {'mode': 26, 'count': 5}
print('Standard Deviation: ', data.std()) # 4.2
print('Variance: ', data.var()) # 17.5
print('Frequency Distribution: ', data.freq_dist()) # [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]
