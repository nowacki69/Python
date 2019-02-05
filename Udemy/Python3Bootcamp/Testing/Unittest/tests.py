import unittest
from activities import eat, nap, is_funny, laugh

class ActivityTests(unittest.TestCase):
    def test_eat_healthy(self):
        """Testing is_healthy == True """
        self.assertEqual(eat("broccoli", is_healthy=True),
                         "I'm eating broccoli, because my body is a temple."
                        )

    def test_eat_healthy_unhealthy(self):
        """Testing is_healthy not True """
        self.assertEqual(
                        eat("pizza", is_healthy=False),
                        "I'm eating pizza, because YOLO"
                        )


    def test_eat_unhealth_boolean(self):
        """is_healthy must be a boolean """
        with self.assertRaises(ValueError):
            eat("pizza", is_healthy="who cares?")


    def test_short_nap(self):
        """ Testing for short nap """
        self.assertEqual(nap(1),
                        "I'm feeling refreshed after my 1 hour nap")


    def test_long_nap(self):
        """ Testing for long nap """
        self.assertEqual(nap(3),
                        "Ugh, I overslept. I didn't mean to nap for 3 hours")


    def test_is_funny_tim(self):
        self.assertEqual(is_funny("tim"), False)
        # self.assertFalse(is_funny("tim"), "tim should not be funny.")


    def test_is_anyone_else(self):
        """Anyone other than tim should be funny """
        self.assertTrue(is_funny("blue"), "blue should be funny")
        self.assertTrue(is_funny("tammy"), "tammy should be funny")
        self.assertTrue(is_funny("sven"), "sven should be funny")


    def test_laugh(self):
        self.assertIn(laugh(), ('lol', 'haha', 'tehehe'))


if __name__ == "__main__":
    unittest.main()
