def designerPdfViewer(h, word):
    max_height = 0
    for char in word:
        max_height = max(max_height, h[ord(char)-97])
    return max_height * len(word)