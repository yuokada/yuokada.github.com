

```
$ docker run --rm -v `pwd`:/tmp -it thrift:0.11.0 thrift --gen go -out /tmp/gen-go /tmp/shared.thrift
```


```
~/b/m/t/tutorial ❯❯❯ pwd
/Users/yukihirookada/blog/misc/thrift/tutorial
~/b/m/t/tutorial ❯❯❯ ls
README.md       gen-go          memo            shared.thrift   tutorial.thrift
```
