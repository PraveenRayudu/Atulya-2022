def double_string(string):
    output=''
    for i in string:
        i = i+i
        output=output+i
    print(output)

double_string("welcome home")
