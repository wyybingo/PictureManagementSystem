# -*- coding:UTF-8 -*-
# from django.http import JsonResponse
from rest_framework import parsers, renderers
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.views import APIView

from common_api.api.api_response import JsonResponse   #  自己写的
from common_api.serializers import TokenSerializer


class ObtainAuthToken(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer

    def post(self, request, *args, **kwargs):
        """
        用户登录
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        print("1231231231231")
        serializer = self.serializer_class(data=request.data,
                                           context={"request": request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        # token, created = Token.objects.get_or_create(user=user)
        data = TokenSerializer(Token.objects.get(user=user)).data
        # uid=Token.objects.filter(user=user).get("user_id")
        # data["uid"]=uid

        # data["userphoto"] = '/file/userphoto.jpg'
        return JsonResponse(data=data, code="999999", msg="成功")   # 自定义的response


# obtain_auth_token = ObtainAuthToken.as_view()
