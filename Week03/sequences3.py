
def remove_duplicates(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

def list_counts(input_list):
    count_dict = {}
    for item in input_list:
        count_dict[item] = count_dict.get(item, 0) + 1
    return count_dict

def reverse_dict(input_dict):
    reversed_dict = {}
    for key, value in input_dict.items():
        reversed_dict[value] = key
    return reversed_dict
