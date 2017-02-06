
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


Link
====

- http://takemikami.com/2016/04/20/Machivemysqlmetastore.html
