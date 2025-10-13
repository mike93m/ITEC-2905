from unittest import TestCase
import area

class TestShapeAreas(TestCase):

    # Ensure the correct area is calculated for a triangle
    def test_triangle_area(self):
        self.assertEqual(area.triangle_area(10, 5), 25)
        
    # Test with floating point numbers
    def test_triangle_area_float(self):
        # Almost equal for floating point precision
        self.assertAlmostEqual(area.triangle_area(10.5, 4.2), 22.05)
        self.assertAlmostEqual(area.triangle_area(7.3, 3.8), 13.87)
        # Exact value test
        self.assertAlmostEqual(area.triangle_area(7.25, 4.91), 17.79875)

    # Test that negative base or height raises ValueError
    def test_triangle_area_negative_height_base_value_exception(self):
        with self.assertRaises(ValueError):
            area.triangle_area(-10, 5)
        with self.assertRaises(ValueError):
            area.triangle_area(10, -5)
        with self.assertRaises(ValueError):
            area.triangle_area(-10, -5)
    
    # Test that zero base or height returns zero area
    def test_triangle_area_zero_height_base(self):
        self.assertEqual(area.triangle_area(0, 5), 0)
        self.assertEqual(area.triangle_area(5, 0), 0)
        self.assertEqual(area.triangle_area(0, 0), 0)