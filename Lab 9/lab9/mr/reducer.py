import sys

less_than_equal_50 = 0
more_than_50 = 0

for line in sys.stdin:
    line = line.strip().split(',')
    idx, cluster = line[0], int(line[1])
    
    if cluster == 0:
        less_than_equal_50 += 1
    else:
        more_than_50 += 1

print('Number of points in cluster 1 (less_than 50) '+str(less_than_equal_50))
print('Number of points in cluster 2 (more than 50) '+str(more_than_50))
