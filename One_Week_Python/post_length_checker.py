print("The social media's char limit is 140! Use this to check your post's char lengths!")
print("*"*25)

max_char = 140
post = input("enter your post:   ")

post_len = len(post)
difference = post_len - 140

print("*"*25)
if post_len > max_char:
    print(f"This post is {post_len} characters. {difference} char too long :(")
else:
    print(f"The {post_len} char post will work!")