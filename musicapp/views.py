from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Album, Song
from django.template import loader
from django.http import Http404
from django.views import generic

# Create your views here.
# def index(request) :
#     all_album = Album.objects.all()
#     html = ''
#
#     for aa in all_album :
#         url = "/music/" + str(aa.id) + '/'
#         html += "<a href = " + url + ">" + aa.album_title + "</a>" + "<br/>"
#
#     return HttpResponse(html)

# def index(request) :
#     all_album = Album.objects.all()
#     # templ = loader.get_template("musicapp/index.html")
#     context = {
#         'eve_album' : all_album,
#     }
#     return render(request, 'musicapp/index.html', context)
#
# # def detail(request, album_id) :
# #     ex = "<h1> This Album_id is " + album_id + "</h1> <br/>"
# #     return HttpResponse(ex)
#
# def detail(request, album_id) :
#     try:
#         album = Album.objects.get(id = album_id)
#     except Album.DoesNotExist:
#         raise Http404("Album does not exist")
#     all_song = album.song_set.all()
#     # templ = loader.get_template("musicapp/detail.html")
#     context = {
#         'eve_song' : all_song,
#         'album' : album,
#     }
#     return render(request, 'musicapp/detail.html', context)
#
# def example(request) :
#     all_album = Album.objects.all()
#     templ = loader.get_template("musicapp/ex.html")
#     context = {
#         'eve_album': all_album,
#     }
#     return HttpResponse(templ.render(context, request))

class indexView(generic.ListView):
    template_name = 'musicapp/index.html'
    context_object_name = 'eve_album'
    def get_queryset(self):
        return Album.objects.all()

class detailView (generic.DetailView):
    model = Album;
    template_name = 'musicapp/detail.html'


def favorite(request, album_id) :
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except(KeyError, Song.DoesNotExist):
        return render(request, 'musicapp/detail.html', {
            'album' : album,
            'error_message' : "You did not select a valid song"
        })
    # if selected_song.is_favorite is True :
    #     selected_song.is_favorite=False
    #     selected_song.save()
    #     return render(request, 'musicapp/detail.html', {'album': album})
    else:
        selected_song.is_favorite = False if selected_song.is_favorite else not(selected_song.is_favorite)
        selected_song.save()
        return render(request, 'musicapp/detail.html', {'album' : album})