def read_file(file_path):  # Opens file. Reads file. Puts header in separate string. Closes file.
    with open(file_path, 'r') as file:
        return [content.strip() for content in file.readlines()]


fasta_file = read_file('sequence.fasta')  # Stores file content in a list
fasta_header = ''  # Header
fasta_sequence = ''  # Sequence

for line in fasta_file:
    if '>' in line:
        fasta_header = line
    else:
        fasta_sequence += line

Nucleotides = ['A', 'T', 'G', 'C']


def validate_dna(dna_seq):  # Check if fasta file is a DNA sequence
    fasta_sequence = dna_seq.upper()
    for nuc in fasta_sequence:
        if nuc not in Nucleotides:
            return "This isn't a DNA sequence"
    return fasta_sequence


def reverse_compliment(seq):  # Mirrors forward strand + calculates complementary nucleotide resulting in a reverse strand.
    compliment_nucleotides = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    return ''.join([compliment_nucleotides[nucleotide] for nucleotide in seq])[::-1]


def codons(seq):
    return (seq[pos:pos + 3] for pos in range(0, len(seq), 3))


def reading_frames(seq):
    sequence = ''
    for i in range(0, len(seq), 3):
        if len(seq[i:i+3]) == 3:
            sequence += seq[i:i+3] + ''

# Writes ORFs to file
output = open("ORFs.txt", 'w')
output.close()
