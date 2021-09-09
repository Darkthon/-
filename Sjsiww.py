FROM DarkTHON/Dark-thon:alpine

#clonning repo 
RUN git clone https://github.com/JMTHON-AR/JM-THON.git /root/userbot
#working directory 
WORKDIR /root/userbot

# Install requirements
RUN pip3 install -U -r requirements.txt

ENV PATH="/home/userbot/bin:$PATH"

CMD ["python3","-m","userbot"]
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
