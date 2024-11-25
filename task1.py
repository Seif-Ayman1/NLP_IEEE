import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.isri import ISRIStemmer
from nltk.stem.porter import PorterStemmer 
import re  
nltk.download('punkt') 
nltk.download('stopwords')  
ArabicText = "فِي فَصْلِ الشِّتَاءِ، تَتَسَاقَطُ الْأَمْطَارُ بِغَزَارَةٍ عَلَى الْجِبَالِ، وَتَجْرِي الْأَنْهَارُ بِسُرْعَةٍ كَبِيرَةٍ، مِمَّا يُجْعِلُ الْمُزَارِعِينَ يَشْعُرُونَ بِالسَّعَادَةِ بِسَبَبِ تَوَافُرِ الْمِيَاهِ اللَّازِمَةِ لِرَيِّ الْمَحَاصِيلِ الزِّرَاعِيَّةِ الَّتِي يَعْتَمِدُونَ عَلَيْهَا كَمَصْدَرٍ رَئِيسِيٍّ لِلْعَيْشِ." 
EnglishText = "In the winter season, heavy rains pour down on the mountains, and rivers flow rapidly, bringing joy to farmers as the availability of water becomes sufficient for irrigating the agricultural crops they rely on for their livelihood."  
def tokenize_text(text, language):     
    if language == 'arabic' :         
        tokens = word_tokenize(text, language='arabic')     
    else:         
        tokens = word_tokenize(text, language='english')     
    return tokens  

def Renoise(text):     
    text = re.sub(r'[^\w\s]','',text)             
    text = re.sub(r'\d+','',text)      
    return text  

def ReStopWords(words, language):     
    if language == 'arabic':         
        arabic_stop_words = set(stopwords.words('arabic')) if 'arabic' in stopwords.fileids() else set(['في', 'من', 'على', 'إلى', 'عن', 'و', 'يا', 'لكن', 'هذا', 'ما'])             
        filter_words = [word for word in words if word not in arabic_stop_words]
    else:
        english_stop_words = set(stopwords.words('english'))
        filter_words = [word for word in words if word not in english_stop_words]
    return filter_words

def normalize_text(text):
    text = re.sub(r'[\u064B-\u065F]','', text)
    text = re.sub(r'[أآإا]', 'ا', text) 
    text = re.sub(r'[ؤ]', 'و', text)
    text = re.sub(r'[ى]', 'ي', text)
    text = re.sub(r'[ة]', 'ه', text)  
    text = re.sub(r'[ء]', '', text)
    return text.lower()

def stem_text(text, language):
    if language=='arabic':
        stemmer = ISRIStemmer()
    else:
        stemmer = PorterStemmer()
    return [stemmer.stem(word) for word in text]         

def TextPreprocess(text, language):

    final_text = stem_text(ReStopWords(tokenize_text(Renoise(normalize_text(text)),language),language),language)

    return ' '.join(final_text)

print ("English Preprocessing : ",TextPreprocess(EnglishText, 'english'))
print ("Arabic Preprocessing : ",TextPreprocess(ArabicText, 'arabic'))