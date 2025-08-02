def transform(legacy_data):
    new_dict = {}
    for key, value in legacy_data.items():
        for item in value:
            new_dict[item.lower()] = key
    return new_dict
    