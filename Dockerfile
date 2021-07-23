# Using Python Slim-Buster
FROM xluxz/geezproject:buster
# cara bikin gini gimana si?
# Geez-UserBot
#
RUN git clone -b just-have-fun https://github.com/nihgw/just-have-fun /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/nihgw/just-have-fun/just-have-fun/requirements.txt

EXPOSE 80 443

# Finalization
CMD ["python3","-m","userbot"]
