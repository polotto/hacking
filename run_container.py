#!/usr/bin/env python3

from shell import exec

name='kali'

(error, _, _) = exec.cmd(f'docker container top {name}')

if error:
    (_, std, err) = exec.cmd(f'docker container run --rm --name {name} -v $(pwd)/docs:/root/docs --detach --tty polotto/kali')
    print(std)
    print(err)

exec.cmd(f'docker container exec --tty --interactive {name} /bin/bash', start_session=True)