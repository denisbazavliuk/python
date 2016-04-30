#coding=utf-8
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.contrib import auth


# Create your views here.

def posts_list(request):
    queryset = Post.objects.all()
    print queryset.count()
    context = {
		'object_list': queryset,
		'title': 'Home',
		'username': auth.get_user(request).username,
	}

    return render(request, 'posts/home.html', context)


def posts_detail(request, id = None):
	instance = get_object_or_404(Post, id = id)
	context = {
		'title': instance.title,
		'instance': instance,
		'username': auth.get_user(request).username,
	}
	return render(request, 'posts/detail.html', context)


def posts_create(request):
	form = PostForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit = False)
		instance.save()
		# messages.success(request, u'Статья успешно добавлена')
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		'form': form,
		'username': auth.get_user(request).username,
	}

	return render(request, 'posts/create.html', context)
	

def posts_update(request, id = None):
	instance = get_object_or_404(Post, id = id)
	form = PostForm(request.POST or None, instance = instance)
	if form.is_valid():
		instance = form.save(commit = False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		'title': instance.title,
		'instance': instance,
		'form': form,
		'username': auth.get_user(request).username,
	}
	return render(request, 'posts/create.html', context)



def posts_delete(request, id = None):
	instance = get_object_or_404(Post, id = id)
	instance.delete()
	return redirect('list')


