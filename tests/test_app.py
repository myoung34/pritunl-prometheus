#!/usr/bin/env python
import pytest
from unittest import mock
from app import create_app
from config import Config


class TestConfig(Config):
    MONGO_URI = "mongodb://mongo:27017/foo"

class foo():
    class db():
        class users():
            def count_documents(args, **kwargs):
                if 'disabled' in args and args['disabled']:
                    return 2
                return 4
        class clients():
            def count_documents(args, **kwargs):
                return 2

@pytest.fixture
def client():
    app = create_app(TestConfig)
    app.app_context().push()

    with app.test_client() as client:
        yield client


@mock.patch('app.main.routes.mongo', new=foo)
def test_metrics(
    client
):
    rv = client.get('/metrics')
    assert rv.data == b'''# HELP pritunl_disabled_users A summary of disabled pritunl users
# TYPE pritunl_disabled_users summary
pritunl_disabled_users_sum 1
pritunl_disabled_users_count 2
# HELP pritunl_online_users A summary of pritunl users
# TYPE pritunl_online_users summary
pritunl_online_users_sum 1
pritunl_online_users_count 2
# HELP pritunl_total_users A summary of pritunl users
# TYPE pritunl_total_users summary
pritunl_total_users_sum 1
pritunl_total_users_count 4'''
