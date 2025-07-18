def find_min(lst):
    if not lst:
        return None
    
    min_value = lst[0]
    for num in lst[1:]:
        if num < min_value:
            min_value = num
    return min_value