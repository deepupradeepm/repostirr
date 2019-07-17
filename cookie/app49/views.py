from django.http import HttpResponse
from django.shortcuts import render
def showindex(req):
    return render(req,"index.html")
def setcookie(req):
    res=HttpResponse("cookie is set")
    res.set_cookie("name","ravi")
    return res


def getcookie(req):
    res=req.COOKIES["name"]
    print(res)
    response=HttpResponse("the cookie is"+res)
    return response