# Bad C2
## General 
Name: `Bad C2`
Description: `Not very versatile malware`
Hint: `Did you say please?`
Flag: `RS{m4gic_word_is_4lw4ys_b31ng_p0lit3}`
Category: `Forensics`

## How to solve 
When we look at the PCAP we see just under 100 rows of web data. As we dig into the streams, it's apparent we're looking at traffic to some domain `maliciouspayload[.]delivery`. There are a few different web endpoints getting hit in this capture, including `/communicate/global`, `get/command`, `get/secret`, and several others. Most of these are just `GET` requests that display some data. Based on the context this traffic might be coming from some type of malware implant, that looks to be interacting with the server in various ways. There is only one `POST` request, and that is to the endpoint `get/secret`. This is the only web request that matters for solving the challenge.

A close look at the HTTP stream for the `POST /get/secret` shows the following:
```
POST /get/secret HTTP/1.1
Host: maliciouspayload.delivery
User-Agent: python-requests/2.21.0
Accept-Encoding: gzip, deflate
Accept: */*
Connection: keep-alive
Content-Length: 19
Content-Type: application/json
{"please": "false"}

HTTP/1.1 200 OK
Server: Werkzeug/2.1.0 Python/3.8.10
Date: Tue, 29 Mar 2022 23:52:27 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 28

sorry, you didn't say please
```

We can see the POST data is very simple, only: `{"please": "false"}`. The response was a 200, but the message indicates that something was not as expected since we didn't "say please". At this point one might infer that setting `{"please": "true"}` as the post data to this endpoint might result in something interesting. 

Using something like python requests (example attached), one should send the `{"please": "true"}` payload to `http://maliciouspayload[.]delivery/get/secret` - they will recieve the response containing the flag: `RS{m4gic_word_is_4lw4ys_b31ng_p0lit3}`.