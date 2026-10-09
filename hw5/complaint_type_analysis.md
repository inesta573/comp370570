# Task 3: Complaint Type Analysis

## Method

I used `borough_complaints.py` to count complaints by type and borough for two
periods of 2024, based on each incident's creation date:

```bash
python3 borough_complaints.py -i 311_2024.csv -s 2024-01-01 -e 2024-02-29 -o janfeb.csv
python3 borough_complaints.py -i 311_2024.csv -s 2024-06-01 -e 2024-07-31 -o junjul.csv
```

I then loaded both files in Jupyter (`task3.ipynb`), summed the counts across
boroughs to find the most common complaint type, and plotted that type by
borough.

## Most common complaint type, January–February 2024

**HEAT/HOT WATER** was the most common complaint type in the first two months
of 2024, with **81,641** complaints. It narrowly beat Illegal Parking (79,916),
followed by Noise - Residential (43,602).

| Borough       | Jan–Feb 2024 | Share of total |
|---------------|-------------:|---------------:|
| Bronx         | 30,139       | 36.9%          |
| Brooklyn      | 20,915       | 25.6%          |
| Manhattan     | 17,604       | 21.6%          |
| Queens        | 12,117       | 14.8%          |
| Staten Island | 866          | 1.1%           |
| **Total**     | **81,641**   | **100%**       |

The Bronx accounts for more than a third of all heat and hot water complaints,
even though Brooklyn and Queens both have larger populations. Staten Island,
where more people live in single-family homes, generates very few.

## Comparison with June–July 2024

| Borough       | Jan–Feb 2024 | Jun–Jul 2024 | Change  |
|---------------|-------------:|-------------:|--------:|
| Bronx         | 30,139       | 2,227        | −92.6%  |
| Brooklyn      | 20,915       | 1,929        | −90.8%  |
| Manhattan     | 17,604       | 1,778        | −89.9%  |
| Queens        | 12,117       | 835          | −93.1%  |
| Staten Island | 866          | 121          | −86.0%  |
| **Total**     | **81,641**   | **6,890**    | **−91.6%** |

HEAT/HOT WATER complaints fell by **91.6%** between the two periods, from
81,641 to 6,890, about 12 times fewer. In June–July it is no longer among the
top three complaint types. Illegal Parking (86,240), Noise - Residential
(58,197) and Noise - Street/Sidewalk (47,320) lead instead.

## Interpretation

The pattern is strongly seasonal. NYC landlords must provide heat during the
"heat season" (October 1 to May 31). Most of these winter complaints are about
missing or inadequate heat, and that need disappears in summer. The roughly
6,900 complaints that remain in June–July are probably about hot water, which
landlords must supply all year.

The ranking of boroughs barely changes between the two periods, and the Bronx
leads in both. This suggests that the borough differences reflect the
underlying housing stock, meaning the number of older rental buildings with
central heating systems controlled by landlords, rather than anything specific
to the season. For city leaders, this means heat and hot water enforcement
resources are most needed in the winter months and in the Bronx.
