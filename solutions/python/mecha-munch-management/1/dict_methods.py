"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """

    pass
    for item in items_to_add:
        if item not in current_cart:
            current_cart[item] = 1
        else:
            current_cart[item] += 1
    return current_cart
        

def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """

    new_dict = {}
    for note in notes:
        new_dict[note] = 1
    return new_dict


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: iterable -  with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """

    pass
    
    ideas.update(recipe_updates)
    return ideas


def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """

    sorted_cart = dict(sorted(cart.items()))
    return sorted_cart


def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """

    # Create an empty dictionary to create to hold the final, structured order.
    fulfillment_cart = {}

    # Get the item names from the cart and sort them in reverse alphabetical order.
    sorted_items = sorted(cart.keys(), reverse=True)

    # Iterate through the sorted list of items.
    for item in sorted_items:
        # Check if the item from the cart exists in the aisle mapping.
        # This prevents errors if the map contains an unmapped item.
        if item in aisle_mapping:
            # Get the quantity from the user's cart.
            quantity = cart[item]

            # Get the aisle and refrigeration info from mapping.
            aisle, needs_refrigeration = aisle_mapping[item]

            # Combine the quantity, aisle and refrigertion status into a list.
            fulfillment_cart[item] = [quantity, aisle, needs_refrigeration]

    return fulfillment_cart


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """

    # Iterate over each item and its details in the fulfillment cart.
    # The .items() method provides both the key (item name) and value (details list).
    for item, order_details in fulfillment_cart.items():
        
        # Check if the item from the order exists in the store's inventory.
        # This prevents errors and handles cases where an item might be in a cart
        # but has since been removed from the store's inventory system.
        if item in store_inventory:
            
            # The quantity ordered is the first element in the order_details list.
            ordered_quantity = order_details[0]
            
            # The current inventory details for the item.
            inventory_details = store_inventory[item]
            
            # Skip if the item is already marked as 'Out of Stock'.
            # This checks if the entire value is the string, or if the first element is.
            if inventory_details == 'Out of Stock' or inventory_details[0] == 'Out of Stock':
                continue

            # The current inventory count is the first element in the inventory_details list.
            inventory_quantity = inventory_details[0]
            
            # Calculate the new inventory level.
            new_quantity = inventory_quantity - ordered_quantity
            
            # If the new quantity is zero or less, update the quantity to 'Out of Stock'.
            if new_quantity <= 0:
                store_inventory[item][0] = 'Out of Stock'
            else:
                # Otherwise, update the inventory count for that item.
                store_inventory[item][0] = new_quantity
                
    return store_inventory
