import unittest
from MenuManagement import MenuManagementPage

class TestMenuManagement(unittest.TestCase):
    def test_add_category_valid_input(self):
        app = MenuManagementPage()

        self.assertTrue(app.validate_add_category("Salad", "fruit"),
                        "It should be accepted because valid input is provided")

    def test_add_category_invalid_input(self):
        app = MenuManagementPage()

        self.assertFalse(app.validate_add_category(220, 66867),
                         "It should be rejected because invalid input is provided")

    def test_add_food_item_valid_input(self):
        app = MenuManagementPage()

        self.assertTrue(app.validate_add_food_item(1, "stake", "hot stake", 20, 2),
                        "It should be accepted because valid input is provided")

    def test_add_food_item_invalid_input(self):
        app = MenuManagementPage()

        self.assertFalse(app.validate_add_food_item("ok", "44", "55", "nice", "karim"),
                         "It should be rejected because invalid input is provided")

    def test_edit_category_valid_input(self):
        app = MenuManagementPage()

        self.assertTrue(app.validate_edit_category(1, "icecream", "vanilla icecream"),
                        "It should be accepted because valid input is provided")

    def test_edit_category_invalid_input(self):
        app = MenuManagementPage()

        self.assertFalse(app.validate_edit_category("1", 11, 12),
                         "It should be rejected because invalid input is provided")

    def test_edit_food_item_valid_input(self):
        app = MenuManagementPage()

        self.assertTrue(app.validate_edit_food_item(1, "44", "hotdog", "hot hot dog", "6", 2),
                        "It should be accepted because valid input is provided")

    def test_edit_food_item_invalid_input(self):
        app = MenuManagementPage()

        self.assertFalse(app.validate_edit_food_item("1", "hmm", "12", "44", "nice", "sc"),
                         "It should be rejected because invalid input is provided")

if __name__ == "__main__":
    unittest.main()
