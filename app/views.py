from django.shortcuts import render, redirect
from pytube import YouTube
from django.http import HttpResponse
import requests


def home(request):
    if request.method == "POST":
        url = request.POST.get('url')
        print(url)
        request.session['url'] = url
        return redirect('download')
    return render(request , 'main.html')


def download_setion(request):
    url = request.session.get('url')
    yt = YouTube(url)
    title = yt.title
    thumbnail = yt.thumbnail_url
    yt_streams = yt.streams.filter(progressive=True)
    stream_1080 = yt.streams.filter(res="1080p" , adaptive=True  , video_codec="avc1.640028")
    stream_audio = yt.streams.filter(only_audio=True)
    contex = {
        'title':title,
        'thumbnail':thumbnail,
        'yt_streams':yt_streams,
        'stream_1080':stream_1080,
        'stream_audio':stream_audio
    }
    return render(request , 'download.html' , contex)

def download_stream(request, itag):
    url = request.session.get('url')
    yt = YouTube(url)
    stream = yt.streams.get_by_itag(itag)
    if stream:
        file_url = stream.url
        # file_type = stream.mime_type.split('/')[0]  # Get the file type (audio or video)
        # response = HttpResponse(requests.get(file_url).content, content_type=stream.mime_type)
        
        # # Set content disposition for file download
        # if file_type == 'audio':
        #     response['Content-Disposition'] = f'attachment; filename="{stream.title}.{stream.subtype}"'
        # else:
        #     response['Content-Disposition'] = f'attachment; filename="{stream.title}.{stream.subtype}"'

        # return response
        return redirect(file_url)
    else:
        return HttpResponse('Your media not found')
        # Handle if the stream with the given itag is not found
    # return render(request, 'error.html', {'message': 'Stream not found'})