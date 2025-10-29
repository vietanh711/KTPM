import unittest
from hw1_fixed import choose

class TestHW1(unittest.TestCase):
    def test_main(self):
        test_cases = [
            ("P1", (0, 3, 3), "Lỗi input"),
            ("P2", (25, 3, 3), "Lỗi input"),
            ("P3", (27, 6.5, 4.5), "Thả bạch tuộc"),
            ("P4", (25, 5.5, 4.5), "Thả cá"),
            ("P5", (23, 6, 5), "Không thả gì"),
            ("P6", (27, 5.5, 4.5), "Thả cá"),
            ("P7", (25, 4.2, 2), "Không thả gì"),
            ("P8", (25, 4, 3), "Thả tôm"),
            ("P9", (27, 6.5, 3), "Thả tôm"),
            ("P10", (25, 5.5, 3), "Thả tôm"),
            ("P11", (25, 5.5, 2), "Không thả gì"),
        ]



        for case_id, args, expected in test_cases:
            with self.subTest(case=case_id, args=args):
                self.assertEqual(choose(*args), expected, msg=f"expected: {expected}, actual: {choose(*args)} in test case {case_id}")

if __name__ == "__main__":
    unittest.main()