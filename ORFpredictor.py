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


# def validate_dna(dna_seq):  # Check if fasta file is a DNA sequence
#     fasta_sequence = dna_seq.upper()
#     for nuc in fasta_sequence:
#         if nuc not in Nucleotides:
#             return "This isn't a DNA sequence"
#     return fasta_sequence


def reverse_compliment(seq):  # Mirrors forward strand + calculates complementary nucleotide resulting in a reverse strand.
    compliment_nucleotides = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    return ''.join([compliment_nucleotides[nucleotide] for nucleotide in seq])[::-1]


def codons(seq):
    for i in range(0, len(seq), 3):
        if (seq[i:i+3] == "TAA" and i%3 == 0) or (seq[i:i + 3] == "TAG" and i%3 == 0) or (seq[i:i+3] == "TGA" and i%3 == 0):
    # return (seq[pos:pos + 3] for pos in range(0, len(seq), 3))


def reading_frames(seq):
    sequence = ''
    for i in range(0, len(seq), 3):
        if len(seq[i:i+3]) == 3:
            sequence += seq[i:i+3] + ''

    ms_1 = [m.start]






# starts = 'ATG'
# stops = ['TAA', 'TAC', 'TAG']
# open_reading = []
# for strand in [validate_dna(seq), reverse_compliment(seq)]:
#     for start in strand:
#         start_co = str(strand[start:start+3])
#         if start_co in starts:
#             frame = str(strand[start:])
#             if any(st in codons(frame[3:], 3) for st in stops):
#                 orf = str(strand[start:])
#                 open_reading.append(orf)
#                 return open_reading

# orfs = orfs.union(set(prot.findall(str(seq[frame]))))

# a = []
# list2 = []
# start_list = 0
# orfs = 0
# for i in range(3):
#     list1.append([])
#     list2.append([])

# for i in range(0, len(seq), 3):
#     if (seq[i:i+3] == stops and i%3 == 0):
#         a = i+3
#         break
#     else:
#         a = None
#
# startcodon = [m.start() for m in re.finditer(starts, seq)]
# print(startcodon)

# codon = seq[i:i+3]
# if(codon in starts):
#     list1[start_list].append(i+1)
# if(codon in stops):
#     list2[start_list].append(i+1)
#
# start_list += 1
# orfs += 1
# print(list1)

# return list1, list2
# frame_one = []
# x = (open_reading_frame.findall(fasta_sequence))
# frame_one.append(x)
# # return set(open_reading_frame.findall(seq))
# print(frame_one)
#
# frame_one = fasta_sequence
# frame_one_orfs = []
# frame_two = ''
# frame_three = ''
# frame_two += fasta_sequence[3:]
# frame_three += fasta_sequence[6:]
# for i in frame_one:
#     if start_codon in frame_one:
#         frame_one_orfs +=

# for i in frame_two:
#     if open_reading_frame in frame_two:
#         frame_one_orfs += open_reading_frame
#     print(frame_one_orfs)

# open_reading_frame = ([ATG]+[TAA|TAC|TAG]){0, 1000}
# open_reading_frame = /([ATG]+[TA].[A|C|G]){0, 1000}
# open_reading_frame = re.compile(r'(?=ATG(?:...)*?)(?=TAA|TAC|TAG)')

