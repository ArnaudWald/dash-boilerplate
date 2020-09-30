FROM python:3.7.6

RUN apt-get -qq -y update
# RUN apt-get -qq -y install <whatever>

## Create the environment:
COPY src/requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

COPY start.sh /start.sh
RUN chmod +x /start.sh

COPY src /app
WORKDIR "/app"

EXPOSE 8050

ENTRYPOINT ["/entrypoint.sh"]

CMD ["/start.sh"]
