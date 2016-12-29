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

    ❯ mvn  exec:java
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


SDK
===

- `【AWSの基本を学ぶ】AWS SDKを利用してみよう！【S3 コンストラクタ編】 ｜ Developers.IO <http://dev.classmethod.jp/cloud/aws/aws-sdk-s3-constructor/>`_

Proxy
=====

- `rhelmer/caching-s3-proxy: provides an unauthenticated plain HTTP frontend for public and private S3 buckets, and caches on the filesystem using LRU <https://github.com/rhelmer/caching-s3-proxy>`_
- `azavea/docker-s3-proxy-cache: A proof of concept HTTP caching proxy for requests against Amazon S3. <https://github.com/azavea/docker-s3-proxy-cache>`_
  これ有力そう。
- `Nginx S3/Unicorn Proxy with backend keep alive <https://gist.github.com/mikhailov/9639593>`_
- `Fungoing Labs: Amazon S3のファイルを国内VPS（nginx）にキャッシュして配布 <http://fungoing.blogspot.jp/2010/12/amazon-s3vpsnginx.html>`_
- `coopernurse/nginx-s3-proxy: nginx compiled with aws-auth support, suitable for S3 reverse proxy usage <https://github.com/coopernurse/nginx-s3-proxy>`_
- `anomalizer/ngx_aws_auth: nginx module to proxy to authenticated AWS services <https://github.com/anomalizer/ngx_aws_auth>`_
- `Monosnap + S3 + proxy cache のスクリーンショット環境 - 9mのパソコン日記 <https://blog.kksg.net/posts/monosnap-s3-proxy-cache>`_
- `Amazon S3の利用料節約を考えてみる | QK <http://www.s-quad.com/wordpress/?p=1776>`_


swagger
-------

- `How to using NGINX caching proxy with S3 « The Wowza Guru <http://thewowza.guru/how-to-using-nginx-caching-proxy-with-s3/>`_
- `Amazon S3 プロキシとしてのサンプル API の Swagger 定義 - Amazon API Gateway <http://docs.aws.amazon.com/ja_jp/apigateway/latest/developerguide/api-as-s3-proxy-export-swagger-with-extensions.html>`_
