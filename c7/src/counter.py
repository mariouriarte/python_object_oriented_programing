from collections import Counter


def letter_frequency_3(sentence: str) -> Counter[str]:
    return Counter(sentence)


print(letter_frequency_3("mario arturo marin"))
favorites = Counter("mario arturo marin").most_common()
name, frequency = favorites[0]
print(name, frequency)
