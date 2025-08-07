def class_limit(highest, lowest, num_of_classes): 
    return highest - lowest // num_of_classes

def percent(frquncy, total_frequncy):
    return (frquncy / total_frequncy) * 100

def relative_frequncy(num_of_frequncy, toatl_frequncy):
    return num_of_frequncy/ toatl_frequncy

def mid_point(h_limit,l_limit):
    return h_limit + l_limit / 2

# data description 

# sample mean
# where x -> the list of data
# n -> the length of the list  
def mean(x,n):
    summision_of_x = 0
    for i in x: 
        summision_of_x =+i
    return summision_of_x / n

def medine(data): 
    length = len(data)

    if length % 2 == 0: 
        mid = data[length /2]
        after_mid = data[(length/2)+1]
        result = mid + after_mid // 2 

        return result
    else:
        return data[length/2]


def mid_range(highest_v,lowest_v): 
    return highest_v + lowest_v / 2

# where x -> the list of values 
# f -> the frequncies of each x 
# n -> the summision of the f 
def mean_for_grouped_data(x,f,n):
    sum_of_xf = 0

    for i in len(x):
        sum_of_xf =+ x[i]*f[i]
    
    result = sum_of_xf / n

    return result


def medine_for_grouped_data(f, cumulative_f):
    medine_class = f[len(f) / 2]
    lower_limit = medine_class[0]
    mean_of_f = mean(f[:][2], len(f))
    class_width = medine_class[1] - medine_class[0]

    result = (lower_limit + ((mean_of_f - cumulative_f) / medine_class[2])) * class_width

    return result 

def mod(data):
    dic = {}

    for v in data:
        if v in dic:
            dic[v] =+ 1
        else:
            dic[v] = 1
    
    mod = dic[0]
    for num, f in dic:
        if f > mod:
            mod = num

    result = [mod]
    multi_mod = dic.get(mod, None)

    if multi_mod is not None:
        result.append(multi_mod)
    
    return result
  
# measure of variation

def rnge(high,low):
    return high - low

def pop_variance(x,n):
    sample_mean = mean(x[:][1], n)
    squared_x_mean = []
    summision_of_squared_x_mean = 0

    for i in range(len(x)):
        squared_x_mean.append((x[i][1] - sample_mean) ** 2)

    for squared in squared_x_mean:
        summision_of_squared_x_mean =+ squared
    
    result = summision_of_squared_x_mean / n

    return result

def standard_deviation_pop(x,n):
    variance = pop_variance(x, n)
    result = variance ** 0.5

    return result


def sample_variance(x,n):
    sample_mean = mean(x[:][1], n)
    squared_x_mean = []
    summision_of_squared_x_mean = 0

    for xi in x:
        squared_x_mean.append((xi - sample_mean) ** 2)

    for squared in squared_x_mean:
        summision_of_squared_x_mean =+ squared
    
    result = summision_of_squared_x_mean / (n-1) 

    return result


def standard_deviation_sample(x,n):
    variance = sample_variance(x, n)
    result = variance ** 0.5

    return result

def variance_grouped(x,n):
    sample_mean = mean(x[:][3],n)
    squared_x_mean = []
    summision_of_fi_by_squared_x_mean = 0

    for i in range(len(x)): 
        squared_x_mean.append((x[i][2] - sample_mean) ** 2)

    for j in range(len(squared_x_mean)):
        summision_of_fi_by_squared_x_mean =+ x[j][1] * squared_x_mean[j]
    
    result = summision_of_fi_by_squared_x_mean / n

    return result

# cofficient of variation
def coff_of_variation_sample(x,n):
    standard_deviation = standard_deviation_sample(x, n)
    sample_mean = mean(x[:][1], n)

    result = (standard_deviation / sample_mean) * 100

    return result

def coff_of_variation_pop(x,n):
    standard_deviation = standard_deviation_pop(x, n)
    sample_mean = mean(x[:][1], n)

    result = (standard_deviation / sample_mean) * 100

    return result

def coumulative_frequncy_percentile(x, desired_rank):
    total_observations = len(x) # N 
    cumulative_frequncy_for_rank = 0 
    sorted_x = sorted(x)

    for i in sorted_x:
        if i <= desired_rank:
            cumulative_frequncy_for_rank =+ 1

    if cumulative_frequncy_for_rank > 0:
        result = (cumulative_frequncy_for_rank / total_observations) * 100

        return result
    
    else:
        return None

def percentile(x, desired_rank):
    sorted_x = sorted(x)
    num_below_desired_rank = 0
    total_obs = len(x)

    for i in sorted_x:
        if i < desired_rank:
            num_below_desired_rank =+ 1
    
    if num_below_desired_rank > 0:
        result = ((num_below_desired_rank + 0.5) / total_obs) * 100

        return result
    else:
        return None

def percentile_to_value(x,percentile,):
    total_data_num = len(x)
    result = (total_data_num * percentile) / 100

    if result is isinstance(float):
        result =+ 0.5
    
        return result
    elif result is isinstance(int):
        result = (result + (result +1)) / 2

        return result
    else:
        return None


# the standard scores (z-sores)

def z_scores_pop(value, x, n):
    sample_mean = mean(x[:][1], n)
    standard_deviation = standard_deviation_pop(x,n)

    result = (value - sample_mean) / standard_deviation

    return result 

def z_scores_sample(value, x, n):
    sample_mean = mean(x[:][1], n)
    standard_deviation = standard_deviation_sample(x,n)

    result = (value - sample_mean) / standard_deviation

    return result
