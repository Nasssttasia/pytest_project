def get_val(collection, key, default='git'):
    for i in collection.keys():
        if key == i:
            return key['key']
        return default