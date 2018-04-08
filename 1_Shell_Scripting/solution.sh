# Nick Tallant 
# Intro to Programming
# TA Session 1

# Erases and rewrites the file header.

echo -e "\nNick Tallant: TA Session 01 ANSWERS\n" > ANSWERS.txt

# 1. What must be entered to see the entire first sonnet?
#    Hint - you will need to play around in terminal.

echo "1. 'head -18 sonnets.txt'" >> ANSWERS.txt

# 2. Love is too young to what?
#    Hint - consider the phrase, "Love is too young"

echo "2. `grep "Love is too young" sonnets.txt`" >> ANSWERS.txt

# 3. How many time is love mentioned in the sonnets?

LOVE=$(grep -i love sonnets.txt | wc -l)
echo "3. Love is mentioned $LOVE times." >> ANSWERS.txt

# 4. What code will rename sonnets.txt to poems.txt?

echo "4. 'mv sonnets.txt poems.txt'" >> ANSWERS.txt

# 5. How many sonnets are in the sonnets.txt file? Translating
#    roman numerals is cheating.

#    Hints: ^ is the begins with character for regex
#           $ is the ends with character for regex
#           * denotes 'any number of following characters'
#           ^\s*$ finds all blank lines

ALL=$(grep ^[MDCLXVI]*$ sonnets.txt | wc -l)
BLANK=$(grep ^\s*$ sonnets.txt | wc -l)
echo "5. `expr $ALL - $BLANK` sonnets in the file." >> ANSWERS.txt

