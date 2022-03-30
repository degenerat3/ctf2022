# Cyber Survey

## General 
Name: `Cyber Survey`
Description: `Lookin' like a Fujitsu FI-6800`
Hint: `Drop the 40's like it's hot, what do you see`
Flag: `RS{sc4ns_bett3r_than_4n_hp_d3skjet3755}` 

## How to solve 
This PCAP captured a network scan from `192.168.50.172` to `192.168.50.128`. It enumerated a lot of ports. Most of the ports that were scanned were closed and resulted in a `[RST, ACK]` being sent back. Some of them, however, were open. These ports replied and continued with full handshake, allowed the string `garbage` to be transmitted. If we look at the dst ports being scanned, it's not like a normal scan that's hitting service ports (ssh, web, rdp, etc) - these are all in the `40000` range. The dst ports will be the key to getting the flag.

To limit the data set we can ignore all the connections that got rst. That cuts us down to 39 connections. If we look at all those dest ports that were successfully connected to, we get 
```[40082, 40083, 40123, 40115, 40095...]``` 

If you're familiar with ascii codes you'll recognize that if you ignore the `40` prefix for all of these, they relate to ascii chars in the alphanumeric (plus a couple symbols) set. In fact as a quick sanity check, the `82`, `83`, and `123` align with `RS{`, which we know is the start of the flag format.

It would be painful to check all the accepted ports manually (although possible, since it's only 39), but there's a script attached that will serve to do the work. The script will look at the packets with `PUSH` flags, since we know that means they were successfull and actually sent some data. You could also look at the packets with the `fin` flag, since that's a graceful close of the connection which implies there was some data sent (or at least a handshake successfully established). The script iterates through all the packets and collects all the ports that we successfully connected to (`[40082, 40083, 40123, 40115, 40095...]`), then trims off the useless `40` prefix and gets the ascii char value for each number, giving us the flag `RS{sc4ns_bett3r_than_4n_hp_d3skjet3755}`