import csv
import xlsxwriter


def save_to_file(jobs):
    file = open("python.csv", encoding="utf-8-sig", mode="w", newline="")
    writer = csv.writer(file)
    writer.writerow(["title", "company", "location", "link"])
    for job in jobs:
        writer.writerow(list(job.values()))
    return