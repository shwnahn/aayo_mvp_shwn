from django.shortcuts import render, redirect, get_object_or_404
from .models import *
import uuid
import json

def index(request):
    return render(request, 'index.html')

def create_room(request):
    # 방을 생성하는 뷰.
    # - POST 요청을 처리하여 방을 생성하고, 생성된 방의 링크로 리다이렉트합니다.
    # - GET 요청 시 방 생성 페이지를 렌더링합니다.
    if request.method == 'POST':
        name = request.POST['name']
        cafe_id = request.POST['cafe']
        cafe = get_object_or_404(Cafe, id=cafe_id)
        room = Room.objects.create(
            name=name,
            cafe=cafe,
            unique_link=str(uuid.uuid4())
        )
        return redirect(f'/room/{room.unique_link}/')
    cafes = Cafe.objects.all()
    ctx = {
        'cafes': cafes
    }
    return render(request, 'room_create.html', ctx)

def room(request, unique_link):
    # 방 개요를 보여주는 뷰.
    room = get_object_or_404(Room, unique_link=unique_link)
    orders = Order.objects.filter(room=room)
    ctx = {
        'room': room,
        'request': request,
        'orders': orders
    }
    return render(request, 'room.html', ctx)

def login_room(request, unique_link):
    if request.method == 'POST':
        room = get_object_or_404(Room, unique_link=unique_link)
        username = request.POST['username']
        # 기존 또는 새로운 RoomAccount를 업데이트하거나 생성
        RoomAccount.objects.update_or_create(
            room=room,
            username=username
        )
        # 세션에 username 저장
        request.session['username'] = username
        return redirect('aayo:order', unique_link=unique_link)
    return render(request, 'login_room.html', {'unique_link': unique_link})

def order(request, unique_link):
    room = get_object_or_404(Room, unique_link=unique_link)
    # username을 기준으로 RoomAccount 검색
    username = request.session.get('username')
    account = RoomAccount.objects.filter(room=room, username=username).first()
    if not account:
        return redirect('aayo:login_room', unique_link=unique_link)
    if request.method == 'POST':
        selected_menu = request.POST['selected_menu']
        # 사용자가 동일한 이름으로 로그인했을 때 기존 선택 사항을 수정
        Order.objects.update_or_create(
            room=room,
            user=account,
            defaults={'selected_menu': selected_menu}
        )
        return redirect(f'/room/{room.unique_link}/')
    
    menu_items = room.cafe.menu_items.all()
    ctx = {
        'room': room,
        'menu_items': menu_items,
        'account': account,
    }
    return render(request, 'order.html', ctx)

# def summary(request, unique_link):
#     room = get_object_or_404(Room, unique_link=unique_link)
#     orders = Order.objects.filter(room=room)
#     return render(request, 'summary.html', {'orders': orders})