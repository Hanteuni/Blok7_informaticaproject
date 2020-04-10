import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.io.*;
import java.util.ArrayList;

public class guiORF extends JFrame
        implements ActionListener {

    private JButton openFileButton, predictORF, blastORF;
    private JFileChooser fileChooser;
    private JTextField fileText, numberORF;
    private JLabel labSequenceText, labNumberText;
    private JTextArea sequenceText, orfText, blastText;
    private BufferedReader inFile;
    private JScrollPane scroll;

    private String sequence = "";

    ArrayList<ORF> orfs = new ArrayList<>();
    ArrayList<BLAST> blasts = new ArrayList<>();

    public static void main(String[] args) {
        try {
            UIManager.setLookAndFeel("com.sun.java.swing.plaf.gtk.GTKLookAndFeel");
        } catch (UnsupportedLookAndFeelException | ClassNotFoundException | InstantiationException | IllegalAccessException e) {
        }

        guiORF gui = new guiORF();

        gui.addORF(new ORF(1, 10, 100, 90, "ATGCAGCAGA", 1, 1));
        gui.addORF(new ORF(2, 10, 100, 90, "ATGCAGCAGAATGCAGCAGAATGCAGCAGA", 2, 1));
        gui.addORF(new ORF(3, 10, 100, 90, "ATGCAGCAGAATGCAGCAGA", 3, 1));

        gui.addBLAST(new BLAST(1, "f", 1, 1, 1));
        gui.addBLAST(new BLAST(1, "f", 1, 1, 1));
        gui.addBLAST(new BLAST(1, "f", 1, 1, 1));
        gui.addBLAST(new BLAST(1, "f", 1, 1, 1));

        gui.setSize(750, 750);
        gui.setResizable(false);
        gui.setDefaultCloseOperation(EXIT_ON_CLOSE);

        gui.createGUI();

        System.out.println(gui.sequence);
        gui.setVisible(true);
    }

    private void createGUI() {
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        Container window = getContentPane();
        window.setLayout(new FlowLayout());

        labSequenceText = new JLabel("Sequence:");
        window.add(labSequenceText);

        openFileButton = new JButton("choose file");
        window.add(openFileButton);
        openFileButton.addActionListener(this);

        fileText = new JTextField(25);
        window.add(fileText);

        sequenceText = new JTextArea(10, 60);
        sequenceText.setEditable(false);
        scroll = new JScrollPane(sequenceText);
        scroll.setVerticalScrollBarPolicy(ScrollPaneConstants.VERTICAL_SCROLLBAR_ALWAYS);
        window.add(scroll);

        predictORF = new JButton("predict ORFs");
        window.add(predictORF);
        predictORF.addActionListener(this);

        orfText = new JTextArea(10, 60);
        orfText.setEditable(false);
        scroll = new JScrollPane(orfText);
        scroll.setVerticalScrollBarPolicy(ScrollPaneConstants.VERTICAL_SCROLLBAR_ALWAYS);
        window.add(scroll);

        labNumberText = new JLabel("ORF number:");
        window.add(labNumberText);

        numberORF = new JTextField(5);
        window.add(numberORF);

        blastORF = new JButton("BLAST ORF");
        window.add(blastORF);
        blastORF.addActionListener(this);

        blastText = new JTextArea(10, 60);
        blastText.setEditable(false);
        scroll = new JScrollPane(blastText);
        scroll.setVerticalScrollBarPolicy(ScrollPaneConstants.VERTICAL_SCROLLBAR_ALWAYS);
        window.add(scroll);
    }

    public boolean validDNA(String seq) {
        //Check for validity of sequence string
        return (sequence.matches("[ATGC]+")|| sequence.matches("[atgc]+"));
    }

    public void addORF(ORF orf) {
        //Adds an ORF to the ArrayList
        orfs.add(orf);
    }

    public void addBLAST(BLAST blast) {
        //Adds a BLAST result to the ArrayList
        blasts.add(blast);
    }


    public void readFile() {
        try {
            inFile = new BufferedReader(new FileReader(fileText.getText()));
            sequenceText.setText(null);
            orfText.setText(null);
            blastText.setText(null);
            String line;
            while ((line = inFile.readLine()) != null) {
                if (!line.startsWith(">")) {
                    sequenceText.append(line + "\n");
                    sequence += line;
                }
            }
            inFile.close();
        } catch (IOException e) {
            JOptionPane.showMessageDialog(null,
                    "File Error: " + e.toString());
        }
    }

    public void actionPerformed(ActionEvent event) {
        File selectedFile;
        int reply;
        if (event.getSource() == openFileButton) {
            sequence = "";
            fileChooser = new JFileChooser();
            reply = fileChooser.showOpenDialog(this);
            if (reply == JFileChooser.APPROVE_OPTION) {
                selectedFile = fileChooser.getSelectedFile();
                fileText.setText(selectedFile.getAbsolutePath());
                readFile();
            }
            if (!validDNA(sequence)) {
                sequenceText.setText(null);
                sequenceText.append(" File does not contain valid DNA sequence");
            }
        }

        if (event.getSource() == predictORF) {
            //Reset text area
            orfText.setText(null);
            blastText.setText(null);
            //Add all ORFs to text area
            for (ORF o : orfs) {
                orfText.append("number: " + o.getNumber());
                orfText.append("   start: " + o.getStartPosition());
                orfText.append("   stop: " + o.getStopPosition());
                orfText.append("   length: " + o.getLength());
                orfText.append("   frame: " + o.getFrame());
                orfText.append("   strand: " + o.getStrand() + "\n");
                orfText.append("sequence: " + o.getSequence() + "\n");
                orfText.append("\n");
            }
        }

        if (event.getSource() == blastORF) {
            //Reset text area
            blastText.setText(null);
            //Loop ArrayList
            for (ORF o : orfs) {
                //Selected ORF number
                if (o.getNumber() == Integer.parseInt(numberORF.getText())) {
                    //Add all BLAST results to text area
                    for (BLAST b : blasts) {
                        blastText.append("blast ID: " + b.getBlastId());
                        blastText.append("   accession code: " + b.getAccessionCode());
                        blastText.append("   percentage identity: " + b.getPercIdentity());
                        blastText.append("   e value: " + b.geteValue());
                        blastText.append("   coverage: " + b.getCoverage());
                        blastText.append("\n");
                    }
                }
            }
        }
    }
}
