import re

text="remplazar toda la vocales por arterisco"

new_tex= re.sub("[aeiou]", "*", text)

print(new_tex)