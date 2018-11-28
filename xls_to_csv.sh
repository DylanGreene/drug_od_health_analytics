#!/bin/sh

for file in data/xls/*.xls; do
    base=${file##*/}
    name="${base%.xls}.csv"
    ssconvert -S "$file" "data/csv/$name"
done

for file in data/csv/*.csv.4; do
    sed -i '1d' $file
done
