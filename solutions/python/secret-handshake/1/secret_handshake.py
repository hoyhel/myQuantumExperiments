def commands(binary_str):
    # Create actions dictionary
    actions = {0: "wink", 1: "double blink", 2: "close your eyes", 3: "jump", 4: "reverse the order of the operations in the secret handshake"}

    secret_handshake = []
    # Loop through binary_str
    # List should be reversed
    for index, item in enumerate(binary_str[::-1]):
        # If == "1":
        if item == "1":
            if index == 4:
                secret_handshake = list(reversed(secret_handshake))
            else:
                secret_handshake.append(actions[index])
    return secret_handshake
