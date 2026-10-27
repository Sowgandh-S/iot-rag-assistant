import re
from pathlib import Path

from app.documents import GUIDE_PATH, chunk_text, load_guide


def _tokens(text: str) -> set[str]:
    """Return lowercase word tokens, ignoring punctuation."""
    return set(re.findall(r"\b[a-z0-9]+\b", text.lower()))


def retrieve_passages(
    question: str,
    path: Path = GUIDE_PATH,
    top_k: int = 3,
) -> list[str]:
    """Return guide passages ranked by shared keywords with the question."""
    if top_k <= 0:
        return []

    guide = load_guide(path)
    chunks = chunk_text(guide)
    question_tokens = _tokens(question)

    if not question_tokens:
        return []

    scored = []
    for chunk in chunks:
        overlap = question_tokens & _tokens(chunk)
        if overlap:
            scored.append((len(overlap), chunk))

    scored.sort(key=lambda item: item[0], reverse=True)
    return [chunk for _, chunk in scored[:top_k]]
