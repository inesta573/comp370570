#!/usr/bin/env python3
"""Count complaint types per borough for a given creation-date range (NYC 311 data)."""
import argparse
import csv
import sys
from collections import Counter
from datetime import datetime

DATE_FMT = "%m/%d/%Y %I:%M:%S %p"   # e.g. 01/15/2024 10:30:00 AM


def parse_args():
    p = argparse.ArgumentParser(
        description="Output the number of each complaint type per borough "
                    "for incidents created within a date range.")
    p.add_argument("-i", "--input", required=True, help="input 311 CSV file")
    p.add_argument("-s", "--start", required=True, help="start date, YYYY-MM-DD (inclusive)")
    p.add_argument("-e", "--end", required=True, help="end date, YYYY-MM-DD (inclusive)")
    p.add_argument("-o", "--output", help="output CSV file (default: stdout)")
    return p.parse_args()


def main():
    args = parse_args()
    start = datetime.strptime(args.start, "%Y-%m-%d").date()
    end = datetime.strptime(args.end, "%Y-%m-%d").date()

    counts = Counter()
    with open(args.input, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                created = datetime.strptime(row["Created Date"], DATE_FMT).date()
            except (ValueError, KeyError, TypeError):
                continue
            if start <= created <= end:
                counts[(row["Complaint Type"], row["Borough"])] += 1

    out = open(args.output, "w", newline="") if args.output else sys.stdout
    writer = csv.writer(out)
    writer.writerow(["complaint type", "borough", "count"])
    for (ctype, borough), n in sorted(counts.items()):
        writer.writerow([ctype, borough, n])
    if args.output:
        out.close()


if __name__ == "__main__":
    main()
