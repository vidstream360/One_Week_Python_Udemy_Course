def laugh(strength=2):
    print("HA" * strength)

laugh(10)
laugh() #defaults to printing * 2 

def slugify(phrase, sep="-"):
    return phrase.lower().strip().replace(" ",sep)

print(slugify("Hello world I am turok","_")) #pass new seperator character