"""
SQLite module tests
"""

from txtai.embeddings import Embeddings

from .testfiledb import Common


# pylint: disable=R0904
class TestSQLite(Common.TestFileDB):
    """
    Embeddings with content stored in SQLite tests.
    """

    @classmethod
    def setUpClass(cls):
        """
        Initialize test data.
        """

        cls.data = [
            "US tops 5 million confirmed virus cases",
            "Canada's last fully intact ice shelf has suddenly collapsed, forming a Manhattan-sized iceberg",
            "Beijing mobilises invasion craft along coast as Taiwan tensions escalate",
            "The National Park Service warns against sacrificing slower friends in a bear attack",
            "Maine man wins $1M from $25 lottery ticket",
            "Make huge profits without work, earn up to $100,000 a day",
        ]

        # Content backend
        cls.backend = "sqlite"

        # Create embeddings model, backed by sentence-transformers & transformers
        cls.embeddings = Embeddings({"path": "sentence-transformers/nli-mpnet-base-v2", "content": cls.backend})

    @classmethod
    def tearDownClass(cls):
        """
        Cleanup data.
        """

        if cls.embeddings:
            cls.embeddings.close()


def length(text):
    """
    Custom SQL function.
    """

    return len(text)
