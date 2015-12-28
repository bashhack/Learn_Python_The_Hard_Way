'''
Create a shell spinner - now to write a CLI to go with it :)
'''
while True:
    for i in ["/", "-", "|", "\\", "|"]:
        print "%s\r" % i,    # prevent new line
