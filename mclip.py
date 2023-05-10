#! python3
#mclip.py - A multi-clipboard program.
#this is the dictionary named TEXT
TEXT = {'agree': """Yes, I agree. That sounds fine to me.""", 
        'busy':"""Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donatition?"""}

import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage: python myclip.py [keyphrase] - copy phrase text')
    sys.exit()
keyphrase = sys.argv[1]  #first command line arg is the keyphrase

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for ' + keyphrase + ' coped to clipboard.')
else:
    print('Ther is no text for ' + keyphrase)

