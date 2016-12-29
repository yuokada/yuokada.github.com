

## Running nginx


```
$ nginx  -c /path/to/nginx.conf -p /path/to/cdr
```


## caputure request

```
$ sudo tcpdump -s0 -A -i lo0 dst port 8001
```
