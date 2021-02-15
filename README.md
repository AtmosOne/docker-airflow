# **Airflow researh**

Source of fork: [dockerized apache airflow](https://github.com/puckel/docker-airflow)

During my career i achieved the problem when, i can't manage my data pipeline/automated business processes implemented on python scripts. So, I want to utilize Apache Airflow as a process management tool in my technological stack. But before that, let's test it's opportunity in practice

## 1. **Installation**

Pull the image from the Docker repository.

```bash
docker pull puckel/docker-airflow
```

## 2. **Usage**

**Start LocalExecutor**:
```bash
docker-compose -f docker-compose-LocalExecutor.yml up -d
```

**Stop LocalExecutor**:
```bash
docker-compose -f docker-compose-LocalExecutor.yml down
```

If you want to use Ad hoc query, make sure you've configured connections:
Go to Admin -> Connections and Edit "postgres_default" set this values (equivalent to values in airflow.cfg/docker-compose*.yml):

- Host : postgres
- Schema : airflow
- Login : airflow
- Password : airflow

## 3. **Configuring Airflow**

It's possible to set any configuration value for Airflow from environment variables, which are used over values from the airflow.cfg.

The general rule is the environment variable should be named `AIRFLOW__<section>__<key>`, for example `AIRFLOW__CORE__SQL_ALCHEMY_CONN` sets the `sql_alchemy_conn` config option in the `[core]` section.

Check out the [Airflow documentation](http://airflow.readthedocs.io/en/latest/howto/set-config.html#setting-configuration-options) for more details

You can also define connections via environment variables by prefixing them with `AIRFLOW_CONN_` - for example `AIRFLOW_CONN_POSTGRES_MASTER=postgres://user:password@localhost:5432/master` for a connection called "postgres_master". The value is parsed as a URI. This will work for hooks etc, but won't show up in the "Ad-hoc Query" section unless an (empty) connection is also created in the DB

## 4. **Custom Airflow plugins**

Airflow allows for custom user-created plugins which are typically found in `${AIRFLOW_HOME}/plugins` folder. Documentation on plugins can be found [here](https://airflow.apache.org/plugins.html)

In order to incorporate plugins into your docker container
- Create the plugins folders `plugins/` with your custom plugins.
- Mount the folder as a volume by doing either of the following:
    - Include the folder as a volume in command-line `-v $(pwd)/plugins/:/usr/local/airflow/plugins`
    - Use docker-compose-LocalExecutor.yml or docker-compose-CeleryExecutor.yml which contains support for adding the plugins folder as a volume

## 5. **Install custom python package**

- Create a file "requirements.txt" with the desired python modules
- Mount this file as a volume `-v $(pwd)/requirements.txt:/requirements.txt` (or add it as a volume in docker-compose file)
- The entrypoint.sh script execute the pip install command (with --user option)

## 6. **UI Links**

- Airflow: [localhost:8080](http://localhost:8080/)
- Flower: [localhost:5555](http://localhost:5555/)

