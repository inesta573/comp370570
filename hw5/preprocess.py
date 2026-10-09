#!/usr/bin/env python3
"""Pre-compute monthly average response time (hours) per zipcode for the Bokeh dashboard.

Usage: python3 preprocess.py <2024 csv> bokeh_dashboard/monthly_response.csv
"""
import csv
import sys
from collections import defaultdict
from datetime import datetime

DATE_FMT = "%m/%d/%Y %I:%M:%S %p"


def main(in_path, out_path):
    sums = defaultdict(float)
    counts = defaultdict(int)

    with open(in_path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            zipcode = (row.get("Incident Zip") or "").strip()[:5]
            if not (len(zipcode) == 5 and zipcode.isdigit()):
                continue                                  # drop missing zips
            try:
                created = datetime.strptime(row["Created Date"], DATE_FMT)
                closed = datetime.strptime(row["Closed Date"], DATE_FMT)
            except (ValueError, KeyError, TypeError):
                continue                                  # not closed -> drop
            if created.year != 2024 or closed.year != 2024:
                continue                                  # opened in 2024
            hours = (closed - created).total_seconds() / 3600
            if hours < 0:
                continue                                  # negative -> drop
            month = closed.month                          # month it was closed
            for key in ((zipcode, month), ("ALL", month)):
                sums[key] += hours
                counts[key] += 1

    with open(out_path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["zipcode", "month", "avg_hours", "n"])
        for (z, m) in sorted(counts):
            w.writerow([z, m, round(sums[(z, m)] / counts[(z, m)], 3), counts[(z, m)]])


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
