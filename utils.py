from chunker import TextChunker


chunker = TextChunker("company_docs.txt")

chunks = chunker.create_chunks()

print(f"\nTotal Chunks : {len(chunks)}\n")

for index, chunk in enumerate(chunks):

    print("=" * 50)

    print(f"Chunk {index + 1}")

    print("=" * 50)

    print(chunk)

    print()