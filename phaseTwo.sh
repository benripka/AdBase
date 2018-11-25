#!/bin/bash
# This script will sort the files and load them into new database files

echo "Sorting files"

sort -u pdates.txt | perl break.pl | db_load -c duplicates=1 -T -t btree da.idx 
sort -u terms.txt | perl break.pl | db_load -c duplicates=1 -T -t btree te.idx 
sort -n prices.txt | perl break.pl | db_load -c duplicates=1 -T -t btree pr.idx 
sort -u -n ads.txt | perl break.pl | db_load -c duplicates=1 -T -t hash ads.idx 

# creates index files using supplied script break.pl



