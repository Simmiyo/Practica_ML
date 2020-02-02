import nltk
from nltk.tokenize import sent_tokenize,word_tokenize,PunktSentenceTokenizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.corpus import state_union
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.corpus import genesis
import re
from string import punctuation
'''
text = "Hello, Mr. Potter! You look great today. How's your son?  The cat is an animal."
text = "the fish is in the sea"
#print(nltk.sent_tokenize(text))
#print(nltk.word_tokenize(text))

stop_words = set(stopwords.words("english"))
#print(stop_words)
words = nltk.word_tokenize(text)
filtered_text = []
for w in words:
    if w not in stop_words:
        filtered_text.append(w)
print(filtered_text)

filtered_text = [w for w in words if w not in stop_words]
print(filtered_text)

words1 = ["accept","accepted","accepting","acceptable","acceptance"]
ps = PorterStemmer()
for w in words1:
    print(ps.stem(w))
newtext = "They will accept you someday because you're acceptable and acceptance is important while accepting proves wisedom. So you'll be accepted."
words1 = nltk.word_tokenize(newtext)
for w in words1:
    print(ps.stem(w))

text1 = state_union.raw('2005-GWBush.txt')
words2 = nltk.word_tokenize(text1)
print(nltk.pos_tag(words2))

print(nltk.pos_tag(words))

l = WordNetLemmatizer()
print(l.lemmatize("canadians"))
print(l.lemmatize("geese"))
print(l.lemmatize("better"))
print(l.lemmatize("better",pos = wordnet.ADJ))

gen = genesis.raw("english-web.txt")
gen = nltk.sent_tokenize(gen)
print(gen[2:20])

syns = wordnet.synsets("program")
print(syns)
print(syns[0])
print(syns[1].lemmas()[0].name())
print(syns[1].definition())
print(syns[0].examples())

synonyms = []
antonyms = []
for s in wordnet.synsets("good"):
    for l in s.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())
print(set(synonyms))
print(set(antonyms))

w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("boat.n.01")
print(w1.wup_similarity(w2))

w1 = wordnet.synset("cat.n.01")
w2 = wordnet.synset("prison.n.01")
print(w1.wup_similarity(w2))

w1 = wordnet.synset("poison.n.01")
w2 = wordnet.synset("angel.n.01")
print(w1.wup_similarity(w2))'''

f = open("/home/simona/PycharmProjects/PRACTICA/cs.CL/art_11.txt", "r")
text = f.read()
f.close()
text = text.lower()
pattern = r"[0-9]"
text = re.sub(pattern, " ", text)
# pattern = r"[@#$%^&*(){}\\=/|_+`~<>]"
pattern = r"[^a-z\.,:;'!\-? \n]"
text = re.sub(pattern, " ", text)
text = re.sub(r"\n", " ", text)
text = nltk.sent_tokenize(text)
dict = {
                     "NN": wordnet.NOUN,
                    "NNS": wordnet.NOUN,
                    "NNP": wordnet.NOUN,
                    "NNPS": wordnet.NOUN,
                    "VB": wordnet.VERB,
                    "VBD": wordnet.VERB,
                    "VBG": wordnet.VERB,
                    "VBN": wordnet.VERB,
                    "VBP": wordnet.VERB,
                    "VBZ": wordnet.VERB,
                    "JJ": wordnet.ADJ,
                    "JJR": wordnet.ADJ,
                    "JJS": wordnet.ADJ,
                    "RB": wordnet.ADV,
                    "RBR": wordnet.ADV,
                    "RBS": wordnet.ADV,
               }
tagg = []
for sent in text:
    tagg.append(nltk.pos_tag(nltk.word_tokenize(sent)))
stop_words = set(stopwords.words("english"))
text = []
for sent in tagg:
    for t in sent:
        if t[0] not in punctuation and t[0] not in stop_words:
            if t[1] in dict:
                text.append((t[0],dict[t[1]]))
            else:
                text.append((t[0],dict["NN"]))
lemma = WordNetLemmatizer()
tagg = []
taggg = ""
for tuple in text:
    #print(tuple[0])
    #print(tuple[1])
    tagg.append(lemma.lemmatize(tuple[0],pos = tuple[1]))
    taggg = taggg + " " + lemma.lemmatize(tuple[0],pos = tuple[1])
print(tagg)
print('\n')
print(taggg)

#print(lemma.lemmatize("testing",pos = "v"))