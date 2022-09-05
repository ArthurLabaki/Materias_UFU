#!/usr/bin/env bash

arquivo="$1"

while read cidade; do
  echo "$cidade"
  nmap -O -p 0-65535 -v "$cidade" >> "$cidade".txt
done < "$arquivo"
# -sS -sU -Pn demoram muito
