from typing import List, Dict, Any
from sentence_transformers import SentenceTransformer
import numpy as np

class EmbeddingService:
    """
    Service for chunking text and generating embeddings using Sentence-Transformers.
    """
    def __init__(self, model_name: str = 'all-MiniLM-L6-v2'):
        self.model = SentenceTransformer(model_name)

    def chunk_text(self, text: str, chunk_size: int = 500, overlap: int = 50) -> List[str]:
        """
        Split text into overlapping chunks.
        """
        words = text.split()
        chunks = []
        i = 0
        while i < len(words):
            chunk = words[i:i+chunk_size]
            chunks.append(' '.join(chunk))
            i += chunk_size - overlap
        return chunks

    def embed_chunks(self, chunks: List[str]) -> np.ndarray:
        """
        Generate embeddings for a list of text chunks.
        """
        return self.model.encode(chunks, show_progress_bar=False)

    def process(self, text: str, chunk_size: int = 800, overlap: int = 80) -> List[Dict[str, Any]]:
        """
        Chunk the text and return a list of dicts with chunk text and embedding.
        """
        chunks = self.chunk_text(text, chunk_size, overlap)
        embeddings = self.embed_chunks(chunks)
        return [
            {"text": chunk, "embedding": embedding}
            for chunk, embedding in zip(chunks, embeddings)
        ]
