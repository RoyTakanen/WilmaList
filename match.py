#Käsittele osittain parsatut
rivit = open('urls.txt', 'r')
rivit = rivit.readlines()

valmiitirvit = []

count = 0
for line in rivit:
    count += 1
    if line.strip().startswith("Location: "):
        if not "<div " in line.strip():
            print(line.strip().replace("Location: ", ""))
            valmiitirvit.append(line.strip().replace("Location: ", "") + "\n")


#Tallenna valmiit
f = open("finalurls.txt", "w")
f.write(''.join([str(x) for x in list(dict.fromkeys(valmiitirvit))]))
f.close()