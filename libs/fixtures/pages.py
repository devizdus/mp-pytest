import pytest
from playwright.sync_api import Page

from libs.pages.infrastructures.infrastructures import InfrastructuresPage


@pytest.fixture()
def infrastructures_page(page: Page):
    return InfrastructuresPage(page)
