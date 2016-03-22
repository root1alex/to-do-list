from unittest import skip
from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):

    @skip
    def test_cannot_add_empty_list_items(self):
        # Edith gos to the home page and accidentally tries to submit
        # an empty item. She hist Enter on the empty input box

        # The home page refreshes, and there is an error message saying
        # than list items cannot be blank

        # She tries again with some text for the item, which now works

        # Perversel, she now dices to submit a second blank list item

        # She recives a similar warning on the list page

        # And she can correct it by filling some text in
        self.fail('write me!')
