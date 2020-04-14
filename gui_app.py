import tkinter
from tkinter import filedialog

orf_array = ['.', '..', '...', '....', '.....', '......', '.....', '....', '...', '..', '.']
blast_array = ['.', '..', '...', '....', '.....', '......', '.....', '....', '...', '..', '.']


class gui_ORF:
    def __init__(self):
        """
        This function creates the GUI including a label, buttons, textareas and scrollbars.
        """
        # main window
        self.main_window = tkinter.Tk()
        self.main_window.title('ORF Predictor')

        # file button
        self.file_btn = tkinter.Button(self.main_window, text='Choose file', command=self.file_btn)
        self.file_btn.pack()

        # label text
        self.label = tkinter.Label(self.main_window, text='Sequence')
        self.label.pack()

        # sequence scrollbar
        scrollbar = tkinter.Scrollbar(self.main_window)
        scrollbar.pack(side='right', fill='y')

        # sequence textarea
        self.seq_text = tkinter.Text(self.main_window, height=10, width=80, yscrollcommand=scrollbar.set)
        self.seq_text.pack()
        scrollbar.config(command=self.seq_text.yview)

        # orf button
        self.orf_btn = tkinter.Button(self.main_window, text='ORF finder', command=self.orf_btn)
        self.orf_btn.pack()

        # ORF scrollbar
        scrollbar2 = tkinter.Scrollbar(self.main_window)
        scrollbar2.pack(side='right', fill='y')

        # ORF textarea
        self.orf_text = tkinter.Listbox(self.main_window, height=10, width=60, yscrollcommand=scrollbar2.set)
        self.orf_text.pack()
        scrollbar2.config(command=self.orf_text.yview)

        # BLAST button
        self.blast_btn = tkinter.Button(self.main_window, text='BLAST search', command=self.blast_btn)
        self.blast_btn.pack()

        # BLAST scrollbar
        scrollbar3 = tkinter.Scrollbar(self.main_window)
        scrollbar3.pack(side='right', fill='y')

        # BLAST textarea
        self.blast_text = tkinter.Listbox(self.main_window, height=10, width=60, yscrollcommand=scrollbar3.set)
        self.blast_text.pack()
        scrollbar3.config(command=self.blast_text.yview)

        tkinter.mainloop()

    def file_btn(self):
        """
        This function clears the textarea if not empty.
        Gives the user the option to choose a file from a dialog filechooser.
        The content of this file will be shown in the sequence textarea.
        """
        filename = filedialog.askopenfilename()
        if self.seq_text.index("end") != 0:
            self.seq_text.delete(1.0, tkinter.END)
        self.seq_text.insert('end', open(filename).read())
        print(filename)

    def orf_btn(self):
        """
        This function clears the textarea if not empty.
        Loops through the ORF array and inserts the content into the ORF textarea.
        """
        if self.orf_text.index("end") != 0:
            self.orf_text.delete('0', tkinter.END)
        for x in orf_array:
            self.orf_text.insert('end', x)

    def blast_btn(self):
        """
        This function clears the textarea if not empty.
        Loops through the BLAST array and inserts the content into the BLAST textarea.
        """
        if self.blast_text.index("end") != 0:
            self.blast_text.delete('0', tkinter.END)
        for x in blast_array:
            self.blast_text.insert('end', x)


if __name__ == '__main__':
    gui_ORF()


