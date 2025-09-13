# backend/context_builder.py

from typing import List

def build_context(sentences: List[str], sentences_per_chunk: int = 4, overlap: int = 1) -> List[str]:
    """
    Builds context-aware chunks from a list of sentences for search queries.
    Overlapping sentences are included for better context.

    Args:
        sentences (List[str]): List of pre-split sentences.
        sentences_per_chunk (int): Number of sentences per chunk.
        overlap (int): Number of overlapping sentences between chunks.

    Returns:
        List[str]: List of context chunks (strings) ready for verification/search.
    """
    chunks = []
    n = len(sentences)
    i = 0

    while i < n:
        # Take sentences for the current chunk
        chunk_sentences = sentences[i:i + sentences_per_chunk]
        chunk = " ".join(chunk_sentences)
        chunks.append(chunk)

        # Move index forward, keeping overlap
        i += sentences_per_chunk - overlap
        if i < 0:  # safety check
            i = 0

    return chunks

# --- Sample usage ---
if __name__ == "__main__":
    sample_sentences = [
        "This is the first sentence.",
        "Here is the second one, a bit longer than the first.",
        "Third sentence goes here.",
        "Finally, the last sentence in this small example.",
        "Extra sentence to test overlapping."
    ]
    
    for chunk in build_context(sample_sentences, sentences_per_chunk=4, overlap=1):
        print(chunk)
