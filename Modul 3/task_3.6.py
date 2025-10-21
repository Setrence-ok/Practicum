def to_rna(dna):
    dna.upper()
    rules = {'G' : 'C', 'C' : 'G', 'T' : 'A', 'A' : 'U'}
    new_dna = ''
    if len(dna) > 0:
        for char in dna:
            if char in rules:
                for k, v in rules.items():
                    if char == k:
                        new_dna += v
                    else:
                        continue
            else:
                raise TypeError("Недопустимый символ")
        return new_dna
    else:
        return dna




# Пример использования
sequence = "TAGCG"
print("РНК:", to_rna(sequence))