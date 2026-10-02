### How big is the dataset?

```
ls -lh clean_dialog.csv
wc -l clean_dialog.csv
csvtool width clean_dialog.csv
```

The file is 4.7 MB with 36,860 lines (1 header + 36,859 dialog lines) and 4 columns.

### What's the structure of the data?

```
head -5 clean_dialog.csv
csvtool col 3 clean_dialog.csv | sort | uniq -c | sort -rn | head
```

There are four fields: title (episode name), writer (episode writer), pony (the character speaking), and dialog (the line spoken). Each row is one line of dialog.

### How many episodes does it cover?

```
csvtool col 1 clean_dialog.csv | tail -n +2 | sort -u | wc -l
```

197 titles. This includes the movie and specials, and two-part episodes are counted separately.

### Unexpected aspect

```
grep -o '","[^"]*Twilight[^"]*","' clean_dialog.csv | sort | uniq -c | sort -rn
grep -c ',NA' clean_dialog.csv
```

The pony field doesn't always contain a single character. Some lines are attributed to groups ("Twilight Sparkle and Spike") or variants ("Young Twilight Sparkle"), so a simple grep for a name overcounts. Character names also appear inside the dialog itself. Also, 21 rows have NA instead of dialog.

## Task 4

```
grep -c '","Twilight Sparkle","' clean_dialog.csv
grep -c '","Rarity","' clean_dialog.csv
grep -c '","Pinkie Pie","' clean_dialog.csv
grep -c '","Rainbow Dash","' clean_dialog.csv
grep -c '","Fluttershy","' clean_dialog.csv
tail -n +2 clean_dialog.csv | wc -l
```

I matched on the pony field exactly so that lines where the name is mentioned in dialog, or where the pony speaks as part of a group, are not counted. Percentages are out of all 36,859 lines.

Twilight Sparkle: 4745 lines, 12.87%

Rarity: 2660 lines, 7.22%

Pinkie Pie: 2833 lines, 7.69%

Rainbow Dash: 3072 lines, 8.33%

Fluttershy: 2109 lines, 5.72%

To make line_percentages.csv:

```
total=$(tail -n +2 clean_dialog.csv | wc -l)
echo "pony_name,total_line_count,percent_all_lines" > line_percentages.csv
for p in "Twilight Sparkle" "Rarity" "Pinkie Pie" "Rainbow Dash" "Fluttershy"; do
  n=$(grep -c "\",\"$p\",\"" clean_dialog.csv)
  pct=$(awk -v n="$n" -v t="$total" 'BEGIN { printf "%.2f", n * 100 / t }')
  echo "$p,$n,$pct" >> line_percentages.csv
done
```

