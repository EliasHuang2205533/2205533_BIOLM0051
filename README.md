This project aims to identify the species origin of four unknown meat samples (A–D) using a DNA-based bioinformatics workflow. The analysis includes several steps:

preprocessing and cleaning the raw FASTQ files

assembling the sample nucleotide sequences

running BLAST searches to find close reference genomes

downloading mitochondrial reference sequences

translating nucleotide data into amino acids

generating multiple sequence alignments (MSAs)

constructing neighbour-joining phylogenetic trees

Repository Structure

The repository is organised into three main folders:

bash/
biopython/
Results/


A short explanation of each directory is given below.

1. bash/ — Data Cleaning & FASTA Extraction

This folder contains all preprocessing steps performed on the raw FASTQ files.

FASTQ/

Stores the original FASTQ files for Samples A–D, including multi-part files (e.g., sampleA_part1.fastq, sampleA_part2.fastq).

script/

Bash scripts used for:

fixing formatting issues in FASTQ files

removing duplicated headers or empty lines

merging multi-part FASTQ files

converting FASTQ → FASTA

Most preprocessing steps were run on the BluePebble HPC cluster (accessed through MobaXterm).

results/

Contains the cleaned FASTA files for each sample:

sampleA.fasta

sampleB.fasta

sampleC.fasta

sampleD.fasta

2. biopython/ — Translation, Reference Handling & Data Processing

ref_fasta_new/ref/

Reference sequences selected for each sample.
Each file contains four mitochondrial reference genomes:

sampleA_ref.fasta

sampleB_ref.fasta

sampleC_ref.fasta

sampleD_ref.fasta

Sample_fasta/

Copies of the sample FASTA files (A–D), kept here for convenience so that the Python scripts run without cross-folder paths.

translate_result/

Outputs generated after translation and cleaning:

aa.fasta — amino-acid dataset

nt.fasta — nucleotide dataset

These files were produced using the translation script with vertebrate mitochondrial genetic code (table 2).

translate.py

Main Python script used to:

read and clean FASTA sequences

trim incomplete codons

translate nt → aa

save the processed datasets for MSA and phylogeny

3. Results/ — BLAST, MSA, and Phylogenetic Trees

This folder contains the final outputs used in the report.

BLAST/

Screenshots (PNG/PDF) of the BLASTn results for Samples A–D, including:

query coverage

percent identity

E-values

species names of the top hits

These BLAST results were used to select appropriate reference sequences.

MSA/

Contains:

aa-p1m.fa — amino-acid MSA

nt-p1m.fa — nucleotide MSA

aa_msa.jpg — visual overview of the AA alignment

phylogenetic tree/

This directory is divided into two parts:

A. EBI Simple Phylogeny/

Tree outputs generated using the EMBL-EBI tool:

aa_EBI_SIMPLE_PHYLOGENY.png / .svg

nt_EBI_SIMPLE_PHYLOGENY.png / .svg

The SVG files can be viewed in a browser. These trees show the contrast between the unstable AA topology and the more coherent NT clustering.

B. MEGA/

Neighbour-joining trees constructed using MEGA 12 with:

pairwise deletion

100 bootstrap replicates

Files include:

aa_meg.png — AA tree

nt_meg.png — NT tree

aa-p1m.mtsx — MEGA session file for AA

nt-p1m.mtsx — MEGA session file for NT

These trees were used to compare the behaviour of protein- vs DNA-based phylogenies.