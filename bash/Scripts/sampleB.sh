#!/bin/bash

#There are 2 header line in sampleB_part1, so delete the first line
sed -i '1d' sampleB_part1.FASTQ

#name of the output fasta file
output="sampleB.fasta"

#Remove old output file if it exists
rm -f "$output"

#Extract the second line (sequence) of every four lines in the FASTQ file and write it to the output file

for file in sampleB_part1.FASTQ sampleB_part2.FASTQ sampleB_part3.FASTQ
do
    awk 'NR % 4 == 2' "$file" >> "$output"
done

#Remove newline characters and concatenate sequences
#Use `grep -v '^>'` to ensure no data corruption
sequence=$(grep -v '^>' "$output" | tr -d '\n')

#build the final fasta
echo ">sampleB" > "$output"  #Add new header line
echo "$sequence" >> "$output"   #Append the full sampleA sequence

#Remove all spaces in the FASTA (if there are any)
sed 's/ //g' sampleB.fasta

