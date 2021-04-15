#!/bin/bash

echo "
 ' /$$$$$ /$$$$$$ /$$    /$$  /$$$$$$ 
   |__  $$|_  $$_/| $$   | $$ /$$__  $$
      | $$  | $$  | $$   | $$| $$  \ $$
      | $$  | $$  |  $$ / $$/| $$$$$$$$
 /$$  | $$  | $$   \  $$ $$/ | $$__  $$
| $$  | $$  | $$    \  $$$/  | $$  | $$
|  $$$$$$/ /$$$$$$   \  $/   | $$  | $$
 \______/ |______/    \_/    |__/  |__/
 "

echo "
' /$$$$$$$$ /$$   /$$ /$$$$$$$$       /$$$$$$$   /$$$$$$  /$$$$$$$$
|__  $$__/| $$  | $$| $$_____/      | $$__  $$ /$$__  $$|__  $$__/
   | $$   | $$  | $$| $$            | $$  \ $$| $$  \ $$   | $$   
   | $$   | $$$$$$$$| $$$$$         | $$$$$$$ | $$  | $$   | $$   
   | $$   | $$__  $$| $$__/         | $$__  $$| $$  | $$   | $$   
   | $$   | $$  | $$| $$            | $$  \ $$| $$  | $$   | $$   
   | $$   | $$  | $$| $$$$$$$$      | $$$$$$$/|  $$$$$$/   | $$   
   |__/   |__/  |__/|________/      |_______/  \______/    |__/   
                                                                  
"

FILE=/app/.git

if [ -d "$FILE" ] ; then
    echo "$FILE directory exists already."
else
    rm -rf ROBOT
    rm -rf .github
    rm -rf sample_config.py
    git clone https://github.com/turquoise-giggle/JIVA JIVA_tb
    mv JIVA_tb/ROBOT .
    mv JIVA_tb/.github . 
    mv JIVA_tb/.git .
    mv JIVA_tb/sample_config.py .
    python ./.github/update.py
    rm -rf requirements.txt
    mv JIVA_tb/requirements.txt .
    rm -rf cat_tb
fi

FILE=/app/bin/
if [ -d "$FILE" ] ; then
    echo "$FILE directory exists already."
else
    bash ./.github/bins.sh
fi

python -m ROBOT
