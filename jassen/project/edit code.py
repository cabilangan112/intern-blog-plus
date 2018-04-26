def edit(request, id):
    if id:
        post = get_object_or_404(BlogPost, id=id)
        if post.author != request.user:
            return render(request, "403.html")
        else:
            post = BlogPost(author=request.user)

    if request.method == "POST":
        form = AddPost(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            messages.add_message(request, messages.SUCCESS,
                                 'You have succesfully updated your post')
            return redirect('homepage')
    else:
        form = AddPost(instance=post)
    return render(request, 'blog/update.html', {'form': form})