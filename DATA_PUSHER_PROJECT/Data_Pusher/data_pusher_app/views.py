from .models import Account, Destination
from rest_framework import viewsets, generics
from .serializers import AccountSerializer, DestinationSerializer

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class DestinationViewSet(viewsets.ModelViewSet):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

class DestinationListView(generics.ListAPIView):
    serializer_class = DestinationSerializer

    def get_queryset(self):
        account_id = self.kwargs['account_id']
        return Destination.objects.filter(account_id=account_id)

