public class ORF {

    private int number;
    private int startPosition;
    private int stopPosition;
    private int length;
    private String sequence = "";
    private int frame;
    private int strand;

    public ORF(int number, int startPosition, int stopPosition, int length, String sequence, int frame, int strand) {
        setNumber(number);
        setStartPosition(startPosition);
        setStopPosition(stopPosition);
        setLength(length);
        setSequence(sequence);
        setFrame(frame);
        setStrand(strand);
    }

    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }

    public int getStartPosition() {
        return startPosition;
    }

    public void setStartPosition(int startPosition) {
        this.startPosition = startPosition;
    }

    public int getStopPosition() {
        return stopPosition;
    }

    public void setStopPosition(int stopPosition) {
        this.stopPosition = stopPosition;
    }

    public int getLength() {
        return length;
    }

    public void setLength(int length) {
        this.length = length;
    }

    public String getSequence() {
        return sequence;
    }

    public void setSequence(String sequence) {
        this.sequence = sequence;
    }

    public int getFrame() {
        return frame;
    }

    public void setFrame(int frame) {
        this.frame = frame;
    }

    public int getStrand() {
        return strand;
    }

    public void setStrand(int strand) {
        this.strand = strand;
    }
}
