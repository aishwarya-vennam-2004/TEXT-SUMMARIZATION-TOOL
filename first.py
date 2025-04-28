import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from collections import Counter
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

# Download NLTK data once
nltk.download('punkt_tab', quiet=True)
nltk.download('stopwords', quiet=True)

def extractive_summary(text, num_sentences=3):
    """Improved extractive summary with length check"""
    if len(sent_tokenize(text)) < num_sentences:
        return "Text too short for extractive summarization (needs multiple sentences)"
    
    sentences = sent_tokenize(text)
    words = [w.lower() for w in word_tokenize(text) if w.isalnum()]
    freq = Counter(words)
    
    ranked = sorted(sentences,
                   key=lambda s: sum(freq.get(w.lower(), 0) 
                                   for w in word_tokenize(s) if w.isalnum()),
                   reverse=True)
    return ' '.join(ranked[:num_sentences])

def abstractive_summary(text, num_sentences=3):
    """Improved abstractive summary with error handling"""
    try:
        parser = PlaintextParser.from_string(text, Tokenizer("english"))
        summarizer = LsaSummarizer()
        summary = summarizer(parser.document, num_sentences)
        return ' '.join(str(s) for s in summary) or "No summary generated"
    except Exception as e:
        return f"Abstractive summarization failed: {str(e)}"

def summarize_text(text, num_sentences=3):
    """Robust summarization with validation"""
    if not text or len(text.split()) < 50:  # Minimum 50 words
        return {"Error": "Text too short - needs at least 50 words for meaningful summarization"}
    
    return {
        "Extractive": extractive_summary(text, num_sentences),
        "Abstractive": abstractive_summary(text, num_sentences)
    }

if __name__ == "__main__":
    # Example with proper long text
    input_text = """
    Natural language processing (NLP) is a subfield of linguistics, computer science, 
    and artificial intelligence concerned with the interactions between computers and human language. 
    It focuses on how to program computers to process and analyze large amounts of natural language data. 
    The result is a computer capable of "understanding" the contents of documents, including the contextual 
    nuances of the language within them. The technology can then accurately extract information and insights 
    contained in the documents as well as categorize and organize the documents themselves.
    
    Challenges in natural language processing frequently involve speech recognition, natural language 
    understanding, and natural language generation. Modern NLP algorithms are based on machine learning, 
    especially statistical machine learning. The paradigm of machine learning is different from that of 
    most prior attempts at language processing. Prior implementations often involved direct hand-coding 
    of large sets of rules.
    
    NLP has many applications including machine translation, chatbots, sentiment analysis, and text 
    summarization. Text summarization is particularly useful for condensing long documents into shorter 
    versions while preserving key information. This helps readers quickly understand the main points 
    without reading the entire content.
    """
    
    summaries = summarize_text(input_text)
    for name, summary in summaries.items():
        print(f"\n=== {name} Summary ===")
        print(summary)