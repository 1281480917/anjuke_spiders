import csv
csvwriter = csv.writer(open('anju.csv', 'w'), delimiter=',')
csvwriter.writerow(['community','average_price'])