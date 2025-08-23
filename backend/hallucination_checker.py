# backend/hallucination_checker.py

from typing import List, Dict

# (Later we'll import actual utils when they exist)
# from .sentence_splitter import split_sentences
# from .search_verifier import verify_with_search
# from .confidence_scorer import score_confidence

def check_text(text: str) -> Dict:
    """
    Main entry point for hallucination checking pipeline.

    Args:
        text (str): Input text to validate.

    Returns:
        Dict: {
            "received_text": str,
            "flagged": List[Dict]  # sentences flagged with reasons
        }
    """
    sentences = [text]  # placeholder until splitter is ready
    
    flagged: List[Dict] = [] 
    for sentence in sentences:
        flagged.append({
            "sentence": sentence,
            "flagged": False,
            "reason": "placeholder - verification not implemented yet"
        })
        
    return {
        "received_text": text,
        "flagged": flagged
    }
