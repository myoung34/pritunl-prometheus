Pritunl Prometheus
==================

A simple flask app to generate pritunl metrics and expose it via a `/metrics` endpoint.


```
$ curl pritunl-metrics.service.consul:3000/metrics
# HELP pritunl_disabled_users A summary of disabled pritunl users
# TYPE pritunl_disabled_users summary
pritunl_disabled_users_sum 1
pritunl_disabled_users_count 1
# HELP pritunl_online_users A summary of pritunl users
# TYPE pritunl_online_users summary
pritunl_online_users_sum 1
pritunl_online_users_count 1
# HELP pritunl_total_users A summary of pritunl users
# TYPE pritunl_total_users summary
pritunl_total_users_sum 1
pritunl_total_users_count 2
```

## Development ##

### Running Locally ###

Data is seeded into mongo from the `mongo-seed/*.js` files


```
$ docker-compose up --build
$ curl localhost:3000/metrics
# HELP pritunl_disabled_users A summary of disabled pritunl users
# TYPE pritunl_disabled_users summary
pritunl_disabled_users_sum 1
pritunl_disabled_users_count 1
# HELP pritunl_online_users A summary of pritunl users
# TYPE pritunl_online_users summary
pritunl_online_users_sum 1
pritunl_online_users_count 1
# HELP pritunl_total_users A summary of pritunl users
# TYPE pritunl_total_users summary
pritunl_total_users_sum 1
pritunl_total_users_count 2
```

### Tests ###

```
$ poetry install
$ poetry run tox
```
