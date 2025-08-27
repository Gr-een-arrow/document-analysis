from django.test import TestCase
from services.embeddings import EmbeddingService


class TestEmbeddingService(TestCase):
    def setUp(self):
        self.embedding_service = EmbeddingService()
        self.text = "This is a test document. It contains several sentences. This is for embedding."
        self.sample_text = "The quick brown fox jumps over the lazy dog. Pack my box with five dozen liquor jugs."

    def test_chunk_text(self):
        # Test with known sample text and chunking
        chunks = self.embedding_service.chunk_text(self.sample_text, chunk_size=5, overlap=2)
        expected = [
            "The quick brown fox jumps",
            "fox jumps over the lazy",
            "the lazy dog. Pack my",
            "Pack my box with five",
            "with five dozen liquor jugs.",
            "liquor jugs."
        ]
        print("Actual chunks:", chunks)
        print("Expected chunks:", expected)

        self.assertEqual(chunks, expected)

    def test_embed_chunks(self):
        chunks = ["This is a test.", "Another chunk."]
        embeddings = self.embedding_service.embed_chunks(chunks)
        self.assertEqual(len(embeddings), len(chunks))
        self.assertEqual(len(embeddings[0].shape), 1)  # Should be a 1D vector

    def test_process(self):
        # Use sample_text for deterministic chunking
        results = self.embedding_service.process(self.sample_text, chunk_size=5, overlap=2)
        self.assertTrue(len(results) > 0)
        self.assertIn("text", results[0])
        self.assertIn("embedding", results[0])


