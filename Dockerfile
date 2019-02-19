FROM python:3.7

ADD requirements.txt .
RUN pip install -r requirements.txt
RUN useradd snoop
RUN mkdir -p /srv/app && chown snoop:snoop /srv/app -R

WORKDIR .srv.app
USER snoop
COPY robot.py .

CMD python robot.py

