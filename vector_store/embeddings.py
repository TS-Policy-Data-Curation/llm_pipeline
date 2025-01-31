from sycamore.transforms.explode import Explode
from sycamore.transforms.merge_elements import GreedySectionMerger
from sycamore.functions.tokenizer import HuggingFaceTokenizer
from sycamore.transforms.embed import SentenceTransformerEmbedder

def embed_docs(doc_transformed, embedding_model="thenlper/gte-small"):
    tokenizer = HuggingFaceTokenizer(embedding_model)
    embedder = SentenceTransformerEmbedder(model_name=embedding_model, batch_size=100)

    embedded_docs = doc_transformed.explode().embed(embedder)

    # embedded_docs.take_all() #converts a doc set --> list of docs, then use a for loop

    return embedded_docs