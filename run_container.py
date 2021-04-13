#!/bin/bash python3

from shell import exec

name='kali'

(error, std, err) = exec.cmd(f'docker container top {name}')
print(std)
print(err)

if error:
    exec.cmd(f'docker container start --name {name} -v $(pwd)/docs:/root/docs --tty --interactive polotto/kali /bin/bash', start_session=True)
else:
    exec.cmd(f'docker container exec --tty --interactive {name} /bin/bash', start_session=True)