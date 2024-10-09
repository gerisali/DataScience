
def remove_duplicates(input_list):
    return list(set(input_list))

def list_counts(input_list):
    count_dict = {}
    for item in input_list:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict

def reverse_dict(input_dict):
    reversed_dict = {}
    for key, value in input_dict.items():
        reversed_dict[value] = key
    return reversed_dict
