#!/bin/bash

# This script updates the requirements.txt file by commenting out specific package versions
# and appending a custom wheel file reference.
# Usage:
# 1. Ensure the script is executable: chmod +x scripts/update_requirements.sh
# 2. Run the script: ./scripts/update_requirements.sh

# Generate requirements.txt
pip list --format=freeze > requirements.txt

# Use a temporary file to make changes and then overwrite the original if necessary
temp_file="temp_requirements.txt"
cp requirements.txt $temp_file

# Comment out specific lines using the temporary file
sed -i '' 's/^mkl-fft==1.3.8/# &/' $temp_file
sed -i '' 's/^mkl-random==1.2.4/# &/' $temp_file
sed -i '' 's/^mkl-service==2.4.0/# &/' $temp_file
# sed -i '' 's/^mdurl==0.1.2/# &/' $temp_file
# sed -i '' 's/^gmpy2==2.1.2/# &/' $temp_file

# Delete specific lines from the temporary file
sed -i '' '/^rpg_world==1.0.0/d' $temp_file

# Append the custom wheel file reference for mdurl
# echo './wheels/mdurl-0.1.2-py3-none-any.whl' >> $temp_file

# Move the final version back to the original file name
mv $temp_file requirements.txt

echo "Updated requirements.txt successfully."
