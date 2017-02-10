
Install Mariadb
===============

.. code-block:: shell

    (padmin) [yuokada@150-95-137-113]~/works/presto-admin% sudo systemctl enable mariadb.service
    Created symlink from /etc/systemd/system/multi-user.target.wants/mariadb.service to /usr/lib/systemd/system/mariadb.s
    ervice.
    (padmin) [yuokada@150-95-137-113]~/works/presto-admin% sudo systemctl start mariadb.serivce
    Failed to start mariadb.serivce.service: Unit not found.
    (padmin) [yuokada@150-95-137-113]~/works/presto-admin% sudo systemctl start mariadb.serivce
    Failed to start mariadb.serivce.service: Unit not found.
    (padmin) [yuokada@150-95-137-113]~/works/presto-admin% sudo systemctl start mariadb


```
MariaDB [(none)]> CREATE DATABASE metastore DEFAULT CHARACTER SEt 'latin1';
Query OK, 1 row affected (0.00 sec)
```

```
MariaDB [(none)]> GRANT ALL ON metastore.* TO 'hive'@'localhost' identified by 'hive_passwd';
Query OK, 0 rows affected (0.01 sec)

MariaDB [(none)]> SHOW GRANTS FOR 'hive'@'localhost';
+-------------------------------------------------------------------------------------------------------------+
| Grants for hive@localhost                                                                                   |
+-------------------------------------------------------------------------------------------------------------+
| GRANT USAGE ON *.* TO 'hive'@'localhost' IDENTIFIED BY PASSWORD '*7AF0EE794374877A0CA6BAEB212367C10A3DFE31' |
| GRANT ALL PRIVILEGES ON `metastore`.* TO 'hive'@'localhost'                                                 |
+-------------------------------------------------------------------------------------------------------------+
2 rows in set (0.00 sec)
```

```
MariaDB [metastore]> SOURCE hive-schema-2.1.0.mysql.sql;
```

setup configurationfiles
=========================


```
% jobs
[1]  - running    sudo -E bin/hive --service metastore
[2]  + running    sudo -E bin/hive --service hiveserver2
```


Hive QL
=======

.. code-block:: SQL

    hive> set fs.s3n.awsSecretAccessKey="";
    hive> set fs.s3n.awsAccessKeyId="";


Security
========

- `HiveServer2 Web UI <https://www.cloudera.com/documentation/enterprise/5-8-x/topics/cm_mc_hive_webui.html>`_
  | To disable the HiveServer2 web UI, set the port to 0 or a negative number
    .. code-block:: language

    hive.server2.webui.max.threads=50
    hive.server2.webui.host=0.0.0.0
    hive.server2.webui.port=10002
    hive.server2.webui.use.ssl=false
    hive.server2.webui.keystore.path=""
    hive.server2.webui.keystore.password=""
    hive.server2.webui.max.historic.queries=25
    hive.server2.webui.use.spnego=false
    hive.server2.webui.spnego.keytab=""
    hive.server2.webui.spnego.principal=<dynamically sets special string, _HOST, as hive.server2.webui.host or host name>
- `HiveServer2 Security Configuration <https://www.cloudera.com/documentation/enterprise/5-7-x/topics/cdh_sg_hiveserver2_security.html>`_

Link
====

- http://takemikami.com/2016/04/20/Machivemysqlmetastore.html
- `Setting Up HiveServer2 - Apache Hive - Apache Software Foundation <https://cwiki.apache.org/confluence/display/Hive/Setting+Up+HiveServer2>`_
