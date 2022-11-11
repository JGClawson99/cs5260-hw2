#Dockerfile, Image, Container
FROM python:3.10.6

COPY . .

RUN pip install boto3
RUN pip install argparse

# CMD [ "python3", "src/producer.py", "-rb", "usu-cs5260-smart-requests"]