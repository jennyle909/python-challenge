#add modules
import os
import csv

#input paths
csvpath=os.path.join('Resources','budget_data.csv')

#create lists to store data
date =[]
pro_loss =[]

#read csvfile
with open(csvpath) as csvfile:
    csv_reader=csv.reader(csvfile, delimiter=',')

    #skip header
    csv_header=next(csv_reader)
    
    for row in csv_reader:
    # add date
        date.append(row[0])
    # add pro_loss
        pro_loss.append(row[1])

#calculate total months then change to integer
total_month = int(len(date))
print(f"Total Months: {total_month}")

#convert pro_loss to integers
pro_loss=[int(num) for num in pro_loss]

#calculate net change
net_change =sum(pro_loss)
print(f"Total:${net_change}")

#calculate average change
ave_change =(net_change/total_month)
print(f"Average Change: ${ave_change:.2f}")

output_path=os.path.join('Analysis', 'fin_analysis.txt')
with open(output_path,'w') as csvfile2:
    csvwriter=csv.writer(csvfile2,delimiter=',')
    #create header for textfile
    csv_header2= ""
    # write into the txtfile
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow([f'Total Months: {total_month}'])
    csvwriter.writerow([f'Average Change: ${ave_change:.2f}'])
    csvwriter.writerow(['Greatest Increase in Profit:$' ])
    csvwriter.writerow(['Greatest Decrease in Profit:$' ])
