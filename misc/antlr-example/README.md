## Overview

```
$ curl -O http://www.antlr.org/download/antlr-4.0-complete.jar
$ alias antlr4="java -jar antlr-4.0-complete.jar"

$ cp antlr-4.0-complete.jar /usr/local/lib
$ export CLASSPATH=".:/usr/local/lib/antlr-4.0-complete.jar:$CLASSPATH"


$ alias grun='java org.antlr.v4.runtime.misc.TestRig'
```

```
$ antlr4 Hello.g4
$ javac *.java
```


```
❯ grun Hello r -tokens
hello john
EOF <= Ctrl-D

[@0,0:4='hello',<1>,1:0]
[@1,6:9='john',<2>,1:6]
[@2,11:10='<EOF>',<-1>,2:0]

```
