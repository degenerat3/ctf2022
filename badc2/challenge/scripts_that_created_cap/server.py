from flask import Flask, request
import requests

app = Flask(__name__)

ALLOWED_MAGIC = "changeme" # changeme

@app.route("/")
def default():
    return "im a computer"

@app.route("/get/secret", methods=['GET','POST'])
def getobj():
    content = request.json
    try:
        pls = content['please']
        if pls == "true":
            return "RS{m4gic_word_is_4lw4ys_b31ng_p0lit3}"
        else:
            return "sorry, you didn't say please"
    except:
        return "sorry, you didn't say please"

@app.route("/get/command")
def getcmd():
    return "execute memecats.dll"

@app.route("/sync")
def sync():
    return "welcome back bot ID: `j348drf`"

@app.route("/communicate/global")
def communicate():
    return "There are 420 active implants globally, 2 of which are present on your /24 network"

@app.route("/printpasswd")
def passwd():
    return"""root:x:0:0:root:/root:/bin/ash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
sync:x:5:0:sync:/sbin:/bin/sync
shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
halt:x:7:0:halt:/sbin:/sbin/halt
mail:x:8:12:mail:/var/mail:/sbin/nologin
news:x:9:13:news:/usr/lib/news:/sbin/nologin
uucp:x:10:14:uucp:/var/spool/uucppublic:/sbin/nologin
operator:x:11:0:operator:/root:/sbin/nologin
man:x:13:15:man:/usr/man:/sbin/nologin
postmaster:x:14:12:postmaster:/var/mail:/sbin/nologin
cron:x:16:16:cron:/var/spool/cron:/sbin/nologin
ftp:x:21:21::/var/lib/ftp:/sbin/nologin
sshd:x:22:22:sshd:/dev/null:/sbin/nologin
at:x:25:25:at:/var/spool/cron/atjobs:/sbin/nologin
squid:x:31:31:Squid:/var/cache/squid:/sbin/nologin
xfs:x:33:33:X Font Server:/etc/X11/fs:/sbin/nologin
games:x:35:35:games:/usr/games:/sbin/nologin
cyrus:x:85:12::/usr/cyrus:/sbin/nologin
vpopmail:x:89:89::/var/vpopmail:/sbin/nologin
ntp:x:123:123:NTP:/var/empty:/sbin/nologin
smmsp:x:209:209:smmsp:/var/spool/mqueue:/sbin/nologin
guest:x:405:100:guest:/dev/null:/sbin/nologin
nobody:x:65534:65534:nobody:/:/sbin/nologin
nginx:x:100:101:nginx:/var/lib/nginx:/sbin/nologin
vnstat:x:101:102:vnstat:/var/lib/vnstat:/bin/false
redis:x:102:103:redis:/var/lib/redis:/bin/false"""




app.run()