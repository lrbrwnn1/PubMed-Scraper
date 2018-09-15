from Bio import Entrez
from Bio import Medline

#TEXT BASED PUBMED SCRAPER
def fetch_details(id_list):
    try:
        ids = ','.join(id_list)#Combines id's from id_list
        Entrez.email = 'xxxx@xxxx.com' #enter your own email address here
        handle = Entrez.efetch(db="pubmed", id=ids, rettype="medline", retmode="text") 
        records = Medline.parse(handle)
        return records
    except: #If the script encounters an error it will ignore it and keep going. This is a workaround for a small number of very old publications that don't seem to play nice with the API
        pass

if __name__ == '__main__': #main function
	#The list of PMID's we want info from. Bio.Entrez has various search methods to get a list of PMIDs if you don't already have the PMID's you need.
    id_list = ['10028039', '10081590']#sample PMIDs
    papers = fetch_details(id_list) #calls the detch_details method above, passes id_list as its argument
    f = open('pubs.txt', 'a+') #creates a text file called pubs.txt in current directory - results are stored here.
    for paper in papers:
    	f.write("PMID:"+ paper.get("PMID", "?")+"\n")
    	f.write("Title:"+ paper.get("TI", "?")+"\n")
    	f.write("Authors:"+ str(paper.get("AU", "?"))+"\n")
    	f.write("Affiliation:"+ paper.get("AD", "?")+"\n")
    	f.write("Abstract:"+ paper.get("AB", "?")+"\n")
    	f.write("Source:"+ paper.get("SO", "?")+"\n")
    	f.write("Data Published:"+ paper.get("DP", "?")+"\n")
    	f.write("Mesh Headings:"+ str(paper.get("MH", "?"))+"\n\n\r")





