from Bio.Blast import NCBIXML
from tkinter import filedialog
import re
import mysql.connector
from Bio import SearchIO, Entrez, SeqIO
import urllib
import time


def main():
    seqs, hdr = file_reader()
    lijst_posities, data = xml_file_reader(hdr, seqs)
    data = data_sorter(hdr, lijst_posities, data)
    data_tuplelist_lineage, data_tuplelist_protein, \
    data_tuplelist_fragment = data_sorteren(data)
    data_insertie(data_tuplelist_lineage, data_tuplelist_protein,
                  data_tuplelist_fragment)


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


def xml_file_reader(hdr, seqs):
    """The xml_file_reader function reads the XML by looping through the hdr
    list. Then the function puts all the data in a list(see data). The
    function also makes a list with the position  of the data
    :param hdr: list with the headers of the Excel file
    :param seqs: list with the sequences of the Excel file
    :return: lijst_posities: list with positions of the data
    data: a list with the data form the XML files
    *note: The XML have to be in the same directory as the py file
    """
    data = []
    lijst_posities = []
    positie = -1
    positie2 = -1
    for header in hdr:
        positie2 += 1
        result_handle = open(header)
        blast_record = NCBIXML.read(result_handle)
        count = 0
        for alignment in blast_record.alignments:
            for hsp in alignment.hsps:
                if count < 100:
                    positie += 1
                    # appends the position to lijst_posities
                    lijst_posities.append(positie)
                    data.append([])
                    count += 1
                    query_coverage = round((hsp.query_end - hsp.query_start)
                                           / hsp.query_end, 3)
                    # print("test4")
                    # # appends information we want to a list
                    # print("score:",hsp.score)
                    # print("espect:",hsp.expect)
                    # print("start",hsp.query_start)
                    # print("stop",hsp.query_end)
                    # print("frame",hsp.frame)
                    # print("coverage:",query_coverage)
                    data[positie].append(hdr[positie2])         #hdr
                    data[positie].append(seqs[positie2])        #seq
                    data[positie].append(hsp.expect)            #E-val
                    data[positie].append(hsp.score)             #score
                    data[positie].append(hsp.query_start)       #startpos
                    data[positie].append(hsp.query_end)         #stoppos
                    data[positie].append(query_coverage)        #Qcov
    return lijst_posities, data


def data_sorter(hdr, lijst_posities, data):
    """ The data_sorter function sorts the data from the XML files. It also
    ''cleans'' the data so it looks better in the database.
    :param hdr: list with the headers of the Excel file
    :param lijst_posities:  list with positions of the data
    :param data: a list with the data form the XML files
    :return: data: tuples of filtered data from the XML files
    """
    teller = -1
    hdr_filtered = []
    for header in hdr:
        query_result = SearchIO.parse(header, 'blast-xml')
        for result in query_result:
            count = 0
            for hit in result:
                # checks every chosen hit
                for hsp in hit:
                    if count < 100:
                        teller += 1
                        data[lijst_posities[teller]].append(
                            hit.description.split('[')[1].strip(']'))
                        data[lijst_posities[teller]].append(
                            hit.description.split('[')[0])
                        data[lijst_posities[teller]].append(hit.accession)
                        count += 1
    for header in hdr:
        blast_qresult = SearchIO.read(header, "blast-xml")
        if len(blast_qresult) != 0:
            hdr_filtered.append(header)
    return data


def data_sorteren(data):
    """ The data_sorteren sorts the data and makes them into tuples to
    insert into the database.
    :param data: tuples of filtered data from the XML files
    :return: data_tuplelist_lineage: Tuplelist of the lineage to insert into
    the database
     data_tuplelist_protein: Tuplelist of the protein to insert into
    the database
     data_tuplelist_fragment: Tuplelist of the fragment to insert into
    the database
    """
    data_tuplelist_lineage = []
    data_list_protein = []
    data_tuplelist_protein = []
    data_tuplelist_fragment = []
    counter = -1
    for lijst in data:
        data_tuplelist_fragment.append(tuple(lijst[0:2]))           #header + seq
        data_list_protein.append((lijst[2:7]))
        data_tuplelist_lineage.append(tuple([lijst[7]]))            #latijnse naame
    for lijst2 in data:
        counter += 1
        data_list_protein[counter].extend(tuple(lijst2[9:10]))      #Accesion code
    for lijst3 in data_list_protein:
        data_tuplelist_protein.append(tuple(lijst3))                #e-val, score, start, stop, qcov

    return data_tuplelist_lineage, data_tuplelist_protein, \
           data_tuplelist_fragment

def data_insertie(data_tuplelist_lineage, data_tuplelist_protein,
                  data_tuplelist_fragment):
    """The data_insertie insert the tuple lists(se parameters) into the
    database using mysql.connector.
    :param data_tuplelist_lineage:  Tuplelist of the lineage to insert into
    the database
    :param data_tuplelist_protein: Tuplelist of the protein to insert into
    the database
    :param data_tuplelist_fragment:  Tuplelist of the fragment to insert into
    the database
    :return: message when the lists are succesfully inserted into the database
    """
    conn = mysql.connector.connect(
        host="hannl-hlo-bioinformatica-mysqlsrv.mysql.database.azure.com",
        user="owe7_pg6@hannl-hlo-bioinformatica-mysqlsrv",
        password="blaat1234",
        db="owe7_pg6")
    insert_gegevens = ""
    query = "INSERT INTO query (header, sequence) " \
            "VALUES (%s, %s)"
    for item in data_tuplelist_fragment:
        print(item[0])      #blast_id
        print(item[1])      #seq
        tempList = []
        tempList.append(item[0])
        tempList.append(item[1])
        insert_gegevens = tuple(tempList)
    Prepared=True
    cursor = conn.cursor(prepared=True)
    cursor.executemany(query, insert_gegevens)
    cursor.close()
    conn.commit()
    print("---------Data insertion into table Protein done----------")
    print("Insertion done, closing connection...")
    conn.close()
    print("Connection closed")


main()
