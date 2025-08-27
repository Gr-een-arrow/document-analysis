
import os
import faiss
import numpy as np
from typing import List, Tuple, Optional

class VectorStore:
    """
    Service for storing and searching embeddings using FAISS.
    Each document's index is stored in user_id/document_id/index.faiss.
    """
    def __init__(self, dim: int):
        self.dim = dim
        self.index = faiss.IndexFlatL2(dim)
        self.ids = []  # Store IDs for mapping

    def add(self, embeddings: np.ndarray, ids: List[str]):
        assert embeddings.shape[1] == self.dim
        self.index.add(embeddings.astype(np.float32))
        self.ids.extend(ids)

    def search(self, query_embedding: np.ndarray, top_k: int = 5) -> List[Tuple[str, float]]:
        D, I = self.index.search(query_embedding.astype(np.float32), top_k)
        results = []
        for idx, dist in zip(I[0], D[0]):
            if idx < len(self.ids):
                results.append((self.ids[idx], float(dist)))
        return results

    def save(self, user_id: str, document_id: str, base_dir: str = "data/faiss_index"):
        """
        Save the FAISS index for a document in user_id/document_id/index.faiss
        """
        dir_path = os.path.join(base_dir, str(user_id), str(document_id))
        os.makedirs(dir_path, exist_ok=True)
        index_path = os.path.join(dir_path, "index.faiss")
        faiss.write_index(self.index, index_path)
        # Save IDs as well
        np.save(os.path.join(dir_path, "ids.npy"), np.array(self.ids))

    def load(self, user_id: str, document_id: str, base_dir: str = "data/faiss_index"):
        """
        Load the FAISS index for a document from user_id/document_id/index.faiss
        """
        dir_path = os.path.join(base_dir, str(user_id), str(document_id))
        index_path = os.path.join(dir_path, "index.faiss")
        self.index = faiss.read_index(index_path)
        ids_path = os.path.join(dir_path, "ids.npy")
        if os.path.exists(ids_path):
            self.ids = np.load(ids_path).tolist()
        else:
            self.ids = []

    def delete_index(self, user_id: str, document_id: str, base_dir: str = "data/faiss_index"):
        """
        Delete the FAISS index and IDs for a document.
        """
        dir_path = os.path.join(base_dir, str(user_id), str(document_id))
        index_path = os.path.join(dir_path, "index.faiss")
        ids_path = os.path.join(dir_path, "ids.npy")
        if os.path.exists(index_path):
            os.remove(index_path)
        if os.path.exists(ids_path):
            os.remove(ids_path)
        # Optionally remove the directory if empty
        try:
            os.rmdir(dir_path)
        except OSError:
            pass
