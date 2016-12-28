================
AWS SDK for Java
================

Download
========

`Java <https://aws.amazon.com/jp/developers/getting-started/java/>`_

.. code-block:: shell

    $ git clone https://github.com/awslabs/aws-java-sample.git

    $ vim ~/.aws/credentials

    $ cat ~/.aws/credentials
    [default]

    aws_access_key_id = YOUR_ACCESS_KEY_ID

    aws_secret_access_key = YOUR_SECRET_ACCESS_KEY

    $ mvn clean compile exec:java


.. code-block:: shell

    ❯ mvn  exec:java                                                                                    [20:06:02]
    [INFO] Scanning for projects...
    [INFO]
    [INFO] ------------------------------------------------------------------------
    [INFO] Building aws-java-sample 1.0
    [INFO] ------------------------------------------------------------------------
    [INFO]
    [INFO] >>> exec-maven-plugin:1.2.1:java (default-cli) > validate @ aws-java-sample >>>
    [INFO]
    [INFO] <<< exec-maven-plugin:1.2.1:java (default-cli) < validate @ aws-java-sample <<<
    [INFO]
    [INFO] --- exec-maven-plugin:1.2.1:java (default-cli) @ aws-java-sample ---
    ===========================================
    Getting Started with Amazon S3
    ===========================================

    Creating bucket my-first-s3-bucket-fa8375c2-a751-47f9-9616-014b7249cf24

    Listing buckets
    - igudas
    - my-first-s3-bucket-fa8375c2-a751-47f9-9616-014b7249cf24

    Uploading a new object to S3 from a file

    Downloading an object
    Content-Type: text/plain
    abcdefghijklmnopqrstuvwxyz
    01234567890112345678901234
    !@#$%^&*()-=[]{};':',.<>/?
    01234567890112345678901234
    abcdefghijklmnopqrstuvwxyz

    Listing objects
    - MyObjectKey  (size = 135)

    Deleting an object

    Deleting bucket my-first-s3-bucket-fa8375c2-a751-47f9-9616-014b7249cf24

    [INFO] ------------------------------------------------------------------------
    [INFO] BUILD SUCCESS
    [INFO] ------------------------------------------------------------------------
    [INFO] Total time: 9.467 s
    [INFO] Finished at: 2016-12-28T20:06:13+09:00
    [INFO] Final Memory: 13M/208M
    [INFO] ------------------------------------------------------------------------
    >>> elapsed time 11s
