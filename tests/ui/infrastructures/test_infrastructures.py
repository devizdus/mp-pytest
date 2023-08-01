import pytest
from playwright.sync_api import Page, expect

from libs.pages import InfrastructuresPage


@pytest.fixture(autouse=True)
def prepare_page(self, page: Page):
    page.goto("/#/scanning/infrastructure/list")


def test_infrastructures_page_content(
    self, page: Page, infrastructures_page: InfrastructuresPage
):
    expect(page).to_have_title("Инфраструктура · MaxPatrol 10")
    expect(infrastructures_page.btnAddInfrastructure).to_be_visible()
    expect(infrastructures_page.btnEditInfrastructure).to_be_visible()
    expect(infrastructures_page.btnDeleteInfrastructure).to_be_visible()
    expect(infrastructures_page.get_list_option("Scope1")).to_be_visible()
