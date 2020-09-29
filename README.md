# Apache Airflow: Complete Hands-On Beginner to Advanced Class

This repository hold the source code for the Udemy online course [Apache Airflow: Complete Hands-On Beginner to Advanced Class](https://www.udemy.com/course/apache-airflow-course/?referralCode=7A7192D2BDE0A30803F8) by Alexandra Abbas.

## Intsall Apache Airflow

As explained in the course before meking use of this code base you need to install Apache Airflow locally on your machine.

```Bash
pip install apache-airflow[gcp,statsd,sentry]==1.10.10
```

Install these extra packages as well.

```Bash
pip install cryptography==2.9.2
pip install pyspark==2.4.5
```

To validate your Airflow installation check your Airflow version. This should print 1.10.10.

```Bash
airflow version
```

If you have installed Airflow earlier you might get a DeprecationWarning about having multiple airflow.cfg files but that’s okay as long as you set the correct AIRFLOW_HOME environment variable in your Terminal.

# Initialise an Airflow environment

As a next step you need to initialise an Airflow environment locally to run DAGs.

Set the AIRFLOW_HOME variable.

```Bash
export AIRFLOW_HOME=path/to/this/directory
```

Initialise Airflow and the metadata database.

```Bash
airflow initdb
```

Now, you can run both the web server and the scheduler.

Run the web server.

```Bash
airflow webserver
```

In a different terminal window/session where you set the AIRFLOW_HOME variable again run the scheduler.

```Bash
airflow scheduler
```

Great!🎉 Now you can access the Airflow web UI on http://localhost:8080.
