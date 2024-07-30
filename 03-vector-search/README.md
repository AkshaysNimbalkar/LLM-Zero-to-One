03 - Vector Search:

Semantic Search: 
documents -> embeddings -> indexing -> store in vecotor db (elastic search) 
user -> query (search) -> embeddings -> search in vector db -> find similar matches -> result

documents : collection of tokens
embeddings: numbers
indexing: storing documents in well suitable formats

Semantic Search: (Contextual search)

Why Vector databases (Vecotr Search) getting Popular?
- 1. 80% of data is unstructured (social media, images, videos etc)
- 2. LLM's lack Long Term Memory (Vector Db's provide ability to store and retrieve data for LLM's)

Vector Embeddings(bunch of numbers):
- used to transform words, sentences and other data into numerical reprasentations (vectors)
- Types: Word, Sentence, Document, Image embeddings

What is Vector database and How do they work?
- 1. A Vector Db indexes and stores vector embeddings in optimized manner.
- 2. Provides ability to compare multiple things(semantically) at the same time.
- 3. searches based on similar things using (Cosine similarity, ecludian distance etc.)
- 4. helps ML models to remember the past data better search

Evaluation Metrics of Retrieval:
1. Ground Truth Data Generation: For Our FAQ Database we have generated 5 questions for each question using OoenAI to evaluate the model results. (ground-truth-data.ipynab)

2. Evaluation of Text Retrieval technique:
    a. HIT Rate/Recall:  Tells if there is relevant document inside the search reasult.
    b. MRR : Gives Ranking to the results

    process: for each q in ground-truth-data:
                execute q

3. Evaluation of Vector Retrieval technique.









