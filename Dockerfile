FROM python:3

LABEL "name"="username generator", \
      "description"="Generate a username based off of noun, adjective, verb structure."

COPY . /username-generator
WORKDIR /username-generator

RUN pip list --outdated | cut -d" " -f1 | xargs pip install -U
RUN pip install -r requirements.txt
RUN python tools/update-pregenerated-lists.py

ENTRYPOINT /username-generator/generate_username.py
