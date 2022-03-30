# Oreo
## General 
Name: `Oreo`
Description: `yum, goes well with milk`
Hint: N/A
Flag: `RS{yumyum_m1lk_4and_co0ki3s_f0r_dayz}`
Category: `Forensics`

## How to solve 
The supplied file `data.tar` is a compressed Google Chrome cache (with some of the garbage folders removed to reduce size). Poking through the various folders and reading file names would point to the fact that it's a web browser cache, and the many references to Google indicate it's likely chromium based. The Name and description for this challenge point strongly to COOKIES. To find the cookies in the Chrome cache, open `data/Default/Cookies`, which is actually a SQLite DB file.

Using a tool like "DB Browser for SQLite", one can browse the `cookies` table in the DB and see 2 interesting rows, 33 and 34. Row 33 is for the host_key `.hacking.cyber` and has the word "flag" obfuscated with periods and commas as the cookie name. The row immediately below it, the only other cookie for the host key `.hacking.cyber`, contains some base64 encoded text - `UlN7eXVteXVtX20xbGtfNGFuZF9jbzBraTNzX2Ywcl9kYXl6fQ==` - decoding this will give the flag: `RS{yumyum_m1lk_4and_co0ki3s_f0r_dayz}`