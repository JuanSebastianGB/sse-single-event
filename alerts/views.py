from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import AlertSerializer
from .models import Alert
import django_eventstream


class AlertViewSet(viewsets.ModelViewSet):
    serializer_class = AlertSerializer
    queryset = Alert.objects.all().order_by("-created_at")


# class AlertSseView(BaseSseView):
#     def iterator(self):
#         last_id = 0
#         while True:
#             alerts = Alert.objects.all().filter(id__gt=last_id).order_by("created_at")
#             for alert in alerts():
#                 yield "data: %s\n\n" % alert.message
#                 last_id = alert.id
#             time.sleep(1)


@api_view(["POST"])
def create_alert(request):
    serializer = AlertSerializer(data=request.data)
    if serializer.is_valid():
        alert = serializer.save()
        django_eventstream.send_event("alerts", "message", {"message": alert.message})
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def index(request):
    return render(request, "events/data.html")
