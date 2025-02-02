with open("books/frankenstein.txt") as f:
    file_contents = f.read()


def wordcount():
    print(len(file_contents.split()))

def charactercount(test = 'no'):
    #take the input string
    #place into a list
    #iterate through the list
        #check if character in the list is in the counted list, that dictionary index
        #if it is increment that dictionary index, if not append it at 
    divided_string = list(file_contents.lower())
    dict_chars = {}
    
    
    for i in range(len(divided_string)):
        if divided_string[i] in dict_chars:
            dict_chars[divided_string[i]] += 1
        else:
            dict_chars[divided_string[i]]= 1
    
    if test != 'no':        
        for x in dict_chars:
            print(f"'{x}': {dict_chars[x]}")

    return dict_chars
    
def report():
    print(f"{wordcount()} words found in the document")
    print("")
    print("")
    chars_to_check = "abcdefghijklmnopqrstuvwxyz"
    char_list_check = list(chars_to_check)
    
    sorted_list = charactercount()
    val_based_rev = {k: v for k, v in sorted(sorted_list.items(), key=lambda item: item[1], reverse=True)}
    
    for i in val_based_rev:
        if i in chars_to_check:
            print(f"The '{i}' character was found {val_based_rev[i]} times")    
    
    print("--- End report ---")

def main():
    go = True
    
    while(go):
        cmd = input("Enter command: ")
        match cmd:
            case "read":
                print(file_contents)
            case "wordcount":
                wordcount()
            case "characters":
                charactercount("print")
            case "report":
                report()
            case "exit" | "q":
                go=False;

main()