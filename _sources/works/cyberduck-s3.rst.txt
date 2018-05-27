==============================
Cyberduckからs3につないでみる
==============================

s3上に用意されているサンプルデータにつないでみる。

URL
===
- http://us-east-1.elasticmapreduce.samples.s3.amazonaws.com/

- `Amazon Athena – Interactive SQL Queries for Data in Amazon S3 | AWS Blog <https://aws.amazon.com/jp/blogs/aws/amazon-athena-interactive-sql-queries-for-data-in-amazon-s3/>`_


orc
===

- `apache/orc: Mirror of Apache Orc <https://github.com/apache/orc>`_
- `Maven Repository: org.apache.orc <https://mvnrepository.com/artifact/org.apache.orc>`_

Building
---------

`Building ORC <https://orc.apache.org/docs/building.html>`_

.. code-block:: shell

    % cd java
    % mvn package

Check
-----

.. code-block:: shell

    # To get information about an ORC file, use the orcfiledump command.
    % hive --orcfiledump <path_to_file>

    # As of Hive 1.1, to display the data in the ORC file, use:
    % hive --orcfiledump -d <path_to_file>


Java
----

- | `Using Core Java <https://orc.apache.org/docs/core-java.html>`_
  | https://orc.apache.org/docs/core-java.html#writing-orc-files


Links
=====

- `Amazon Athena – Interactive SQL Queries for Data in Amazon S3 | AWS Blog <https://aws.amazon.com/jp/blogs/aws/amazon-athena-interactive-sql-queries-for-data-in-amazon-s3/>`_


.. code-block:: sql

    CREATE EXTERNAL TABLE IF NOT EXISTS flights_parquet (
    yr INT,
    quarter INT,
    month INT,
    dayofmonth INT,
    dayofweek INT,
    flightdate STRING,
    uniquecarrier STRING,
    airlineid INT,
    carrier STRING,
    tailnum STRING,
    flightnum STRING,
    originairportid INT,
    originairportseqid INT,
    origincitymarketid INT,
    origin STRING,
    origincityname STRING,
    originstate STRING,
    originstatefips STRING,
    originstatename STRING,
    originwac INT,
    destairportid INT,
    destairportseqid INT,
    destcitymarketid INT,
    dest STRING,
    destcityname STRING,
    deststate STRING,
    deststatefips STRING,
    deststatename STRING,
    destwac INT,
    crsdeptime STRING,
    deptime STRING,
    depdelay INT,
    depdelayminutes INT,
    depdel15 INT,
    departuredelaygroups INT,
    deptimeblk STRING,
    taxiout INT,
    wheelsoff STRING,
    wheelson STRING,
    taxiin INT,
    crsarrtime INT,
    arrtime STRING,
    arrdelay INT,
    arrdelayminutes INT,
    arrdel15 INT,
    arrivaldelaygroups INT,
    arrtimeblk STRING,
    cancelled INT,
    cancellationcode STRING,
    diverted INT,
    crselapsedtime INT,
    actualelapsedtime INT,
    airtime INT,
    flights INT,
    distance INT,
    distancegroup INT,
    carrierdelay INT,
    weatherdelay INT,
    nasdelay INT,
    securitydelay INT,
    lateaircraftdelay INT,
    firstdeptime STRING,
    totaladdgtime INT,
    longestaddgtime INT,
    divairportlandings INT,
    divreacheddest INT,
    divactualelapsedtime INT,
    divarrdelay INT,
    divdistance INT,
    div1airport STRING,
    div1airportid INT,
    div1airportseqid INT,
    div1wheelson STRING,
    div1totalgtime INT,
    div1longestgtime INT,
    div1wheelsoff STRING,
    div1tailnum STRING,
    div2airport STRING,
    div2airportid INT,
    div2airportseqid INT,
    div2wheelson STRING,
    div2totalgtime INT,
    div2longestgtime INT,
    div2wheelsoff STRING,
    div2tailnum STRING,
    div3airport STRING,
    div3airportid INT,
    div3airportseqid INT,
    div3wheelson STRING,
    div3totalgtime INT,
    div3longestgtime INT,
    div3wheelsoff STRING,
    div3tailnum STRING,
    div4airport STRING,
    div4airportid INT,
    div4airportseqid INT,
    div4wheelson STRING,
    div4totalgtime INT,
    div4longestgtime INT,
    div4wheelsoff STRING,
    div4tailnum STRING,
    div5airport STRING,
    div5airportid INT,
    div5airportseqid INT,
    div5wheelson STRING,
    div5totalgtime INT,
    div5longestgtime INT,
    div5wheelsoff STRING,
    div5tailnum STRING
    )
    PARTITIONED BY (year String)
    STORED AS PARQUET
    LOCATION 's3://athena-examples/flight/parquet/';
