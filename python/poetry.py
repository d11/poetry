import os, sys; sys.path.insert(0, os.path.join("..", ".."))
import itertools

from pattern.web import Wikipedia
from pattern.en import parse, pprint, tag


def parseSection(s):
   # The en module contains a fast regular expressions-based parser.
   # A parser identifies words in a sentence, word part-of-speech tags (e.g. noun, verb)
   # and groups of words that belong together (e.g. noun phrases).
   # Common part-of-speech tags: NN (noun), VB (verb), JJ (adjective), PP (preposition).
   # A tag can have a suffix, for example NNS (plural noun) or VBG (gerund verb).
   # Overview of tags: http://www.clips.ua.ac.be/pages/mbsp-tags
   #s = "I eat pizza with a fork."
   s = s.content
   s = parse(s,
        tokenize = True,  # Tokenize the input, i.e. split punctuation from words.
            tags = False,  # Find part-of-speech tags.
          chunks = False,  # Find chunk tags, e.g. "the black cat" = NP = noun phrase.
       relations = False,  # Find relations between chunks.
         lemmata = False,  # Find word lemmata.
           light = False)

   # The light parameter determines how unknown words are handled.
   # By default, unknown words are tagged NN and then improved with a set of rules.
   # light=False uses Brill's lexical and contextual rules,
   # light=True uses a set of custom rules that is less accurate but faster (5x-10x).


   sentences = s.split()

   for s in sentences:
      if len(s) < 12:
         return
      print " ".join(itertools.chain.from_iterable(s))

   # The output is a string with each sentence on a new line.
   # Words in a sentence have been annotated with tags,
   # for example: fork/NN/I-NP/I-PNP
   # NN = noun, NP = part of a noun phrase, PNP = part of a prepositional phrase.
   #print s
   #print

   # Prettier output can be obtained with the pprint() command:
   #pprint(s)
   #print

   # The string's split() method will (unless a split character is given),
   # split into a list of sentences, where each sentence is a list of words
   # and each word is a list with the word + its tags.
   #print s.split()
   #print 

   # The tag() command returns a list of (word, POS-tag)-tuples.
   # With light=True, this is the fastest and simplest way to get an idea 
   # of a sentence's constituents:
   #s = "I eat pizza with a fork."
   #s = tag(s)
   #print s
   #for word, tag in s:
   #    if tag == "NN": # Find all nouns in the input string.
   #        print word


# This example retrieves an article from Wikipedia (http://en.wikipedia.org).
# A query requests the article's HTML source from the server, which can be quite slow.
# It is a good idea to cache results from Wikipedia locally,
# and to set a high timeout when calling Wikipedia.search().

engine = Wikipedia(language="en")

# Contrary to other search engines in the module,
# Wikipedia simply returns one WikipediaArticle object (or None) instead of a list of results.
article = engine.search("alice in wonderland", cached=True, timeout=30)

#print article.title               # Article title (may differ from the search query).
#print
#print article.languages["fr"]     # Article in French, can be retrieved with Wikipedia(language="fr").
#print article.links[:10], "..."   # List of linked Wikipedia articles.
#print article.external[:5], "..." # List of external URL's.
#print

#print article.source # The full article content as HTML.
#print article.string # The full article content, plain text with HTML tags stripped.

# An article is made up of different sections with a title.
# WikipediaArticle.sections is a list of WikipediaSection objects.
# Each section has a title + content and can have a linked parent section or child sections.
for s in article.sections:
    #print s.title.upper()
    #print 
    #print s.content # = ArticleSection.string, minus the title.
    #print
    parseSection(s)

