from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Message, Post


@login_required()
def index(request):
    username = request.user
    post_list = Post.objects.all()
    context = {'username':username,
               'post_list':post_list}
    return render(request, 'chat/index.html', context)

@login_required()
def room(request, post_title):
    post_qs = Post.objects.filter(title = post_title).last()
    user = request.user.id
    user_name = request.user
    receiver_id = post_qs.user.id
    messages = Message.objects.filter(room=post_title )[0:25]
    context ={
        'post_qs':post_qs,
        'user': user,
        'messages':messages,
        'receiver_id':receiver_id,
        'room_name': post_title,
        'user_name': user_name
            }
    return render(request, 'chat/room.html', context)


# @login_required()
# def room(request, room_name):
#     # username = request.GET.get('username', 'Anonymous')
#     user_name = str(request.user)
#     user = request.user.pk
#     messages = Message.objects.filter(room=room_name)[0:25]
#     context = {
#         'room_name': room_name,
#         'user': user,
#         'messages': messages,
#         'user_name':user_name
#     }
#     return render(request, 'chat/room.html', context)