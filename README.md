# stthaddeus-contributions
Contains anonomized contribution information

Inside the anon directory is the file merge_files.txt
   this file contains the linux commands to merge the various anon-pledge-gift-all-20xx.csv files into one big file:
   anon-pledge-gift-all-2009-2019.csv 
 
Use that file to bring into a database and run queries on.
   
The process_giving.py script process the downloaded from ACS csv files and anonomizes them.

Future work:
Process the all-gift-detail-listing-XX.csv so it and the pledge gift one can be matched up so we can get more
granular information (weekly / monthly / quarterly )

Create a sqlite database and a set of queries to generate the reports needed

Create a report document (latex template?) to generate the contribution information needed for the stewardship committee.
