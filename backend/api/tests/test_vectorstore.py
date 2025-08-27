import os
import shutil
import numpy as np
from django.test import TestCase
from services.vectorstore import VectorStore

class TestVectorStore(TestCase):
    def setUp(self):
        self.dim = 4
        self.user_id = "testuser"
        self.document_id = "doc1"
        self.base_dir = "test_faiss_index"
        self.vs = VectorStore(self.dim)
        self.embeddings = np.array([[1, 2, 3, 4], [4, 3, 2, 1]], dtype=np.float32)
        self.ids = ["chunk1", "chunk2"]

    def tearDown(self):
        # Clean up test directory
        dir_path = os.path.join(self.base_dir, self.user_id, self.document_id)
        if os.path.exists(dir_path):
            shutil.rmtree(os.path.join(self.base_dir, self.user_id))

    def test_add_and_search(self):
        self.vs.add(self.embeddings, self.ids)
        query = np.array([[1, 2, 3, 4]], dtype=np.float32)
        results = self.vs.search(query, top_k=1)
        self.assertEqual(results[0][0], "chunk1")

    def test_save_and_load(self):
        self.vs.add(self.embeddings, self.ids)
        self.vs.save(self.user_id, self.document_id, self.base_dir)
        # Create a new instance and load
        vs2 = VectorStore(self.dim)
        vs2.load(self.user_id, self.document_id, self.base_dir)
        self.assertEqual(vs2.ids, self.ids)
        query = np.array([[1, 2, 3, 4]], dtype=np.float32)
        results = vs2.search(query, top_k=1)
        self.assertEqual(results[0][0], "chunk1")

    def test_delete_index(self):
        self.vs.add(self.embeddings, self.ids)
        self.vs.save(self.user_id, self.document_id, self.base_dir)
        self.vs.delete_index(self.user_id, self.document_id, self.base_dir)
        dir_path = os.path.join(self.base_dir, self.user_id, self.document_id)
        self.assertFalse(os.path.exists(os.path.join(dir_path, "index.faiss")))
        self.assertFalse(os.path.exists(os.path.join(dir_path, "ids.npy")))
        self.assertFalse(os.path.exists(dir_path))
