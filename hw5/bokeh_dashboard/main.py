"""Bokeh dashboard: monthly average 311 response time, all NYC vs. two chosen zipcodes.

Run from the hw5 folder:  bokeh serve bokeh_dashboard
"""
import csv
import os
from collections import defaultdict

from bokeh.io import curdoc
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, Select
from bokeh.plotting import figure

DATA = os.path.join(os.path.dirname(__file__), "monthly_response.csv")
MONTHS = list(range(1, 13))

avg = defaultdict(dict)
with open(DATA, newline="") as f:
    for r in csv.DictReader(f):
        avg[r["zipcode"]][int(r["month"])] = float(r["avg_hours"])

zips = sorted(z for z in avg if z != "ALL")


def series(z):
    return [avg[z].get(m, float("nan")) for m in MONTHS]


src_all = ColumnDataSource(dict(x=MONTHS, y=series("ALL")))
src_z1 = ColumnDataSource(dict(x=MONTHS, y=series(zips[0])))
src_z2 = ColumnDataSource(dict(x=MONTHS, y=series(zips[1])))

select1 = Select(title="Zipcode 1", value=zips[0], options=zips)
select2 = Select(title="Zipcode 2", value=zips[1], options=zips)

p = figure(title="Monthly average 311 response time, 2024",
           x_axis_label="Month (2024, by closed date)",
           y_axis_label="Average create-to-closed time (hours)",
           width=800, height=400)
p.xaxis.ticker = MONTHS
p.line("x", "y", source=src_all, line_width=2, color="gray", legend_label="All NYC")
p.line("x", "y", source=src_z1, line_width=2, color="steelblue", legend_label="Zipcode 1")
p.line("x", "y", source=src_z2, line_width=2, color="darkorange", legend_label="Zipcode 2")
p.legend.location = "top_left"


def update(attr, old, new):
    src_z1.data = dict(x=MONTHS, y=series(select1.value))
    src_z2.data = dict(x=MONTHS, y=series(select2.value))


select1.on_change("value", update)
select2.on_change("value", update)

curdoc().add_root(column(select1, select2, p))
curdoc().title = "311 Response Time by Zipcode"
