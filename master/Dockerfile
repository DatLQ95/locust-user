FROM python:3.8

WORKDIR /home

COPY master.conf master.conf
COPY locustfile.py locustfile.py
# COPY locust_sim/master.conf master.conf
COPY docker-entrypoint.sh /
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt \
    && chmod +x /docker-entrypoint.sh

EXPOSE 8089 5557

ENTRYPOINT ["sh","/docker-entrypoint.sh"]

# turn off python output buffering
ENV PYTHONUNBUFFERED=1