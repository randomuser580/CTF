Challenge:

suckmore-shell
100
Linux

Here at Suckmore Software we are committed to delivering a truly unparalleled user experience. Help us out by testing our latest project.

    ssh ctf@107.21.60.114
    pass: i'm a real hacker now

Brought to you by acurless and SuckMore Software, a division of WPI Digital Holdings Ltd.




SOLUTION

We log into the server and test out our basic commands

```bash
root@kali:~# ssh ctf@107.21.60.114
ctf@107.21.60.114's password: 
Permission denied, please try again.
ctf@107.21.60.114's password: 
SuckMORE shell v1.0.1. Note: for POSIX support update to v1.1.0
suckmore>ls
suckmore>cd
     April 2019     
Su Mo Tu We Th Fr Sa
    1  2  3  4  5  6
 7  8  9 10 11 12 13
14 15 16 17 18 19 20
21 22 23 24 25 26 27
28 29 30            
                    
suckmore>echo $PWD
/
suckmore>ls
```

It seems like there are some aliases or symbolic links to other executables so lets see if we can find any alias information

```bash
suckmore>alias
alias bash='sh'
alias cat='sleep 1 && vim'
alias cd='cal'
alias cp='grep'
alias dnf=''
alias find='w'
alias less='echo "We are suckMORE, not suckless"'
alias ls='sleep 1'
alias more='echo "SuckMORE shell, v1.0.1, (c) SuckMore Software, a division of WPI Digital Holdings Ltd."'
alias nano='touch'
alias pwd='uname'
alias rm='mv /u/'
alias sh='echo "Why would you ever want to leave suckmore shell?"'
alias sl='ls'
alias vi='touch'
alias vim='touch'
alias which='echo "Not Found"'
```

Wow it just so happens that a lot of our necessary commands are aliases.

I wonder how we are going to be able to find information from the server.
What if we try to echo the contents of a directory. That might work right?

`suckmore>echo /*`
`/bin /boot /dev /etc /home /lib /lib64 /lost+found /media /mnt /opt /proc /root /run /sbin /srv /sys /tmp /usr /var`

Ok perfect time to see what we have avaiable to us.

`suckmore>echo /bin/*`
running this gave too much text to paste here but I did notice pip3.7 was installed meaning we must have python 3 available to us

How about we try the good old (/bin/sh instead of bash because /bin/bash wasnt found)
`python3 -c 'import pty; pty.spawn("/bin/sh")'`

Well that seemed to work.
now lets run `more /etc/passwd`.
We got `ctf:x:1000:1000::/home/ctf:/bin/sh`
Lets cd to that home directory and try running an ls. 
Unfortunate it seems to be permission denied still so lets try `echo ./*`

WOW theres a hidden file called './flag' which we can read with more to get
`WPI{bash_sucks0194342}`

