import unittest
from gun import Gun


class TestGun(unittest.TestCase):
    def test_that_magazine_is_empty_from_initial_state(self):
        gun1 = Gun(0, True)
        self.assertTrue(gun1.check_empty)

    def test_reload_adds_bullets_to_magazine_magazine_is_not_empty(self):
        gun1 = Gun(0, True)
        gun1.reload()
        self.assertEqual(1, gun1.check_magazine())
        gun1.reload()
        self.assertEqual(2, gun1.check_magazine())

    def test_reload_bullet_shoot_bullet_magazine_is_empty(self):
        gun1 = Gun(0, True)
        gun1.reload()
        self.assertEqual(1, gun1.check_magazine())
        gun1.shoot()
        self.assertEqual(0, gun1.check_magazine())

    def test_reload_bullet_beyond_max_magazine_contains_five_bullets(self):
        gun1 = Gun(0, True)
        for count in range(1, 8):
            gun1.reload()
        self.assertEqual(5, gun1.check_magazine())

    def test_shoot_empty_gun_raise_error(self):
        gun1 = Gun(0, True)
        self.assertEqual(None, gun1.shoot())

    def test_replace_magazine_bullets_are_five(self):
        gun1 = Gun(0, True)
        gun1.replace_magazine()
        self.assertEqual(5, gun1.check_magazine())