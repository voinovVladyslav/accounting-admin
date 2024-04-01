import pytest


@pytest.fixture(scope="session", autouse=True)
def configure_test_db() -> None:
    from django.conf import settings
    from django.db import connections

    del connections.__dict__["settings"]

    settings.DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": "test.sqlite3",
        }
    }

    connections._settings = connections.configure_settings(settings.DATABASES)
    connections["default"] = connections.create_connection("default")
