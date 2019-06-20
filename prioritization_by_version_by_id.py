import heapq

def merge_boxs(prime_box_heap, version_map, regular_box):
    output = [] # final output result will be stored here
    while prime_box_heap:
        version = heapq.heappop(prime_box_heap)
        box_ids = version_map[version]
        box_id = box_ids.pop()
        output.append(box_id + ' ' + version)
    while regular_box:
        output.append(regular_box.pop())
    return output    

def orderedJunctionBoxes(numberOfBoxes, boxList):
    prime_box_heap = [] # holds version of prime boxs in priority queue/heap
    version_map = {} # holds mapping of each prime box version with its corresponding box id
    regular_box = [] # holds regular boxs (in reversed box of their occerance for tail poping)
    for box in reversed(boxList):
        entry = box.split()
        if entry[1].isdigit():    # put regular boxs in regular_box list
            regular_box.append(box)
        else:   # split the version and box_id of prime boxs 
            box_id = entry[0]
            version = " ".join(entry[1:])  # put the version as a string in Python min heap
            heapq.heappush(prime_box_heap, version)
            box_ids = version_map.get(version, []) 
            box_ids.append(box_id)  # for each version store its id or possibly sorted list of ids 
            version_map[version] = sorted(box_ids, reverse=True)
    
    result = merge_boxs(prime_box_heap, version_map, regular_box)  # get merged list of the two box types
    return result
