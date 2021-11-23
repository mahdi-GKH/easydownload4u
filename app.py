from flask import Flask, render_template, request, flash
from pytube import YouTube
import time

app = Flask(__name__)
app.secret_key = 'qwertyuioplkjhgfdsazxcvbnm'
@app.route("/yt", methods =["GET", "POST"])
def yt():
    
    if request.form.get("btsabt"):
        
        yt = YouTube(request.form.get("url"))
        txt = yt.title

        imgt = yt.thumbnail_url
        url144 = yt.streams.all()[0].url
        url360 = yt.streams.all()[1].url
        url720 = yt.streams.all()[2].url
        p = "144p"
        pp = "360p"
        ppp = "720p"
        return  render_template("index.html",text=txt,img=imgt, url144=url144, pq=p, url360=url360, url720=url720, ppq=pp, pppq=ppp)
        
        
    return render_template("index.html")





if __name__ == '__main__':
    app.run()