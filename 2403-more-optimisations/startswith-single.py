from timeit import repeat

text = "Hello world!"

t0 = min(repeat("text.startswith('Hello')", globals={"text": text}))
t1 = min(repeat("text.startswith('world')", globals={"text": text}))

t2 = min(repeat("text[:5] == 'Hello'", globals={"text": text}))
t3 = min(repeat("text[:5] == 'world'", globals={"text": text}))

print(
    f"""
SINGLE
Startswith (T): {t0:.3f}
Startswith (F): {t1:.3f}
Slicing    (T): {t2:.3f}
Slicing    (F): {t3:.3f}
"""
)
