#!/bin/bash

output="sampleA.fasta" #name of the output fasta file

rm -f "$output"

#Extract the second line of every four lines in the FASTQ file and write it to the output file

for file in sampleA_part1.FASTQ sampleA_part2.FASTQ sampleA_part3.FASTQ
do
    awk 'NR % 4 == 2' "$file" >> "$output"
done

#Remove aLL newline
sequence=$(tr -d '\n' < "$output")

#Remove space (There is space between sampleA_part1 and sampleA_part2) 
sequence=$(echo "$sequence" | tr -d ' ')

#Build the final fasta
echo ">sampleA" > "$output"   #Add new header line
echo "$sequence" >> "$output"   #Append the full sampleA sequence below the header
