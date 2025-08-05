def proteins(strand):
    amino_acids = {"Methionine": ["AUG"],
                  "Phenylalanine": ["UUU", "UUC"],
                  "Leucine": ["UUA", "UUG"],
                  "Serine": ["UCU", "UCC", "UCA", "UCG"],
                  "Tyrosine": ["UAU", "UAC"],
                  "Cysteine": ["UGU", "UGC"],
                  "Tryptophan": ["UGG"],
                  "STOP": ["UAA", "UAG", "UGA"]}

    groups = [strand[i:i+3] for i in range(0, len(strand), 3)]

    proteins = []
    for item in groups:
        # Check if the item is equals to the values of STOP
        # Return nothing if so
        if item in amino_acids["STOP"]:
            break
        for key, value in amino_acids.items():
            for codon in value:
                if item == codon:
                    proteins.append(key)
    return proteins