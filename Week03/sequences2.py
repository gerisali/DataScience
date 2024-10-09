
def remove_duplicates(input_list):
    return list(dict.fromkeys(input_list))

def list_counts(input_list):
    from collections import Counter
    return dict(Counter(input_list))

def reverse_dict(input_dict):
    return {value: key for key, value in input_dict.items()}
