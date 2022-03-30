# Leaky Pail

## General 
Name: `Leaky Pail`
Description: `This one doesn't hold sand or water`
Hint: `Anything interesting in the EC2 creation logs?`
Flag: `RS{a_p0st_p4ram_sux_4_buck3t_secur1ty}` 
Category: `Misc`

## How to solve 
The provided json file is a collection of AWS Cloudtrail logs. The logs are also in reverse chronological order. AWS Cloudtrail tracks all sorts of events that happen in AWS, including EC2 activity (modifcations, new instances, etc), bucket activity, VPC modifications, IAM activity, etc. If it's in AWS, it can probably be tracked in Cloudtrail. This is a very small excerpt of Cloudtrail logs, and some of the sensitive data (keys, account numbers, etc) has been sanitized, but plenty of hints for the challenge are scattered throughout. The first thing you'll see is an event for a bucket creation (`CreateBucket`). The bucket is named `hold-my-secret-stuff-q673c5f6ns`.

Attempting to hit that bucket via an AWS SDK or the web browser will not yield the desired results, as your access will be denied. That's because the next relevant event, a `PutBucketPolicy` event is setting up a deny policy with the following condition:

```
    "Condition": {
        "NotIpAddress": {
            "aws:SourceIp": [
                "REDACTED/32"
            ]
        }
    },
```

This condition will result in all traffic to the bucket being blocked, except for those requests sourced from the specified IP address. Unfortunately that address is redacted, however this plants the idea that we're going to need to somehow get to the whitelisted source (whatever it is) in order to access the bucket.

The next relevant log may be the one you read first, since it contains the string `flag.txt`. While this log does not contain the actual, it is a `PutObject` event showing that the file `flag.txt` was uploaded to the bucket `hold-my-secret-stuff-q673c5f6ns`. Now, if we ever get access to that bucket we know to look at the `flag.txt` object. 

Later in the timeline (further up in the file) we see a `CreateKey` event for the key `prooxy_access`, along with a `RunInstances` event (and several other EC2 events). The `RunInstances` event signifies a user spinning up a new EC2 instance. In this case, this event is _loaded_ with important details for the challenge. As mentioned, we know the key used to SSH/remote into this instance is called `prooxy_access`, which gives a hint about what the instance may be for. There are also two tags associated with this EC2, seen under the `tagSpecificationSet`:
```
                "tagSpecificationSet": {
                    "items": [
                        {
                            "resourceType": "instance",
                            "tags": [
                                {
                                    "key": "application",
                                    "value": "git:yung-g4ngst3r360noscope/prooxy"
                                },
                                {
                                    "key": "magic",
                                    "value": "yldzzf9vi5"
                                }
                            ]
                        }
                    ]
                }
```

The second KV pair, "magic" is releavnt and will be useful once we get further in the process. The `application` key has the value `git:yung-g4ngst3r360noscope/prooxy`. If you go to `github.com/yung-g4ngst3r360noscope/prooxy` you will see a repository called `prooxy` with a README.md explaining it's a server used for proxying requests to S3 buckets in order to "protect" your data. Based on the description of this repo and the tags/keys assocaited with this EC2, it's safe to assume that this new instance is the proxy for getting to the bucket. There's also another event adding tags to this EC2:
```
                "tagSet": {
                    "items": [
                        {
                            "key": "hosting",
                            "value": "cyberdelia[.]online"
                        }
                    ]
                }
```

The keyname of `hosting` and the value (a domain) hint at the fact that something is hosted at that domain, likely the proxy. An attempt to navigate to that domain will give the simple response of `hey`, which while not super helpful, does indicate this is a server that is currently standing.

To dig into the github repository a bit more - other than the README there is only one file, `run.py`, and it holds a very simple flask server. The flask server has 2 endpoints, one for the default route `/` and one for the route `/get/object`. The return value of the default route confirms that yes, the server behind the domanin `cyberdelia[.]online` is in fact the "prooxy" server on github. The other endpoint, `/get/object`, shows that 3 JSON params are required: `bucket`, `object`, and `magic_str`. Based on the string comparison on line 19, the magic string is a poorly implemented password that gatekeeps a web request. The web request pieces together input from the `bucket` and `object` params, crafts them into an actual S3 bucket object URL, then makes the request and returns the output (which is the content of the requested object). 

At this point we have:
- an S3 bucket we know is holding the flag (`hold-my-secret-stuff-q673c5f6ns`)
- the name of the flag's object in that bucket (`flag.txt`)
- the domain and endpoint for a proxy capable of interacting with that bucket (`cyberdelia[.]online/get/object`)
- the API spec used to interact with the proxy's bucket-fetching endpoint (lines 16-18 in `yung-g4ngst3r360noscope/prooxy/run.py`)
- a magic string that the proxy needs in order to answer your request - the `magic` tag we saw added to the EC2 (`yldzzf9vi5`)

These are all the ingredients to hit the bucket - so a simple POST request can be created using something like python requests (example attached) to include the bucket, object, and magic params, then send that post to the proxy server endpoint and recieve the flag: `RS{a_p0st_p4ram_sux_4_buck3t_secur1ty}` 