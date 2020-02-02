import re
from string import punctuation
import nltk
from nltk.tokenize import sent_tokenize,word_tokenize,PunktSentenceTokenizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.corpus import state_union
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

cat = ['astro-ph.GA','math.DG','quant-ph','stat.ML','cs.CL','q-bio.NC']
for c in cat:
    for i in range(1,5001):
        #obtaining the data extracted from articles (title & summary) to be processed
        f = open("/home/simona/PycharmProjects/PRACTICA/" + c + "/art_{0}.txt".format(i),"r")
        text = f.read()
        f.close()

        def preprocessing(text):
            #converting capitall letters into small ones
            text = text.lower()
            #removing the numbers from the text
            pattern = r"[0-9]"
            text = re.sub(pattern, " ", text)
            #removing the special characters and the new lines from the text
            pattern = r"[^a-z\.,:;'!\-? \n]"
            text = re.sub(pattern, " ", text)
            text = re.sub(r"\n", " ", text)
            #extracting all the sentences composing the text
            text = nltk.sent_tokenize(text)
            tagg = []
            #extracting the words from the resulted sentences in order to mention which part of speech they are
            for sent in text:
                tagg.append(nltk.pos_tag(nltk.word_tokenize(sent)))
            text = []
            stop_words = set(stopwords.words("english"))
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
            #removing the punctuation and the english common words
            #converting the ordinary pos tags into wordnet pos tags
            for sent in tagg:
                for t in sent:
                    if t[0] not in punctuation and t[0] not in stop_words:
                        if t[1] in dict:
                            text.append((t[0], dict[t[1]]))
                        else:
                            text.append((t[0], dict["NN"]))
            #lemmatizing (i.e. extracting the basic form of each word)
            lemma = WordNetLemmatizer()
            tagg = ""
            for tuple in text:
                tagg = tagg + " " + lemma.lemmatize(tuple[0],pos = tuple[1])
            return tagg

        text = preprocessing(text)
        g = open('/home/simona/PycharmProjects/PRACTICA/modified_{0}/art_{1}.txt'.format(c, i), 'w')
        g.write(text)
        g.close()
