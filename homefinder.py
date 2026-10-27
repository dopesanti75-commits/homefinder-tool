import csv
import zipfile

with open("homefinder_listings.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Address", "Price", "Listing URL"])

with zipfile.ZipFile("homefinder_listings.zip", "w") as z:
    z.write("homefinder_listings.csv")

print("CSV and ZIP files created.")
