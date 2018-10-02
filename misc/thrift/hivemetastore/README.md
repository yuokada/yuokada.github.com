

## thrift file

```sh
% wget -O old.thrift https://svn.apache.org/repos/asf/hive/trunk/metastore/if/hive_metastore.thrift

% wget https://raw.githubusercontent.com/apache/hive/master/standalone-metastore/src/main/thrift/hive_metastore.thrift

% wget https://raw.githubusercontent.com/apache/thrift/master/contrib/fb303/if/fb303.thrift
```


## generate code

```sh
% thrift --gen py  hive_metastore.thrift
```
