Enya project
============

Containerized micro services example.

Inspired by http://brunorocha.org/python/microservices-with-python-rabbitmq-and-nameko.html

Architecture
============

.. image:: enya_arch.png



Testing it out
==============

Create virtualenv in root of folder::
        
        virtualenv venv

Activate the environment::

        source venv/bin/activate

install the Python packages::

        pip install -r requirements.txt


The DB backend is postgres. Check the config.py for connection info.

Database name::

        enyadb

Database user and pw::
       
        dbadmin

Assuming you have postgresql installed::
        
        adduser dbadmin
        passwd dbadmin
        <password> : dbadmin
        sudo su - postgres
        psql
        CREATE USER dbadmin with PASSWORD 'dbadmin';
        CREATE DATABASE enyadb;
        GRANT ALL PRIVILEGES ON DATABASE enyadb to dbadmin;
        \q

Set up the DB tables etc::

        python manage.py db init
        python manage.py db migrate
        python manage.py db upgrade

Create API user::

        python create_db_admin.py

Run the REST api server::

        python app.py

RabbitMQ is an open source message broker software that implements the Advanced Message Queuing Protocol (AMQP).

Run the RabbitMQ server::

        docker run -d --hostname my-rabbit --name some-rabbit -p 15672:15672 -p 5672:5672 rabbitmq:3-management

Create the logger service::
        
        # Note that you have to enter your ip in the command below, example : 192.168.0.7
        docker run -d enya-logger nameko run logger --broker amqp://guest:guest@<your-ip>

Create the receiver service::

        # Note that you have to enter your ip in the command below, example : 192.168.0.7
        docker run -d enya-receiver nameko run receiver --broker amqp://guest:guest@<your-ip>

Finally, sending some data to the API server that will perform RPC calls to log the data::

        curl -u enya:secret -X POST -d "data=This is some test data" http://localhost:5000/api/dump

Checking that it actually worked::

        docker exec -it <logger container> cat data.log

        2016-06-18 21:46:56 This is some test data



