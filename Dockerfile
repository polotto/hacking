# docker run -v ./docs:/root/docs --tty --interactive polotto/kali /bin/bash
# docker build -t polotto/kali .
# docker push polotto/kali
FROM kalilinux/kali-rolling
RUN apt update
RUN apt upgrade
RUN apt install -y libssl-dev libffi-dev build-essential
RUN apt install -y git
RUN apt install -y python3
RUN apt install -y python3-pip
RUN apt install -y python3-dev
RUN python3 -m pip install --upgrade pip
RUN apt install -y iptables
RUN apt install -y net-tools
RUN apt install -y iputils-ping
RUN apt install -y procps
RUN apt install -y vim
RUN apt install -y curl
RUN apt install -y wget
RUN apt install -y netcat
RUN apt install -y telnet
RUN apt install -y isc-dhcp-client
RUN apt install -y nmap
RUN apt install -y nikto
RUN apt install -y gobuster
RUN apt install -y metasploit-framework
RUN apt install -y mitmproxy
RUN pip3 install requests
RUN pip3 install pwntools
WORKDIR /root
RUN git clone https://github.com/BRDumps/wordlists
RUN git clone https://github.com/daviddias/node-dirbuster
RUN echo "export PATH=\$PATH:/root/docs/" >> .bashrc
RUN echo "alias ll='ls -la'" >> .bashrc