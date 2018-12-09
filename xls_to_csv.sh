#!/bin/sh

### Perform xls to csv conversion

# Each xls has 7 sheets, each sheet will generate a separate csv numbered 0-6
for file in data/xls/*.xls; do
    base=${file##*/}
    name="${base%.xls}.csv"
    ssconvert -S "$file" "data/csv/$name"
done

### Files have two header rows, the second row is more granular so delete the first for the files we use

# Ranked Measure Data Sheet
for file in data/csv/*.csv.3; do
    sed -i '1d' $file
done

# Additional Measure Data Sheet
for file in data/csv/*.csv.4; do
    sed -i '1d' $file
done
