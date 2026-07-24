#statistics_in_python.py
data = [12, 15, 20, 20, 25, 28]

def find_mean(array):
    sum = 0 
    for i in array:
        sum += i
    mean = sum/len(array)
    return mean

def find_median(array):
    array = sorted(array)
    median_index = len(array) // 2
    if len(array) % 2 == 0:
        median = (array[median_index] + array[median_index - 1]) / 2
    else:
        median = array[median_index]
    return median

def find_mode(array):
    counts = {}
    
    for i in array:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
            
    modes = []
    maximum = 0
    
    for i, count in counts.items():
        if count > maximum:
            maximum = count
            modes = [i]
        elif count == maximum:
            modes.append(i)
    
    if maximum == 1:
        return "No Mode"
    
    if len(array) == 0:
        return None 
        
    return modes[0] if len(modes) == 1 else modes

def find_range(array):
    lowest = array[0]
    highest = array[0]
    
    for i in array: 
        if i > highest:
            highest = i
    
    for i in array:
        if i < lowest:
            lowest = i
    
    return highest - lowest

def find_variance(array):
    array_sum = 0
    
    for i in array:
        array_sum += i
    
    mean = array_sum / len(array)
    
    vari = []
    for i in array:
        var = (i - mean)**2
        vari.append(var)
        
    vari_sum = 0 
    
    for var in vari:
        vari_sum += var
    
    return vari_sum
    
def find_sample_variance(array):
    vari_sum = find_variance(array)
    return vari_sum / (len(array) - 1)

def find_population_variance(array):
    vari_sum = find_variance(array)
    return vari_sum / (len(array) - 1)

def find_sample_stdev(array):
    sample_variance = find_sample_variance(array)
    return sample_variance ** 0.5
    
def find_population_stdev(array):
    population_variance = find_population_variance(array)
    return population_variance ** 0.5


print(find_mean(data))
print(find_median(data))
print(find_mode(data))
print(find_range(data))
print(find_sample_variance(data))
print(find_population_variance(data))
print(find_sample_stdev(data))
print(find_population_stdev(data))
