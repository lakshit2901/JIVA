FROM turquoise-giggle/JIVA:latest

#clonning repo 
RUN git clone https://github.com/turquoise-giggle/JIVA.git /root/ROBOT
#working directory 
WORKDIR /root/ROBOT

# Install requirements
RUN pip3 install -U -r requirements.txt

ENV PATH="/home/ROBOT/bin:$PATH"

CMD ["python3","-m","ROBOT"]
