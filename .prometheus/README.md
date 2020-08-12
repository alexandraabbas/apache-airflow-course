# Monitor Airflow with StatsD, Prometheus and Grafana

This is the source code for the lecture Monitor Airflow with StatsD, Prometheus and Grafana in Section 8: Airflow in Production.

Make sure you're in the `.prometheus/` directory while running these commands. We're using Docker to run these services so make sure you have Docker installed.

## Run statsd-exporter

This command configures statsd-exporter to listen for metrics sent on port 8125. It converts Statsd metrics to Prometheus format using the mapping.yml configuration file. It exposes metrics for Prometheus to scrape over host port 9123 and container port 9102.

```Bash
docker run --name=prom-statsd-exporter \
    -p 9123:9102 \
    -p 8125:8125/udp \
    -v $PWD/mapping.yml:/tmp/mapping.yml \
    prom/statsd-exporter \
        --statsd.mapping-config=/tmp/mapping.yml \
        --statsd.listen-udp=:8125 \
        --web.listen-address=:9102
```

## Run Prometheus

This command runs Prometherus and configures it to scrape metrics exposed on port 9123. It allows Grafana to use Prometheus as a data source over address port 9090.

```Bash
docker run --name=prometheus \
    -p 9090:9090 \
    -v $PWD/prometheus.yml:/prometheus.yml \
    prom/prometheus \
        --config.file=/prometheus.yml \
        --log.level=debug \
        --web.listen-address=:9090 \
        --web.page-title='Prometheus - Airflow Demo'
```

Now you can access the Prometheus web UI on http://localhost:9090.

## Run Grafana

```Bash
docker run -d --name=grafana -p 3000:3000 grafana/grafana
```

Now you can access the Grafana web UI on http://localhost:3000.

Follow the lecture to configure Prometheus as a data source in the Grafana UI.
