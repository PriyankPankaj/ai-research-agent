from src.rag.retriever import Retriever

SAMPLE_DOCS = [
    "Climate change is causing ocean temperatures to rise, leading to coral bleaching events worldwide. When water is too warm, corals expel the algae living in their tissues, causing them to turn completely white.",
    "Coral reefs support approximately 25% of all marine species despite covering less than 1% of the ocean floor. They are often called the rainforests of the sea due to their biodiversity.",
    "Ocean acidification, caused by increased CO2 absorption, reduces the availability of carbonate ions that corals need to build their calcium carbonate skeletons, weakening reef structures over time.",
    "The Great Barrier Reef has experienced multiple mass bleaching events since 2016, with rising sea temperatures being the primary driver of coral mortality in the region.",
    "Machine learning models can process large datasets efficiently, but require careful validation to avoid overfitting on training data.",
]

if __name__ == "__main__":
    retriever = Retriever()
    retriever.add_documents(SAMPLE_DOCS)
    print(f"Added {len(SAMPLE_DOCS)} documents to the vector store.")