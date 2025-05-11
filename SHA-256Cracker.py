import hashlib
import random
import itertools

chars = "deGioOstu"
hash_ = "b8c49d81cb795985c007d78379e98613a4dfc824381be472238dbd2f974e37ae"


def sha256_cracker(hash_: str, chars: str) -> str:
    while True:
        candidate = generator(chars)
        candidate_hash = hashlib.sha256(candidate.encode()).hexdigest()
        if candidate_hash == hash_:
            return candidate
    return None


def generator(chars):
    newstr = ""
    while len(newstr) != len(chars):
        random_letter = random.randint(0, len(chars) - 1)
        if chars[random_letter] in newstr:
            continue
        newstr += chars[random_letter]
    return newstr


print(sha256_cracker(hash_, chars))


# Chatgpt
def sha256_cracker(hash_: str, chars: str) -> str:
    # Генерируем все возможные перестановки из символов
    for candidate_tuple in itertools.permutations(chars, len(chars)):
        candidate = "".join(candidate_tuple)
        candidate_hash = hashlib.sha256(candidate.encode()).hexdigest()
        if candidate_hash == hash_:
            return candidate
    return None
