#TEXT-SUMMARIZATION-TOOL

COMPANY:CODE TECH IT SOLUTIONS

NAME:VENNAM AISHWARYA

INTERN ID: CT04WT94

DOMAIN:ARTIFICIAL INTELLIGENT

DURATION:4 WEEKS

How the Code Works:

1. Import Libraries
nltk: For tokenizing text into sentences and words.

collections.Counter: To calculate word frequencies.

sumy.parsers.plaintext, sumy.nlp.tokenizers, and sumy.summarizers.lsa:

To perform abstractive summarization using Latent Semantic Analysis (LSA).

2. Extractive Summarization
Function: extractive_summary(text, num_sentences=3)

Purpose: Picks the most important sentences from the article.

How:

Split text into sentences (sent_tokenize).

Tokenize words and compute word frequency (word_tokenize + Counter).

Rank sentences based on the sum of word frequencies.

Return the top num_sentences ranked sentences.

3. Abstractive Summarization
 
4.Function: abstractive_summary(text, num_sentences=3)

Purpose: Create a shorter version of the article by understanding the text (via LSA).

How:

Parse the article into a document format (PlaintextParser).

OUTPUT:2. Extractive Summarization


