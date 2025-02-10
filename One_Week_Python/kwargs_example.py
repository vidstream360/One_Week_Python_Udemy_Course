# kew word arguments, make dictionaries
#inputs have to be key value pairs

def print_ages(**kwargs):
    for k,v in kwargs.items():
        print(f"{k} os {v} years old")
    
print_ages(max=67,sue=59,kim=14)
