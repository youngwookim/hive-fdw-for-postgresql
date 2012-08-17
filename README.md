Hive FDW for PostgreSQL
===============================

This Python module implements the `multicorn.ForeignDataWrapper` interface to allow you to create foreign tables in PostgreSQL 9.1+ that query to tables in Apache Hive. 

Pre-requisites
--------------

* [PostgreSQL 9.1+](http://www.postgresql.org/)
* [Python](http://python.org/)
* [Multicorn](http://multicorn.org)
* [hive-thrift-py](https://github.com/youngwookim/hive-thrift-py)

Installation
------------

1. [Install Multicorn](http://multicorn.org/#installation)
2. [Install hive-thrift-py](https://github.com/youngwookim/hive-thrift-py)
3. Build the FDW module:

        $ cd hive-fdw-for-postgresql
        $ python setup.py sdist
        $ sudo python setup.py install

    or, with easy_install:

        $ cd hive-fdw-for-postgresql
        $ sudo easy_install .

4. In the PostgreSQL client, create an extension and foreign server:

        CREATE EXTENSION multicorn;
        
        CREATE SERVER multicorn_hive FOREIGN DATA WRAPPER multicorn
        OPTIONS (
            wrapper 'hivefdw.HiveForeignDataWrapper'
        );

Examples
------------

1. User can executes simple selects on a remote Hive table:

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

2. Also user can executes selects using a Hive query:
         
        CREATE FOREIGN TABLE hive_query (
            x varchar,
            y varchar,
            z varchar
        ) SERVER multicorn_hive OPTIONS (
            host 'tb081',
            port '10000',
            query 'SELECT x,y,z from src'
        );
        
        SELECT * from hive_query;
