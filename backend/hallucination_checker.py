# backend/hallucination_checker.py

from typing import List, Dict
from .splitter import split_sentences
from .context_builder import build_context  # import context builder

# (Later we'll import actual utils when they exist)
# from .search_verifier import verify_with_search
# from .confidence_scorer import score_confidence

def check_text(text: str, lang: str = "en") -> Dict:
    """
    Main entry point for hallucination checking pipeline.

    Args:
        text (str): Input text to validate.
        lang (str): Language code for sentence splitting.

    Returns:
        Dict: {
            "received_text": str,
            "flagged": List[Dict],       # sentences flagged with reasons
            "chunks": List[str]          # context chunks ready for search
        }
    """
    # Step 1: Split text into sentences
    sentences = split_sentences(text, lang=lang)
    
    # Step 2: Build context chunks from sentences (e.g., 20-30 words each)
    chunks = build_context(sentences, sentences_per_chunk=4, overlap=1)
    flagged: List[Dict] = []
    for chunk in chunks:
        flagged.append({
            "chunk": chunk,
            "flagged": False,
            "reason": "placeholder - verification not implemented yet"
        })
    
    return {
        "received_text": text,
        "flagged": flagged,
        "chunks": chunks
    }