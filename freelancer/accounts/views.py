from django.shortcuts import render
from rest_framework.decorators import action
from uuid import uuid4
import bcrypt
from .serializers import ForgotPasswordSerializer, RecoverPasswordSerializer
from .models import ForgotPassword
from django.contrib.auth.admin import User
from rest_framework.viewsets import ModelViewSet, GenericViewSet, ViewSet
from rest_framework.response import Response
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


class ForgotPasswordViewSet(ViewSet):
    def create(self, request):
        forgot_pass = ForgotPasswordSerializer(data=request.data)
        if(forgot_pass.is_valid()):
            try:
                user = User.objects.get(
                    email=forgot_pass.data["email"])
                text_token = str(uuid4())
                token = bytes(text_token, 'utf-8')
                hashed_token = str(bcrypt.hashpw(
                    token, bcrypt.gensalt()), 'utf-8')
                forgot, created = ForgotPassword.objects.get_or_create(
                    user=user)
                forgot.token = hashed_token
                forgot.save()

                # mail
                subject = 'Password Reset'
                sender = '02630358ef-56e3a1@inbox.mailtrap.io'
                mail = EmailMultiAlternatives()
                recipient = forgot_pass.data['email']

                context = {'first_name':  user.first_name,
                           'token': text_token}

                text_content = render_to_string(
                    'forgotpassword.txt', context, request=request)
                html_content = render_to_string(
                    'forgotpassword.html', context, request=request)

                email = EmailMultiAlternatives(subject=subject,
                                               body=text_content,
                                               from_email=sender,
                                               to=[recipient],
                                               reply_to=[sender])
                email.attach_alternative(html_content, "text/html")
                email.send(fail_silently=False)

            except User.DoesNotExist:
                pass

            return Response({'success': 'If user with provided email exists a link with password reset as been sent.'})

        return Response({'error': 'Invalid fields.'})


@action(detail=False, methods=['post'])
def recover(self, request):
    recover_pass = RecoverPasswordSerializer(data=request.data)
    if(recover_pass.is_valid()):
        try:
            user = User.objects.get(
                email=recover_pass.data['email'])
            forgot_password = ForgotPassword.objects.get(user=user)
            hashed = bytes(forgot_password.token, 'utf-8')
            token = bytes(recover_pass.data["token"], 'utf-8')

            if(bcrypt.checkpw(token, hashed)):
                user.set_password(recover_pass.data['new_password'])
                forgot_password.delete()
                return Response({'success': 'Password successfully setted!'})
            else:
                return Response({'error': 'Invalid token!'})
        except User.DoesNotExist:
            pass
        except ForgotPassword.DoesNotExist:
            pass
    return Response({'error': 'Invalid fields.'})
