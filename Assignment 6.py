text = "X-DSPAM-Confidence:    0.8475";
pos = text.find(':')
piece = text[pos+5:]
xyz = float(piece)
print(piece)
