import re

from typing import List, Dict

try:
    import spacy
    nlp = spacy.load("en_core_web_sm")
    spacy_available = True
except:
    spacy_available = False
    print("Spacy not available. falling back to regex-based sentence splitter.")
    
MODEL_MAP = {
    "en": "en_core_web_sm",
    "de": "de_core_news_sm",
    "es": "es_core_news_sm",
    "hi": "xx_ent_wiki_sm",  # basic Hindi support
}
    
def split_sentences(text:str , lang="en")->List[str]:
    
    nlp= None
    
    if spacy_available:
        model_name = MODEL_MAP.get(lang, "en_core_web_sm")
        try:
            nlp = spacy.load(model_name)
            
            if not nlp.has_pipe("parser") and not nlp.has_pipe("sentencizer"):
                nlp.add_pipe("sentencizer")
        except Exception as e:
            print(f"Could not load spacy model '{model_name}': {e}")
            nlp = None
    if nlp:   
        doc = nlp(text)
        return [sent.text.strip()for sent in doc.sents]
   
    if lang == "hi":
         pattern = r'(?<=[।!?])\s+'
    else:
        pattern = r'(?<=[.!?])\s+'
        
    sentences = re.split(pattern, text.strip())
    return [s.strip() for s in sentences if s.strip()]
    
if __name__ == "__main__":
    # English
    english_text = "This is a sentence. This is another sentence."
    print("English:", split_sentences(english_text, lang="en"))

    # Hindi
    hindi_text = "यह एक परीक्षण है। क्या आप ठीक हैं? ठीक है!"
    print("Hindi:", split_sentences(hindi_text, lang="hi"))

    # Spanish
    spanish_text = "Hola mundo. ¿Cómo estás? Esto es una prueba."
    print("Spanish:", split_sentences(spanish_text, lang="es"))

    # German
    german_text = "Hallo Welt. Wie geht es dir? Dies ist ein Test."
    print("German:", split_sentences(german_text, lang="de"))
