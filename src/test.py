from main import calculate_owed, calculate_total, output, parse_input, Person
import unittest


class Test(unittest.TestCase):
    def test_parse_input(self):
        self.assertEqual(parse_input("John;50"), Person(name="John", payed=50))
        self.assertEqual(parse_input("James;23.5"), Person(name="James", payed=23.5))
        self.assertEqual(parse_input("J;0"), Person(name="J", payed=0))
        self.assertEqual(parse_input("J.;0.0"), Person(name="J.", payed=0))

        self.assertEqual(parse_input(""), None)
        self.assertEqual(parse_input("James"), None)
        self.assertEqual(parse_input("0"), None)
        self.assertEqual(parse_input(";"), None)
        self.assertEqual(parse_input(";;"), None)
        self.assertEqual(parse_input("J;"), None)
        self.assertEqual(parse_input(";0"), None)
        self.assertEqual(parse_input("James;50;"), None)
        self.assertEqual(parse_input(";James;50"), None)
        self.assertEqual(parse_input(";James;50;"), None)

    def test_calculate_total(self):
        people = [
            Person(name="J", payed=100, owes=50),
            Person(name="K", payed=150, owes=0),
            Person(name="L", payed=200, owes=-50),
        ]
        self.assertEqual(calculate_total(people), 450)

    def test_calculate_owed(self):
        self.assertEqual(
            calculate_owed([Person(name="J", payed=50)]),
            [Person(name="J", payed=50, owes=0)],
        )
        self.assertEqual(
            calculate_owed([Person(name="J", payed=50), Person(name="K", payed=100)]),
            [
                Person(name="J", payed=50, owes=25),
                Person(name="K", payed=100, owes=-25),
            ],
        )
        self.assertEqual(
            calculate_owed(
                [
                    Person(name="J", payed=100),
                    Person(name="K", payed=150),
                    Person(name="L", payed=200),
                ]
            ),
            [
                Person(name="J", payed=100, owes=50),
                Person(name="K", payed=150, owes=0),
                Person(name="L", payed=200, owes=-50),
            ],
        )

    def test_output(self):
        people = [
            Person(name="J", payed=100, owes=50),
            Person(name="K", payed=150, owes=0),
            Person(name="L", payed=200, owes=-50),
        ]
        self.assertEqual(
            output(people),
            "\nTotal: 450\n---------------\nJ: 50\nK: 0\nL: -50\n",
        )


if __name__ == "__main__":
    unittest.main()
