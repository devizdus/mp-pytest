from re import Pattern

from playwright.sync_api import Locator, Page

from libs.pages.base_page import BasePage


class InfrastructuresPage(BasePage):
    def __init__(self, root: Page | Locator):
        super().__init__(root)

        self.btnAddInfrastructure = self.root.locator("[e2e-id=btnAddInfrastructure]")

        self.btnEditInfrastructure = self.root.locator("[e2e-id=btnEditInfrastructure]")

        self.btnDeleteInfrastructure = self.root.locator(
            "[e2e-id=btnDeleteInfrastructure]"
        )

    def get_list_option(self, name: str | Pattern[str]) -> Locator:
        return self.root.locator("[e2e-id=infrastructureListOption]", has_text=name)
