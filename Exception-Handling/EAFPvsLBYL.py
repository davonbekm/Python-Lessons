
"""
  Mavzu: EAFP vs LBYL (pythonik uslub).
  Xatolik turlari: KeyError (cache[key]).
  Qayerda ishlatish: Lug'at/cache o'qish, race/TOCTOU bo'lishi mumkin bo'lgan joylarda EAFP yaxshi.

  Topic: EAFP vs LBYL (pythonic style).
  Error types: KeyError (cache[key]).
  When to use: Dict/cache access; EAFP is safer under race/TOCTOU scenarios.
"""

cache = {}

def compute_and_store(key):
    # UZ: Haqiqiy loyihada bu og'ir hisob-kitob, DB yoki API chaqiruv bo'lishi mumkin
    # EN: In real projects this may be heavy compute, DB or API call
    value = len(str(key))
    cache[key] = value
    return value

# EAFP
def get_value_eafp(key):
    try:
        return cache[key]
    except KeyError:
        return compute_and_store(key)

# LBYL
def get_value_lbyl(key):
    if key in cache:
        return cache[key]
    else:
        return compute_and_store(key)

if __name__ == "__main__":
    print("EAFP:", get_value_eafp("hello"))  # compute
    print("EAFP:", get_value_eafp("hello"))  # cache
    print("LBYL:", get_value_lbyl("world"))  # compute
    print("LBYL:", get_value_lbyl("world"))  # cache
