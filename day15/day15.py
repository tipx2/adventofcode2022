from parse import parse
with open("input15.txt") as f:
    lines = f.readlines()

ranges = []
limit = 4000000

def fewest_ranges(ranges):
    # Sort the ranges by their start value in ascending order
    sorted_ranges = sorted(ranges, key=lambda r: r[0])

    # Initialize the result with the first range in the sorted list
    result = [sorted_ranges[0]]

    # Iterate over the rest of the sorted ranges
    for start, end in sorted_ranges[1:]:
        # If the current range overlaps with the last range in the result,
        # merge them by updating the last range in the result to cover both
        if start <= result[-1][1]:
            result[-1][1] = max(result[-1][1], end)
        # If the current range does not overlap with the last range in the result,
        # add it to the result as a new range
        else:
            result.append([start, end])

    # Find the overall minimum and maximum values in the input ranges
    min_val = min(r[0] for r in ranges)
    max_val = max(r[1] for r in ranges)

    # Check if the first range in the result starts after the minimum value
    # or if the last range in the result ends before the maximum value
    if result[0][0] > min_val or result[-1][1] < max_val:
        # If so, insert a new range at the beginning or end of the result
        # to cover the full range of values in the input ranges
        if result[0][0] > min_val:
            result.insert(0, [min_val, result[0][0]])
        if result[-1][1] < max_val:
            result.append([result[-1][1], max_val])

    # Check if any ranges in the result are completely contained within another range
    for i in range(len(result)):
        for j in range(len(result)):
            # If range i is contained within range j and i is not equal to j,
            # remove range i from the result
            if i != j and result[i][0] >= result[j][0] and result[i][1] <= result[j][1]:
                result.remove(result[i])

    # Check if any ranges in the result can be merged without increasing the number of ranges
    for i in range(len(result)):
        for j in range(len(result)):
            # If range i and range j are adjacent and i is not equal to j,
            # merge them by updating range i to cover both and remove range j from the result
            if i != j and result[i][1] == result[j][0]:
                result[i][1] = result[j][1]
                result.remove(result[j])

    return result

def get_line_coverage(yline):
    ranges = []
    for line in lines:
        sensorx, sensory, beaconx, beacony = parse("Sensor at x={}, y={}: closest beacon is at x={}, y={}", line)
        sensorx, sensory, beaconx, beacony = int(sensorx), int(sensory), int(beaconx), int(beacony)
    
        manhatt_dist = abs(sensorx-beaconx) + abs(sensory-beacony)
        dist_to_line = abs(yline - sensory)
    
        linerange = manhatt_dist-dist_to_line
        if linerange < 0:
            continue
        low = min(sensorx-linerange, sensorx+linerange)
        high = max(sensorx-linerange, sensorx+linerange)
        range_on_line = [low, high]
        
        ranges.append(range_on_line)
    return ranges
for x in range(limit+1):
    if x % 10000 == 0:
        print("aryehvalue", x)
    coverage = fewest_ranges(get_line_coverage(x))

    for t_range in coverage:
        if t_range[1] < 0:
            t_range[1] = 0
        if t_range[0] > limit:
            t_range[0] = limit
        if t_range[0] < 0:
            t_range[0] = 0
        if t_range[1] > limit:
            t_range[1] = limit
    
    for t in range(len(coverage)-1, 0, -1):
        if coverage[t] == [0,0]:
            del coverage[t]
        elif coverage[t] == [limit, limit]:
            del coverage[t]
    
    if sum([abs(x[0] - x[1])+1 for x in coverage]) == limit:
        for w in range(0, limit+1):
            for r in coverage:
                if w in range(r[0], r[1]+1):
                    break
            else:
                print(w*4000000 + x)
                break