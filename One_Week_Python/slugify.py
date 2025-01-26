def slugify(phrase):
    return phrase.lower().strip().replace(" ","-")

print(slugify("Hello world I am turok"))