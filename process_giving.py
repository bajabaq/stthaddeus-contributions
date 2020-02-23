#!/usr/bin/python3

import csv
import hashlib
import os
import sys

def hash_name(name_in):
    
    hashed_name_o = hashlib.md5(name_in.encode())
    hashed_name   = hashed_name_o.hexdigest()
    name          = hashed_name

    if name_in in ["Loose Cash","Mr & Mrs Ervin Swearingen, Jr."]:
        print("Known Val: " + name_in + " " + hashed_name)
    #endif

    
    return(name)
#enddef

def get_ofile(filename):
    ofile = os.path.join("anon","anon-" + filename)
    if os.path.exists(ofile):
        os.remove(ofile)
    #endif              
    return(ofile)
#enddef
              
def main2():
    for filename in os.listdir("."):
        if filename.startswith("all-gift"): 
            print("do stuff with this: " + filename)
            ofile = get_ofile(filename)
            print("to create this: " + ofile)
            with open(ofile, mode='w') as oh:
                oh_writer = csv.writer(oh, delimiter=',',quotechar='"', quoting=csv.QUOTE_ALL)
            
                with open(filename) as fh:
                    csv_reader = csv.DictReader(fh)
                    oh_writer.writerow(["Envelope","Name","PostDate","FullType","FundCode","Description","Amount","Reference","GiftDescription","Value","SName","IndvID"])
                    line_count = 0
                    for row in csv_reader:
                            env   = "REDACTED" #row["Envelope"]
                            name  = row["Name"]
                            name  = hash_name(name)

                            pdate = row["PostDate"]
                            ftype = row["FullType"]
                            fc    = row["FundCode"]
                            desc  = row["Description"]
                            amt   = row["Amount"]
                            ref   = row["Reference"]
                            gd    = row["GiftDescription"]
                            val   = row["Value"]
                            sn    = "REDACTED" #row["SName"]
                            iid   = "REDACTED" #row["IndvID"]
                            
                            oh_writer.writerow([env, name, pdate, ftype, fc, desc, amt, ref, gd, val, sn, iid])

                    #endfor
                #endwith
            #endwith
        #endif
    #endfor
#enddef

#sys.exit()

def get_year(ofile):
    a_ofile = ofile.split('-')
    year    = a_ofile[-1]  #20XX.csv
    year    = year.replace('.csv','')
    return(year)
#enddef

def main():
    for filename in os.listdir("."):
        if filename.startswith("pledge-gift-all"): 
            print("do stuff with this: " + filename)
            ofile = get_ofile(filename)              
            print("to create this: " + ofile)
            with open(ofile, mode='w') as oh:
                oh_writer = csv.writer(oh, delimiter=',',quotechar='"', quoting=csv.QUOTE_ALL)
            
                with open(filename) as fh:
                    csv_reader = csv.DictReader(fh)
                    oh_writer.writerow(["Envelope","Name","FundCode","Description","NonPledgePTD","Pledge","CPledgePTD","OPledgePTD","PrePay","Balance","SName","Year"])                    
                    line_count = 0
                    for row in csv_reader:
                            env   = "REDACTED" #row["Envelope"]
                            name  = row["Name"]
                            name  = hash_name(name)
                            
                            fcode = row["FundCode"]
                            desc  = row["Description"]
                            np    = row["NonPledgePTD"]
                            p     = row["Pledge"]
                            cp    = row["CPledgePTD"]
                            op    = row["OPledgePTD"]
                            pp    = row["PrePay"]
                            bal   = row["Balance"]
                            sn    = "REDACTED" #row["SName"]
                            year  = get_year(ofile)
                            
                            oh_writer.writerow([env, name, fcode, desc, np, p, cp, op, pp, bal, sn, year])

                    #endfor
                #endwith
            #endwith
        #endif
    #endfor
#enddef

if __name__ == "__main__":
    main()  #pledge-gift-all
    main2() #all-gift-detail
#endif
