#!/usr/bin/env python
import re
import argparse
def get_args():
    parser = argparse.ArgumentParser(description='Input K-mer Size and File name.')
    parser.add_argument('-f', '--file', type=str,help='File Name to be evaluated',required=True)
    return parser.parse_args()
args= get_args()
f = args.file
def contigs(f):
    kmer_lengths=[]
    kmer_coverage=[]
    with open (f,"r") as s:
        for line in s:
            if '>' in line:
                q= re.findall('\d+_c',line)
                #pulls out kmer length
                r= re.findall('[0-9]+\.[0-9]+',line)
                #pulls out coverage
                for i in q:
                    q= i.strip('_c')
                    s = int (q)
                    #removes _c, converts to an int
                for i in r:
                    r = float(i)
                    #converts r to a float
                kmer_lengths.append(s)
                kmer_coverage.append(r)
        i=0
        phyLen=[]
        for item in kmer_lengths:
            #loop to create an array called phyLen that contains the physical lengths
            x = kmer_lengths[i]+49-1
            #adjusts the kmer lengths to be physical lengths based on kcnt=str(len)-k+1
            phyLen.append(x)
            i+=1
        phyLens=sorted(phyLen, reverse=True)
        nContigs=len(phyLens)
        maxContig=max(phyLens)
        meanContig=(sum(phyLens)/nContigs)
        assemblyLen=sum(phyLens)
        i=0
        coverage=[]
        for item in kmer_lengths:
            #loop to convert kmer coverage to physical coverage based on Ck =C*(L-K+1)/L
            x=(kmer_coverage[i]*phyLen[i])/(phyLen[i]-48)
            coverage.append(x)
            i+=1
        meanDepth= sum(coverage)/len(coverage)
        i=0
        summ=0
        while summ <= (assemblyLen/2):
            #iterates over contig lengths and adds them until the number exceeds half the assembly length
            summ+= phyLens[i]
            i+=1
        n50=phyLens[(i-1)]
        #the value where half of the genome is covered by nContigs
        bins={}
        for item in phyLens:
            #creates bins of 100bp for each item in phyLens and increments the key with each occurance
            x=item//100
            x=x*100
            if x in bins:
                bins[x]+=1
            else:
                upd={x:1}
                bins.update(upd)
        print('#'+'\t'+'Contig Length'+'\t'+'Number of Contigs in this Category')
        for item in bins:
            print(str(item)+'\t'+str(bins[item]))

        print("assembly Length",assemblyLen)
        print("Mean Contig",meanContig)
        print("max Contig",maxContig)
        print("Number of Contigs",nContigs)
        print("Mean Depth",meanDepth)
        print("N50",n50)
contigs(f)
