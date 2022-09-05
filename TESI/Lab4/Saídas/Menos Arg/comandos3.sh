#!/usr/bin/env bash

arquivo="$1"

while read cidade; do
  echo "$cidade"
  nmap "$cidade" >> "$cidade".txt
done < "$arquivo"
# -sS -sU -Pn demoram muito
