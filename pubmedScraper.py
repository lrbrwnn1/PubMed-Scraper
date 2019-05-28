from Bio import Entrez
from Bio import Medline

#list of all keywords that can be used to retrieve info from the medline db
# Includes 
#https://biopython-tutorial.readthedocs.io/en/latest/notebooks/09%20-%20Accessing%20NCBIs%20Entrez%20databases.html

def fetch_details(id_list):
    try:
        ids = ','.join(id_list)#Combines id's from id_list
        Entrez.email = 'lrbrwnn1@memphis.edu'
        handle = Entrez.efetch(db="pubmed", id=ids, rettype="medline", retmode="text")
        records = Medline.parse(handle)

        return records
    except:
        pass

#for each author tag (1 per line):
  #1 - Go through the list of pmid's and get info on each
  #2 - Append author_tag
  #3 - Write to file
if __name__ == '__main__':  
  count = 0 
  f = open('pubs.txt', 'a+')
  with open('author2citation.txt') as a:
    for line in a:
      investigator_tag = (line.split('\t')[0])
      pmidList = (line.split('\t')[1]).rstrip()
      pmidList = pmidList.split(',')
      print(investigator_tag, pmidList)
      papers = fetch_details(pmidList)
      for paper in papers:
        count+=1
        f.write(paper.get("PMID", "?")+"\t")
        f.write(paper.get("TI", "?")+"\t")
        f.write(str(paper.get("AU", "?"))+"\t")
        f.write(paper.get("AB", "?")+"\t")
        f.write(paper.get("SO", "?")+"\t")
        f.write(paper.get("DP", "?")+"\t")
        f.write(str(paper.get("MH", "?"))+"\t")
        f.write(investigator_tag+"\n")





