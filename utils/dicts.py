def get_val(collection, key, default='git'):
    # Проверям наличие ключа в словаре
    if key in collection:
        return collection[key]
    # Если ключа нет, возвращаем default
    return default