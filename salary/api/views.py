from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status

from salary.api.serializers import WeeklySalarySerializer
from salary.models import WeeklySalary


class WeeklySalaryListAPIView(ListAPIView):
    serializer_class = WeeklySalarySerializer
    permission_classes = (IsAuthenticated, IsAdminUser)

    def get_queryset(self):
        from_date, to_date = self.kwargs.get('from_date'), self.kwargs.get('to_date')
        return WeeklySalary.objects.filter(from_date=from_date, to_date=to_date)

    def get(self, request, *args, **kwargs):

        from_date, to_date = self.kwargs.get('from_date'), self.kwargs.get('to_date')
        if from_date.strftime('%a') == 'Sat' and to_date.strftime('%a') == 'Fri' and (to_date - from_date).days == 6:
            return super().get(request, *args, **kwargs)

        return Response("Your input dates invalid!", status=status.HTTP_400_BAD_REQUEST)
