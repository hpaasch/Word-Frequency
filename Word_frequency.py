import string

def getKey(item):
    return item[1]

histogram = {}
hist_list = []

sherlock_book = open("sampletext.txt")

parse_the_book = sherlock_book.read().lower()

for d in string.punctuation:
    parse_the_book = parse_the_book.replace(d, "").replace("\n", " ").replace("  ", "").replace("-", " ")# add hyphen

parse_the_book = parse_the_book.split(" ")

for word in parse_the_book:
    if word in histogram.keys():
        histogram[word] += 1
    else:
        histogram[word] = 1

for key, value in histogram.items():
    temp = [key, value]
    hist_list.append(temp)

top_20 = ((sorted(hist_list, key=getKey, reverse=True))[0:19])
for key, value in top_20:
    print(key, value)

sherlock_book.close()
