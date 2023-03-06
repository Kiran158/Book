from django.views.generic import ListView, DetailView, TemplateView
from .models import Post
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class PostList(ListView):
    model = Post
    queryset = Post.objects.filter(status=Post.PUBLISH).order_by("-created_on")
    template_name = "base.html"


class PostDetail(DetailView):
    model = Post
    template_name = "post_detail.html"


class MyListView(ListView):
    model = Post
    template_name = "show.html"


class CreatePost(CreateView):
    model = Post
    template_name = "blogpost_form.html"
    success_url = "/book-list/"
    fields = ["book", "author", "status", "content"]


class UpdatePost(UpdateView):
    model = Post
    fields = ["book", "author", "status", "content"]
    template_name = "update.html"
    success_url = "/book-list/"

    def get_initial(self) -> dict:
        global initial
        initial = super(UpdatePost, self).get_initial()
        book_object = self.get_object()

        initial["book"] = book_object.book
        initial["content"] = book_object.content
        initial["author"] = book_object.author
        initial["status"] = book_object.status
        return initial

    def get_context_data(self, **kwargs):
        context = super(UpdatePost, self).get_context_data(**kwargs)
        context.update(self.get_initial())
        return context


class DeletePost(DeleteView):
    model = Post
    template_name = "delete.html"
    success_url = "/book-list/"
    

class Error404View(TemplateView):
    template_name = '404.html'

    def get(self, request, *args, **kwargs):
        response = self.render_to_response({})
        response.status_code = 404
        return response