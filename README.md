PES
===

Progress Evaluation System - A system for students/employees and teachers/managers to evaluate the progress of the undergoing assignments/projects. 

Installation guide
==================

Step 1: 
======
Install Python pip. 

```
sudo apt-get install python-pip

```

Step 2: 
=======

Install and Create a virtual environment and activate it. 

```
pip install virtualenv 

```
or 

```
sudo apt-get install python-virtualenv

```

```
virtualenv name_of_your_virtualenv

source name_of_your_virtualenv/bin/activate

```

Step 3: 
======

Install requirements for the project. 

``` 
pip install -r requirements.txt

```

Step 4:
=======

Run the project. 

Inside pes directory:

```
python manage.py runserver [port_no]

```

Thanks!
