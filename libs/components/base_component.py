from playwright.sync_api import Locator, Page


class BaseComponent:
    def __init__(self, root: Page | Locator):
        self.root = root if isinstance(root, Locator) else root.locator("body")
        self.page = self.root.page
