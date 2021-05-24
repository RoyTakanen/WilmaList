rivit = open('urls.txt', 'r')
rivit = rivit.readlines()
 
count = 0
# Strips the newline character
for line in rivit:
    count += 1
    if line.strip().startswith("Location: "):
        if not "<div " in line.strip():
            print(line.strip().replace("Location: ", ""))
