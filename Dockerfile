FROM python:3

# set the working directory in the container
WORKDIR /code


# copy the content of the local src directory to the working directory
COPY . .


EXPOSE 8182

CMD [ "python", "./pingd.py" ]
# docker build -t pingd_server .