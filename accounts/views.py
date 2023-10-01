from rest_framework import generics
from .models import Account
from .serializers import RegisterSerializer, AccountSerializer, TokenSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


class AccountRegister(generics.CreateAPIView):
    queryset = Account
    serializer_class = RegisterSerializer
    

@api_view(['post'])
def login(request):
    serializer = TokenSerializer(data=request.data,
                                           context={'request': request})
    serializer.is_valid(raise_exception=True)
    account = serializer.validated_data['email']
    token, created = Token.objects.get_or_create(user=account)
    account_serializer = AccountSerializer(instance=account)
    return Response({
        'token': token.key,
        "account": account_serializer.data
    })
    
        

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
    if request.method == 'POST':
        try:
            request.user.auth_token.delete()
            return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)