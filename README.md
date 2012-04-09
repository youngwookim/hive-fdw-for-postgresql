Hive FDW for PostgreSQL
===============================

This Python module implements the `multicorn.ForeignDataWrapper` interface to allow you to create foreign tables in PostgreSQL 9.1+ that query to tables in Apache Hive. 

Pre-requisites
--------------

* [PostgreSQL 9.1+](http://www.postgresql.org/)
* [Python](http://python.org/)
* [Multicorn](http://multicorn.org)
* [ls-thrift-py-hadoop] (https://github.com/lovelysystems/ls-thrift-py-hadoop)

Installation
------------

1. [Install Multicorn](http://multicorn.org/#installation)
2. Build the FDW module:

        $ cd hive-fdw-for-postgresql
        $ python setup.py sdist
        $ sudo python setup.py install

    or, with easy_install:

        $ cd hive-fdw-for-postgresql
        $ sudo easy_install .

3. In the PostgreSQL client, create an extension and foreign server:


        CREATE EXTENSION multicorn;
        CREATE SERVER multicorn_hive FOREIGN DATA WRAPPER multicorn
        OPTIONS (
            wrapper 'hivefdw.HiveForeignDataWrapper'
        );

        CREATE FOREIGN TABLE hive (
            a varchar,
            b varchar,
            c varchar,
            d varchar
        ) SERVER multicorn_hive OPTIONS (
            host 'tb081',
            port '10000',
            table 'test'
        );

        SELECT * FROM hive;
