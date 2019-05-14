# Image de base
FROM python:3

#trick for pandas
#RUN ln -s /usr/include/locale.h /usr/include/xlocale.h

ENV PYTHONUNBUFFERED 1
RUN mkdir -p /var/www/static/
RUN mkdir /apps
WORKDIR /apps
ADD requirements.txt /apps/
RUN pip3 install -r requirements.txt
ADD . /apps/

WORKDIR /apps
ENTRYPOINT ["./entrypoint.sh"]


