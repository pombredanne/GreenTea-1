HOW TO INSTALL
==============

At first you need installed repositories (rhel/fedora + epel) which containt following packages.

.. parsed-literal::
   python-psycopg2 gitweb-caching source-highlight highlight libxslt-devel libxml2-devel 
   graphviz-devel python-virtualenv beaker-common beaker-client gcc
   
All needed packages are written in file requirement/rpms-basic.txt. 

.. parsed-literal::

   >> cat requirement/rpms-basic.txt | xargs yum install -y

Create project directory and clone git repositore to them.

.. parsed-literal::

   >> git clone https://github.com/SatelliteQE/GreenTea.git


Now we install virtual envinroment. 

.. parsed-literal::
   >> virtualenv env


Install necessary python packages 

.. parsed-literal::
  >> source env/bin/activate
  >> pip install -r requirement/requirement.txt


Project uses sqlite as default database. The database was created when you run this script:

.. parsed-literal::
   >> python manage.py syncdb
   >> python manage.py migrate

Or you can set own database.

For testing/developing it's possible to use django http server and sqlite database 

.. parsed-literal::
   >> python manage.py runserver
  
Docker
------
Public container is avalable on folowing site https://hub.docker.com/r/pajinek/greentea/

.. parsed-literal::

  >> docker pull pajinek/greentea
  >> docker run -i -t -p 80:8000 pajinek/greentea

Administration 
--------------

Green Tea is posible to manage by following script (not as superuser)

.. parsed-literal::
   >> python manage.py 


for WebUI administration, at first you need create new user

.. parsed-literal::
  >> python manage.py createsuperuser


Uwsgi and Httpd
-----------------------------------

.. parsed-literal::

   >> httpd uwsgi-plugin-common mod_proxy_uwsgi
