import os
from typing import Literal

import pytest
from dotenv import load_dotenv
from playwright.sync_api import Browser

pytest_plugins = ("libs.fixtures.pages", "libs.fixtures.components")


def pytest_configure(config: pytest.Config):
    load_dotenv(verbose=True)


@pytest.fixture(scope="session", autouse=True)
def browser_context_args(browser_context_args, base_url: str, storage_state: dict):
    return {
        **browser_context_args,
        "ignore_https_errors": True,
        "base_url": base_url,
        "viewport": {
            "width": 1920,
            "height": 1080,
        },
        "storage_state": storage_state,
    }


@pytest.fixture(scope="session", autouse=True)
def storage_state(browser: Browser, base_url: str, credentials: dict):
    context = browser.new_context(base_url=base_url)

    page = context.new_page()
    page.goto("/#/authorization/login")

    page.fill("input[e2e-id=inputLogin]", credentials["login"])
    page.fill("input[e2e-id=inputPassword]", credentials["password"])
    page.click("button[e2e-id=btnLogin]")

    storage_state = context.storage_state()

    context.close()

    return storage_state


@pytest.fixture(scope="session")
def base_url() -> str:
    return os.environ.get("PYTEST_BASE_URL") or "http://localhost:4200"


@pytest.fixture(scope="session")
def credentials() -> dict[Literal["login", "password"], str]:
    return {"login": "Bobcat", "password": "admin"}
