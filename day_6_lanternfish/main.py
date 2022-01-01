data = [int(x) for x in open("input.txt").read().split(',')]
from collections import Counter

max_days = 256
counts = Counter(data)

for i in range(max_days):  
    new_counts = {x:0 for x in range(9)}
    
    for k,i in counts.items():
        new_counts[k-1] = i
        
    if -1 in new_counts:
        new_counts[6] += new_counts[-1]
        new_counts[8] = new_counts[-1]
        del(new_counts[-1])
    
    counts = new_counts    

print(f"sum: {sum(counts.values())}")    
