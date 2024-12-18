fname = input("Enter the file name: ")
try:
    fhand = open(fname)
except:
    print(f"file cannot be opened: {fname}")
    exit()

search_word = input("Enter the word to search for: ").strip()
count = 0

for line in fhand:
    if line.startswith(search_word):
        count += 1
if count == 1:
    print(f"There was 1 line starting with '{search_word}' in {fname}")
else:
    print(f"There were {count} line starting with '{search_word}' in {fname}")