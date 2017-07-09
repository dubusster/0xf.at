#!/usr/bin/bash
echo $1 > 20.hash
optirun hashcat -a 1 -m 0 20.hash wordlist.txt wordlist.txt --show
