from collections import defaultdict, Counter
import re
from textblob import TextBlob



class Booklib:
    def __init__(self):
        self.data = defaultdict(dict)

    @staticmethod
    def _default_parser(file):
        with open(file) as f:
            lines = f.readlines()

            # Remove the beginning and end of text disclaimers
            lines = lines[25:-351]

            # Create a duplicate list for modification in place
            temp = []
            for i in range(len(lines)):

                # Filters out the unique quotation marks in the books
                filt1 = re.sub('[“”]', '', lines[i]).strip()

                # Remove people and brackets
                filt2 = re.sub(r'\[[^\]]*\]', '', re.sub(r'[A-Z]+\s+','', re.sub(r'[A-Z]+\.', '', filt1)))

                # Removes empty strings from the list
                temp = [i for i in temp if i]

                if 'Chapter' not in lines[i]:
                    temp.append(filt2)






    def load_text(self, file, label=None, parser=None):
        if parser == None:
            results = Booklib._default_parser(file)
        else:
            pass

        self._save_results()


    def _save_results(self, label, results):
        pass


bl = Booklib()
bl._default_parser('pg2641.txt')
# bl._default_parser('pg1513.txt')
# bl._default_parser('1400-0.txt')




