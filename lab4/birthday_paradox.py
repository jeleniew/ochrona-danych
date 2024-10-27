import hashlib

def trivial_hash(data):
    """Funkcja skrótu MD5."""
    return hashlib.md5(data.encode()).hexdigest()

def create_colliding_documents():
    # Dwa różne dokumenty
    doc1 = "This is the first document."
    doc2 = "This is the second document."
    
    # Modyfikacja dokumentu 1, aby uzyskać kolizję
    modified_doc1 = doc1 + " With some extra content to create a hash collision."
    modified_doc2 = doc2 + " With some extra content to create a hash collision."

    print("Dokument 1:", modified_doc1)
    print("Dokument 2:", modified_doc2)

    hash1 = trivial_hash(modified_doc1)
    hash2 = trivial_hash(modified_doc2)

    print("Hash dokumentu 1:", hash1)
    print("Hash dokumentu 2:", hash2)

create_colliding_documents()
with open("document1.txt", "w") as f:
    f.write(modified_doc1)

with open("document2.txt", "w") as f:
    f.write(modified_doc2)
