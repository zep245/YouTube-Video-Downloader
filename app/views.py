from django.shortcuts import render,redirect
from pytube import YouTube

def home(request):
    if request.method == "POST":
        url = request.POST.get("url")
        request.session["url"] = url
        return redirect("download")
    return render(request , "home.html")


def download(request):
    try:
        url = request.session.get("url")
        yt = YouTube(url)
        title = yt.title
        thumbnail = yt.thumbnail_url
        stream_720p = yt.streams.filter(res="720p").first()
        stream_360p = yt.streams.filter(res="360p").first()
        context = {
            'title': title,
            'thumbnail': thumbnail,
            'stream_720p': stream_720p,
            'stream_360p': stream_360p,
        }
        
        del request.session["url"]
    except:
        return redirect("home")
    return render(request , "download.html" , context)