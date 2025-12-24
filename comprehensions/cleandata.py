raw_users = [" ALICE ", "bob", " C ", "CHarlie", "Jo "]
strippedlist = []
finale = []
for name in raw_users:
    strippedlist.append(name.strip().lower())
for item in strippedlist:
    if len(item) >3:
        finale.append(item)
print(finale)
