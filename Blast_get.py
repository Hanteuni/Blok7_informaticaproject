from Bio.Blast import NCBIWWW
from tkinter import filedialog, messagebox
import time


def main():
    seqs, hdr = file_reader()
    blaster_file(hdr, seqs, count=0)


def file_reader():
    # fname = filedialog.askopenfilename(
    #     initialdir='C:\\', title='Select')
    # fname = "/home/han/augustus.2.5.5/SD.fa"
    fname = "/home/han/Test_document"
    seqs = []
    hdr = []
    seq = ""
    file = open(fname, "r")
    for line in file:
        if line.startswith(">"):
            hdr.append(line)
            if seq != "":
                seqs.append(seq)
                seq = ""
        else:
            seq += line
    seqs.append(seq)
    return seqs, hdr


def blaster_file(hdr, seqs, count):
    """ The blaster_file function gets every sequence and then uses the
    online BLASTx tool (from the NCBI) to blast every sequence. The results
    from these blasts are then put into a file with the appropriate sequence
    header. Furthermore it notes a number in a separate file to keep track
    at wich seqence it was in case of an error.
    :param hdr: list with the headers of the Excel file
    :param seqs: list with the sequences of the Excel file
    :param count: the last index number in the seqs list
    :return: A tkinter message *if everything did go correctly) when all the
    sequences are BLASTED
    """
    try:
        for seq in seqs:
            count = int(count)
            # using time.sleep to not get kicked out of the NCBI server
            print("Sleepy time")
            time.sleep(10)
            # Blasting the sequence online against blastx
            print("-------------=====================---------------\n"
                  "\t \t \t\t BLAST IN PROCESS\n"
                  "-------------=====================---------------")
            result_handle = NCBIWWW.qblast("blastx", "refseq_protein", seq)
            print("\nBEEP BOOP done")
            count = int(count)
            header = hdr[count]
            # Makes the XML with the appropriate header
            file = open(header, "x")
            print("Writing the file ")
            file.write(result_handle.read())
            file.close()
            # creatig a back-up number
            back_up = open('Blast_text', 'w')
            back_up.write(str(count))
            back_up.close()
            count += 1
    except FileExistsError:
        # error so you do not redownload the same file
        file = open('Blast_text')
        count = file.readline()
        file.close()
        # checks for the back-up number
        file = open('Blast_text', 'w')
        count = int(count)
        count += 1
        file.write(str(count))
        file.close()
        # returns to the function with the new back-p number
        return blaster_file(hdr, seqs, count)
    except IndexError:
        messagebox.showinfo('Error', 'Alle bestanden zijn aangemaakt.')

main()
