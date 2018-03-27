from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals
from tika import parser
import easygui
import re

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words


LANGUAGE = "english"
SENTENCES_COUNT = 15

def initial_match(filename):
    number_pattern = re.compile("^\d+\..*$")
    link_pattern = re.compile("^http://.*$")
    doi_pattern = re.compile("^.*(doi|DOI):.*$")
    header_pattern = re.compile("^.*(Citation|Funding):.*$")
    edited_output = []
    with open(filename) as f:
        for line in f:
            if not number_pattern.match(line) \
            and not link_pattern.match(line) \
            and not doi_pattern.match(line) \
            and not header_pattern.match(line) \
            and line not in ['\n', '\r\n']:
                edited_output.append(line)
            else:
                print("matched line: %s" % line)
    return edited_output

if __name__ == "__main__":
    path = easygui.fileopenbox()
    raw = parser.from_file(path)

    with open("output.txt", "w") as text_file:
        text_file.write(raw['content'])

    edited_output = initial_match("output.txt")

    with open("output.txt", "w") as f:
        f.writelines(edited_output)



    # url = "https://en.wikipedia.org/wiki/Frances_Ivens"
    # parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
    # or for plain text files
    parser = PlaintextParser.from_file("output.txt", Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)
    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)

    with open('final.txt', 'w') as f:
        for sentence in summarizer(parser.document, SENTENCES_COUNT):
            f.write("%s \n" % str(sentence))
