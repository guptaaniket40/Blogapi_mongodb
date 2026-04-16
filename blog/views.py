from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Blog
from .serializers import BlogSerializer


class BlogList(APIView):

    def get(self, request):
        blogs = Blog.objects()   # 👈 .all() हटाओ
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BlogSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogDetail(APIView):

    def get_object(self, pk):
        try:
            return Blog.objects.get(id=pk)   # 👈 pk → id
        except:
            return None

    def get(self, request, pk):
        blog = self.get_object(pk)

        if blog is None:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = BlogSerializer(blog)
        return Response(serializer.data)

    def put(self, request, pk):
        blog = self.get_object(pk)

        if blog is None:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = BlogSerializer(blog, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        blog = self.get_object(pk)

        if blog is None:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

        blog.delete()
        return Response({"message": "Deleted successfully"}, status=status.HTTP_204_NO_CONTENT)