#add modules
import os
import csv

#input paths
csvpath=os.path.join('Resources','election_data.csv')

#create lists to store data
ballot_id =[]
county =[]
candidate =[]

#read csvfile
with open(csvpath) as csvfile:
    csv_reader=csv.reader(csvfile, delimiter=',')

    #skip header
    csv_header=next(csv_reader)
    
    for row in csv_reader:
    # add ballot_id
        ballot_id.append(row[0])
    # add county
        county.append(row[1])
    #add candidate
        candidate.append(row[2])

#calculate total number of votes case
total_votes = int(len(ballot_id))
print(f"Total Votes: {total_votes}")


output_path=os.path.join('Analysis', 'election_analysis.txt')
with open(output_path,'w') as csvfile2:
    csvwriter=csv.writer(csvfile2,delimiter=',')
    #create header for textfile
    csv_header2= ""
    # write into the txtfile
    csvwriter.writerow(['Election Results'])
    csvwriter.writerow([f'Total votes: {total_votes}'])
    csvwriter.writerow([f'Charles Casper Stockham:'])
    csvwriter.writerow([f'Diana DeGette:' ])
    csvwriter.writerow([f'Raymon Anthony Doane:' ])
    csvwriter.writerow([f'Winner:' ])

