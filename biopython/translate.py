from pathlib import Path
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

"""
PART 1 — Define all input and output paths
1. Defines the directories that contain reference FASTA files and sample FASTA files
2. Defines the output directory where merged nucleotide and translated amino-acid FASTA files will be written
3. Ensures the output directory exists to prevent write errors
"""

# Paths for reference, sample and output
ref_dir = Path(r"E:\2205533_BIOLM0051\biopython\ref_fasta_new\ref")
sample_dir = Path(r"E:\2205533_BIOLM0051\biopython\Sample_fasta")
output_dir = Path(r"E:\2205533_BIOLM0051\biopython\translate_result")

# Output FASTA files
output_nt = output_dir / "nt.fasta"   # merged nucleotide sequences
output_aa = output_dir / "aa.fasta"   # translated amino-acid sequences


"""
PART 2 — Merge reference + sample FASTA into a single nt.fasta
1. Loads all reference and sample nucleotide sequences.
2. Standardises sequence IDs to ensure clean headers for MSA
   and phylogenetic tree programs.
3. Writes all nucleotide sequences to nt.fasta.
"""

# List container for all nucleotide SeqRecords
all_records = []


# Read reference FASTA files
for f in ref_dir.glob("*.fasta"):
    for rec in SeqIO.parse(f, "fasta"):

        # Split the original FASTA header into tokens
        header = rec.description.split()

        # The first token is always the accession number
        accession = header[0]

        # The next two tokens is scientific name
        species = "_".join(header[1:3])  # Replace space with underscore

        # Construct sequence ID:
        rec.id = f"{accession}_{species}"

        rec.name = rec.id      # Update the `name` field for consistency
        rec.description = ""   # Remove long descriptions to keep FASTA headers tidy

        # Store the processed reference sequence
        all_records.append(rec)



# Read sample FASTA files
for f in sample_dir.glob("*.fasta"):
    for rec in SeqIO.parse(f, "fasta"):
        rec.id = f.stem                       # Use the filename (e.g., sampleA) as sequence ID
        rec.description = ""                  # Remove descriptions for consistency
        all_records.append(rec)


# Write merged nucleotide FASTA
SeqIO.write(all_records, output_nt, "fasta")
print("Wrote nt.fasta with", len(all_records), "records.")



"""
PART 3 — Translate nucleotide sequences into amino acids
1. Loads nt.fasta.
2. Trims sequences so their length is divisible by 3 when required
3. Translates them using the vertebrate mitochondrial code (table 2)
4. Writes translated protein sequences to aa.fasta
"""


# Parameter explanations:
# nt_fasta:      path to the merged nucleotide FASTA file (input)
# aa_fasta:      path to the translated amino-acid FASTA file (output)
# genetic_code:  translation table number (2 = vertebrate mitochondrial)
# keep_full_codons: if True, trims sequence length to a multiple of 3 (to prevent translation issues)

def convert_nt_to_aa(nt_fasta: str,
                     aa_fasta: str,
                     genetic_code: int = 2,
                     keep_full_codons: bool = True):
    """Translate nucleotide sequences to amino acids and write to aa_fasta."""

    aa_records = []


    # Read nucleotide sequences
    for record in SeqIO.parse(nt_fasta, "fasta"):
        seq_nt = record.seq.upper()  # Convert to uppercase for consistent translation

        # Trim trailing nucleotides if not divisible by 3
        if keep_full_codons:
            seq_nt = seq_nt[: len(seq_nt) - (len(seq_nt) % 3)]

        # Perform translation (do not stop at first STOP codon)
        seq_aa = seq_nt.translate(table=genetic_code, to_stop=False)

        # Store the translated protein as a SeqRecord
        aa_records.append(
            SeqRecord(
                seq_aa,
                id=record.id,
                description=f"translated (table {genetic_code})"
            )
        )

    # Write amino-acid FASTA output
    SeqIO.write(aa_records, aa_fasta, "fasta")
    print("Protein sequences written to:", aa_fasta)


"""
PART 4 — Run the translation function and execute Part 3
"""
convert_nt_to_aa(output_nt, output_aa)








