#!/bin/bash

#Name of the output fasta file
output="sampleD.fasta"

#Remove old output file if it exists
rm -f "$output"

#Extract the second line (sequence) of every four lines in the FASTQ file and write it to the output file

for file in sampleD_part1.FASTQ sampleD_part2.FASTQ sampleD_part3.FASTQ
do
    awk 'NR % 4 == 2' "$file" >> "$output"
done

#Use `grep -v '^>'` to ensure no data corruption
#Remove newline characters to concatenate sequences
sequence=$(grep -v '^>' "$output" | tr -d '\n')

#Built the final fasta
echo ">sampleD" > "$output"    #Add new header line
echo "$sequence" >> "$output"  #Append the full sampleA sequence