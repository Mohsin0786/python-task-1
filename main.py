list_1 = [
    {"id": "1", "name": "Shrey", "age": 25},
    {"id": "3", "age": 10, "name": "Hello"},
    {"id": "2", "name": "World", "age": 24},
]

list_2 = [
    {"id": "1", "marks": 100},
    {
        "id": "3",
        "marks": 90,
        "roll_no": 11,
        "extra_info": {
            "hello": "world",
        },
    },
]


def merge_lists(list_1, list_2) -> list:
    """
    Complete this function, by merging the information from list_1 and list_2
    to create a new list, which has all the information about each student from
    both lists in one single dict.

    - Both lists are unsorted
    - Both lists can have missing values (for ex list_2 has missing id=2)
    """
    merged_list = []
    
    # Create a dictionary with id as key and values from given list_1
    tempDict_1 = {val["id"]: val for val in list_1}
    
    # Create a dictionary with id as key and values from given list_2
    tempDict_2 = {val["id"]: val for val in list_2}
    
    #make set union of keys from tempDict_1 and tempDict_2 for unique key
    unique_key  = set(tempDict_1.keys()) | set(tempDict_2.keys())
    # Iterate over the unique_key
    for _id in unique_key:
        # Initialize an empty dictionary to store the merged key-value pairs
        merged_dict = {}
        
        # Check if the current id is in tempDict_1
        if _id in tempDict_1:
            # If it is, update merged_dict with the values from tempDict_1 for that id
            merged_dict.update(tempDict_1[_id])
        
        # Check if the current id is in tempDict_2
        if _id in tempDict_2:
            # If it is, update merged_dict with the values from tempDict_2 for that id
            merged_dict.update(tempDict_2[_id])
        
        # Append the merged dictionary to the merged_list
        merged_list.append(merged_dict)
    
    # Return the merged_list containing all the merged dictionaries
    return merged_list


list_3 = merge_lists(list_1, list_2)
print(list_3)
