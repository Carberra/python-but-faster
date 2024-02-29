from timeit import repeat

text = "Hello world!"

t4 = min(
    repeat("text.startswith(('He', 'Ha', 'Hi', 'Ho', 'Hu'))", globals={"text": text})
)
t5 = min(
    repeat("text.startswith(('Ha', 'Hi', 'Ho', 'Hu', 'He'))", globals={"text": text})
)
t6 = min(repeat("text[:5] in {'Ha', 'He', 'Hi', 'Ho', 'Hu'}", globals={"text": text}))

print(
    f"""
MULTIPLE
Startswith (B): {t4:.3f}
Startswith (W): {t5:.3f}
Slicing       : {t6:.3f}
"""
)
