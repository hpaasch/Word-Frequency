#import sys and use argv to require filename to be input on command line
import string

def getKey(item):
    return item[1]

histogram = {}
hist_list = []
#this list could've been split instead of hand-repaired.
ignore_list = ["a", "able", "about", "across", "after", "all", "almost", "also", "am", "among",
               "an", "and", "any", "are", "as", "at", "be", "because", "been", "but",
               "by", "can", "cannot", "could", "dear", "did", "do", "does", "either",
               "else", "ever", "every", "for", "from", "get", "got", "had", "has", "have",
               "he", "her", "hers", "him", "his", "how", "however", "i", "if", "in", "into",
               "is", "it", "its", "just", "least", "let", "like", "likely", "may", "me",
               "might", "most", "must", "my", "neither", "no", "nor", "not", "of", "off",
               "often", "on", "only", "or", "other", "our", "own", "rather", "said", "say",
               "says", "she", "should", "since", "so", "some", "than", "that", "the", "their",
               "them", "then", "there", "these", "they", "this", "tis", "to", "too", "twas",
               "us", "wants", "was", "we", "were", "what", "when", "where", "which", "while",
               "who", "whom", "why", "will", "with", "would", "yet", "you", "your"]


sherlock_book = open("sampletext.txt")

parse_the_book = sherlock_book.read().lower()

for d in string.punctuation:
    parse_the_book = parse_the_book.replace(d, "").replace("\n", " ").replace("  ", " ").replace("-", " ")# add hyphen

parse_the_book = parse_the_book.split(" ")

for word in parse_the_book:
    if word in ignore_list:
        continue
    if word in histogram.keys():
        histogram[word] += 1
    else:
        histogram[word] = 1

for key, value in histogram.items():
    temp = [key, value]
    hist_list.append(temp)

top_20 = ((sorted(hist_list, key=getKey, reverse=True))[0:20])
most_uses = top_20[0][1]

for key, value in top_20:
    print(key)
    print("#" * (int(value * (50 / most_uses))))

sherlock_book.close()

# subtract len of word to get buffer


# create list variable. go thru the sorted list. second index and append.
# use max(list) to find biggest number