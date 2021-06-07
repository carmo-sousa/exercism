def reverse(text:str):
    reversed = []

    for char in text:
        reversed.insert(0, char)
    
    return "".join(reversed)
