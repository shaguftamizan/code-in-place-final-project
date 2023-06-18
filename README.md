# WordIt - The Keeper of Words

---

## Overview

This is a simple, personal vocabulary/glossary dictionary model
that allows users to input words and their meanings to build
a digital vocabulary notebook. As a user, you can complete
the following actions - 

1. Add words into the dictionary
2. Remove words from the dictionary
3. Search words in the dictionary

## Disclaimer

Please bear in mind that the raw version of the program does not record the entries
in a separate file. This means, everytime you re-run the program, any previous
entries made whatsoever will be removed. Therefore, the program always starts with
an empty dictionary. To circumvent this issue, I created a JSON file to store
the entries while the script is running. So the JSON file is basically keeping a 
tab on all user entries. The JSON package was used to define two functions in order
to write the entries to the file as well as to load them in the dictionary variable
everytime the script is run. The JSON file must be built within the same directory
your script is in.

---
