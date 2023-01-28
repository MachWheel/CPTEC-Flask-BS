import re


def alfa_string(item: str) -> str:
    item = item.replace('-', ' ')
    expression = fr'[^a-zA-Z\s]+'
    item = re.sub(expression, '', item)
    return re.sub(r" +", " ", item).lower()


def accentuated_chars(item: str) -> str:
    item = item.lower()
    accent_map = {
        'á': 'a', 'à': 'a', 'ã': 'a', 'â': 'a',
        'é': 'e', 'ê': 'e',
        'í': 'i', 'î': 'i',
        'ó': 'o', 'õ': 'o', 'ô': 'o',
        'ú': 'u', 'ü': 'u',
        'ç': 'c',
    }
    return re.sub(
        r"[{}]".format("".join(accent_map.keys())),
        lambda m: accent_map[m.group(0)],
        item
    )
