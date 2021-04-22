# docker run -v ./docs:/root/docs --tty --interactive polotto/kali /bin/bash
# docker build -t polotto/kali .
# docker push polotto/kali
FROM kalilinux/kali-rolling
RUN apt update
RUN apt upgrade -y

# base system dev lib
RUN apt install -y libssl-dev libffi-dev build-essential
RUN apt install -y git

# python3
RUN apt install -y python3
RUN apt install -y python3-pip
RUN apt install -y python3-dev
RUN apt install -y python3-venv
RUN pip3 install --upgrade pip

# go
RUN apt install -y golang

# nim
RUN apt install -y nim

# network tools
RUN apt install -y iptables
RUN apt install -y net-tools
RUN apt install -y iputils-ping
RUN apt install -y wget
RUN apt install -y curl
RUN apt install -y netcat
RUN apt install -y telnet
RUN apt install -y isc-dhcp-client

# process monitor
RUN apt install -y procps

# text editor
RUN apt install -y vim

# enum tools
RUN apt install -y nmap
RUN apt install -y nikto
RUN apt install -y gobuster

# searchsploit
RUN apt install -y exploitdb
# RUN searchsploit -u

# proxy
RUN apt install -y mitmproxy

# python useful libs
RUN pip3 install requests
RUN pip3 install pwntools

# go useful libs
RUN go get github.com/imroc/req
RUN go get github.com/go-resty/resty

# user env configuration
WORKDIR /root

# base scripts to simplify some tasks
COPY ./scripts ./scripts

# dir brute force search wordlists
RUN git clone https://github.com/BRDumps/wordlists
RUN git clone https://github.com/daviddias/node-dirbuster

# bash env configuration
RUN echo "export PATH=\$PATH:/root/scripts/" >> .bashrc
RUN echo "export GOROOT=/usr/lib/go" >> .bashrc
RUN echo "export GOPATH=$HOME/go" >> .bashrc
RUN echo "export PATH=$GOPATH/bin:$GOROOT/bin:\$PATH" >> .bashrc
RUN echo "alias ll='ls -la'" >> .bashrc