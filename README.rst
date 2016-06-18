Enya project
============

Containerized micro services example

Architecture
============




Testing it out
==============

The DB backend is postgres. Check the config.py for connection info.

Database name::

        enyadb

Database user and pw::
       
        dbadmin



RabbitMQ is an open source message broker software that implements the Advanced Message Queuing Protocol (AMQP).

Run the RabbitMQ server::

        docker run -d --hostname my-rabbit --name some-rabbit -p 15672:15672 -p 5672:5672 rabbitmq:3-management

Create the logger service::
        
        # Note that you have to enter your ip in the command below, example : 192.168.0.7
        docker run -d enya-logger nameko run logger --broker amqp://guest:guest@<your-ip>

Create the receiver service::

        # Note that you have to enter your ip in the command below, example : 192.168.0.7
        docker run -d enya-receiver nameko run receiver --broker amqp://guest:guest@<your-ip>


