# ctf2022
stuff for RITSEC ctf 2022

The contents of this zip are as follows:

A folder for each challenge (`badc2`, `cyber_survey`, `leaky_pail`, and `oreo`)

In each folder, there will be a file `info.txt`, a folder `challenge`, and a folder `solution`. `info.txt` specifieds the challenge name, description, hint, etc. It also specifies which file from the challenge folder should be included/excluded. In some cases it also mentions scope, since there are 2 challenges where competitors will have to send a SINGLE request to a domain (no DoS pls, exactly one request is needed to solve the challenge).

The challenge folder contains the file that should be uploaded as part of the challenge, but be warned it ALSO may contain scripts or other files that were used to make the challenge. In both cases where present, these 'non challenge' files are present in a `scripts_that_created_cap` directory. Administrators can look at this, but don't give these files to the competitors. Again, ONLY THE SPECIFIED FILE named in `info.txt` should be included in the challenge. 

The `solution` folder will contain the writeup markdown, as well as any relevant solver script (if applicable). 