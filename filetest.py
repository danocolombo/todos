file = open('essay.txt', 'r')
contents = file.read()
file.close()

content = contents.title()
print(f"{content}")