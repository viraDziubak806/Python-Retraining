def add_to_list(my_list, additional_item):
    """
        Adds an item or multiple items to list.

        This function takes a list and an additional item as input. If the additional item
        is a collection, it will be extended with each item from additional_item collection.
        If the additional item is of any other type, it will be appended as a single element.

        Args:
            my_list (list): The list to which items will be added. This list will be modified in place.
            additional_item (any): The item or items to add to the list.
                                   This can be a single item or a collection (list, tuple, set).

        Returns:
            None: The function modifies `my_list` and does not return a new list.
        """
    item_type = type(additional_item)
    if item_type == list or item_type == tuple or item_type == set:
        my_list.extend(additional_item)
    else:
        my_list.append(additional_item)

    print(my_list)


common_list = [1,3,6,68, 'a']
dictionary_values = {'k':'45', 'j':8}
additional_list = [ 'cat', 'dog', 'cat']
tuple_values = (1, 'one')
set_values = set(additional_list)


add_to_list(common_list, None)
add_to_list(common_list, True)
add_to_list(common_list, 77)
add_to_list(common_list, 1.76)
add_to_list(common_list, 'cat')
add_to_list(common_list, dictionary_values)
add_to_list(common_list, additional_list)
add_to_list(common_list, tuple_values)
add_to_list(common_list, set_values)