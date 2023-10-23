import heapq, sys
from collections import defaultdict

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(txt):
    char_freq = defaultdict(int)
    for char in txt:
        char_freq[char] += 1

    heap = [HuffmanNode(char, freq) for char, freq in char_freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        parent = HuffmanNode(None, left.freq + right.freq)
        parent.left = left
        parent.right = right
        heapq.heappush(heap, parent)

    return heap[0]

def generate_huffman_codes(node, code="", mapping=None):
    if mapping is None:
        mapping = {}
    if node.char is not None:
        mapping[node.char] = code
        print(f"Character: {node.char}, Code: {code}")
    if node.left:
        generate_huffman_codes(node.left, code + "0", mapping)
    if node.right:
        generate_huffman_codes(node.right, code + "1", mapping)
    return mapping

def compress_text(txt):
    huffman_tree = build_huffman_tree(txt)
    huffman_codes = generate_huffman_codes(huffman_tree)
    compressed_text = "".join(huffman_codes[char] for char in txt)
    return compressed_text

def decompress_text(compressed_text, huffman_tree):
    current_node = huffman_tree
    decompressed_text = ""
    for bit in compressed_text:
        if bit == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.char is not None:
            decompressed_text += current_node.char
            current_node = huffman_tree  # Reset to the root

    return decompressed_text

original_text = input("ENTER TEXT TO COMPRESS: ");
compressed_text = compress_text(original_text)

print("Compressed Text:", compressed_text)
decompressed_text = decompress_text(compressed_text, build_huffman_tree(original_text))
print("Decompressed Text:", decompressed_text)

