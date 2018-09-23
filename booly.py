# Booly - Colin Burke 2018
# Takes in input and tries to determine what boolean it is.
# Meant to be used for replacing boilerplate user-confirmation prompts.
# See README for examples

from difflib import SequenceMatcher


class Booly:
    # lists of truthy / falsey words
    # these must be sorted by largest-word-first, for higher accuracy on specific matches.
    # unfortunately, one-letter answers need to be deprioritized to ensure fair shakes for larger words
    def __init__(self):
        self.trues = ['unquestionably', 'without fail', 'undoubtedly', 'indubitably', 'good enough', 'affirmative',
                      'sure thing', 'definitely', 'willingly', 'very well', 'precisely', 'of course', 'naturally',
                      'assuredly', 'certainly', 'all right', 'positive', 'continue', 'i guess', 'just so', 'granted', 'exactly',
                      'even so', 'surely', 'gladly', 'sure', 'true', 'okay', 'good', 'fine', 'amen', 'yay', 'yep',
                      'yes', 'aye', 'yea', 'ok', ,'go', '1', 't']
        self.falses = ['negatory', 'negative', 'no way', 'cancel', 'denied', 'false', 'never', 'quit', 'stop', 'exit', 'wait', 'not',
                       'nix', 'nay', 'no', 'f', '0']
        self.item = 0
        self.item = 0
        self.debugging = 0

    # mutator methods for customization of lists
    def truelist_append(self):
        try:
            self.trues.append(self.item)
            self.trues.sort(key=lambda n: len(n))
            self.trues.reverse()
        except (ValueError, KeyError):
            return False

    def truelist_remove(self):
        try:
            self.trues.remove(self.item)
        except (ValueError, KeyError):
            return False

    def falselist_append(self):
        try:
            self.falses.append(self.item)
            self.falses.sort(key=lambda n: len(n))
            self.falses.reverse()
        except (ValueError, KeyError):
            return False

    def falselist_remove(self):
        try:
            self.falses.remove(self.item)
        except (ValueError, KeyError):
            return False

    # if string is at least 80% similar, will return true
    def similar(self, a, b, pct_accuracy):
        ourratio = SequenceMatcher(None, a, b).ratio()
        if ourratio >= pct_accuracy:
            return True
        else:
            return False

    # checks answers against true and false thesaurus
    # takes in a user's input, and compares it against 2 lists of truey and falsey words.
    # it then checks each item in each list, at 100%, and if it fails to find a match, it moves down to 99%.
    def booly(self, answer):
        i = 1
        while i > 0:
            for listitem in self.trues:
                if self.debugging:
                    print('Searching \"' + str(answer) + '\" for up to ' +
                          '{0:.2f}'.format(i) + '% likeliness to \"' + str(listitem) + '\"')
                if self.similar(listitem, answer, i):
                    return [listitem, True]
            for listitem in self.falses:
                if self.similar(listitem, answer, i):
                    return [listitem, False]
            i -= .01
