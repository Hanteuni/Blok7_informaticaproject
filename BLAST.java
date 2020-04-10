public class BLAST {

    private int blastId;
    private String accessionCode;
    private int percIdentity;
    private int eValue;
    private int coverage;

    public BLAST(int blastId, String accessionCode, int percIdentity, int eValue, int coverage) {
        setBlastId(blastId);
        setAccessionCode(accessionCode);
        setPercIdentity(percIdentity);
        seteValue(eValue);
        setCoverage(coverage);
    }

    public int getBlastId() {
        return blastId;
    }

    public void setBlastId(int blastId) {
        this.blastId = blastId;
    }

    public String getAccessionCode() {
        return accessionCode;
    }

    public void setAccessionCode(String accessionCode) {
        this.accessionCode = accessionCode;
    }

    public int getPercIdentity() {
        return percIdentity;
    }

    public void setPercIdentity(int percIdentity) {
        this.percIdentity = percIdentity;
    }

    public int geteValue() {
        return eValue;
    }

    public void seteValue(int eValue) {
        this.eValue = eValue;
    }

    public int getCoverage() {
        return coverage;
    }

    public void setCoverage(int coverage) {
        this.coverage = coverage;
    }
}
