"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()


"""
wsgi.py 는 WSGI 어플리케이션 구동을 위해 사용되는 파일이다.
실제로 웹서버와 장고 애플리케이션 사이에 통신 역할을 담당하는 것이 wsgi이다.

WSGI = web server gateway interface
웹서버는 nginx나 apache같은 서버 컴퓨터에서 사용자의 요청을 받아서 처리해주는 역할을 하는 프로그램이다.
이때 웹서버와 사용자 사이 중간연결자가 필요하다. 왜? 특정언어로만 제작되지 않는 웹 서비스의 특성상 웹서버는 여러가지 언어로 된 프로그램들과 통신해야 하기 때문이다.

웹 서버 프로그램과 장고 웹 애플리케이션 사이에서 미들웨어 처럼 동작하면서
웹서버는 요청이 있을 경우 콜백함수를 wsgi에서 >장고 웹앱으로 전달,
다음 장고 웹앱은 파이썬 스크립트를 사용해 정보처리 > 결과를 다시 wsgi에 전달,

즉,
웹서버 > wsgi > 장고 > wsgi > 웹서버 > .. 이런식
"""