import os 
import argparse

def Split_fasta(fasta_file,output_folder):
    name=list()
    fasta=open(fasta_file,"rt")
    lines=fasta.readlines()
    fasta.close()
    for line in lines:
        if line.startswith(">"):
            name.append(line[1:-1])
    for i in range(len(name)):
        name[i]= name[i].replace("/","_")
    fasta=open(fasta_file,"rt")
    lines=fasta.read()
    split=lines.split(">")
    fasta.close()
    for i, j in zip(range(len(split)-1), range(len(name))):
        fout=open(output_folder + name[j]+".fasta","wt")
        fout.write(">"+split[i+1])
        fout.close()

parser=argparse.ArgumentParser(
    prog="python Split_fasta.py",
    formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument("-i","--input",help="The path of a fasta file for split")
parser.add_argument("-o","--output", help="The path of your output folder")
args=parser.parse_args()

if __name__=="__main__":
    fasta_file=args.input
    output_folder=args.output
    Split_fasta(fasta_file,output_folder)