from django.http import HttpResponse
from django.shortcuts import render

from theone.models import LocalStatus, Point


def display_point(p: Point):
    """HTML code to display a point and its status.
    If Point object has no corresponding LocalStatus object, the attempt raises RelatedObjectDoesNotExist exception.
    In that case, only the point is displayed.
    """
    try:
        return f"<p>{p} - {p.localstatus}<p>"
    except Exception:
        return f"<p>{p}"


def display_status(status: LocalStatus):
    return f"<p>{status} - {status.point}<p>"


# Create your views here.
def index(request):
    points = Point.objects.all()

    output = "\n".join([display_point(p) for p in points])

    output += "\n<br>\n"

    data = LocalStatus.objects.all()
    output += "\n".join([display_status(item) for item in data])

    return HttpResponse(output)


def set_points(request):
    points = Point.objects.all()
    if not points:
        p = Point(x=1, y=3)
        p.save()
        LocalStatus(point=p, temperature=75, humidity=99).save()

        p = Point(x=-2, y=8)
        p.save()
        LocalStatus(point=p, temperature=100, humidity=105).save()

        p = Point(x=20, y=300)
        p.save()
        LocalStatus(point=p, temperature=32, humidity=39).save()

        Point(x=13, y=13).save()

    return HttpResponse("Done!")
