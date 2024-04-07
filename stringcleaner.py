import nltk
import nltk.corpus
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
nltk.download('punkt')

stopwordlist = stopwords.words('english')

def formatString(input):
    # Split and remove all stop words
    output = input.split(' ')
    output = [word for word in output if word not in stopwordlist]

    # Change words to be singular and breaks down words in different tenses
    for word in output:
        word = PorterStemmer().stem(word)
        word = WordNetLemmatizer.lemmatize(word)
    
    output = ' '.join(output)
    return output

def formatFile(filepath):
    inputString = ''
    with open(filepath, 'r') as f:
        inputString = filepath.read()
    
    with open(filepath, 'w') as f:
        f.write(formatString(inputString))
