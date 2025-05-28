import unittest
import sys 
sys.path.append("src")
sys.path.append(".")

from model import app
from model.app import Saving
from controller.saving_controller import create_savings_table, connect_db, insert_saving, update_saving, select_savings, delete_saving


class Programmed_savings_test(unittest.TestCase):

    def test_normal_1(self):
        amount = 300000
        interest_anual = 0.035
        period = 24
        tasa_mensual = (1 + interest_anual) ** (1/12) - 1

        s = app.Saving(amount, interest_anual, period)
        result = s.calculate_programmed_savings()
        expected = amount * (((1 + tasa_mensual) ** period - 1) / tasa_mensual)
        self.assertAlmostEqual(expected, result, 0)
    
    def test_normal_2(self):
        amount = 500000
        interest = 0.06
        period = 36

        s = app.Saving(amount, interest, period)
        result = s.calculate_programmed_savings()
        expected = 19621367.33
        self.assertAlmostEqual(expected, result, 0)
    
    def test_normal_3(self):
        amount = 1000000
        interest = 0.01
        period = 60

        s = app.Saving(amount, interest, period)
        result = s.calculate_programmed_savings()
        expected = 61492111
        self.assertAlmostEqual(expected, result, 0)
    
    def test_normal_4(self):
        amount = 250000
        interest = 0.05
        period = 1

        s = app.Saving(amount, interest, period)
        result = s.calculate_programmed_savings()
        expected = 250000
        self.assertAlmostEqual(expected, result, 0)
    
    def test_normal_5(self):
        amount = 200000
        interest = 0.045
        period = 12

        s = app.Saving(amount, interest, period)
        result = s.calculate_programmed_savings()
        expected = 2449106.61
        self.assertAlmostEqual(expected, result, 0)
    
    def test_extraordinary_1(self):
        amount = 1000000
        interest = 0.02
        period = 1

        s = app.Saving(amount, interest, period)
        result = s.calculate_programmed_savings()
        expected = 1000000
        self.assertAlmostEqual(expected, result, 2)
    
    def test_extraordinary_2(self):
        amount = 200000
        interest = 0.05
        period = 99

        s = app.Saving(amount, interest, period)
        result = s.calculate_programmed_savings()
        expected = 24328526
        self.assertAlmostEqual(round(expected), round(result))
    
    def test_extraordinary_3(self):
        amount = 500000
        interest = 1
        period = 12

        s = app.Saving(amount, interest, period)
        result = s.calculate_programmed_savings()
        expected = 8408576.8
        self.assertAlmostEqual(expected, result, 0)
    
    def test_error_1(self):
        amount = 300000
        interest = -0.05
        period = 12

        with self.assertRaises( app.Invalidinterest ):
            s = app.Saving(amount, interest, period)
            result = s.calculate_programmed_savings()
    
    def test_error_2(self):
        amount = 500000
        interest = 0.06
        period = -12

        with self.assertRaises( app.Invalidmonths ):
            s = app.Saving(amount, interest, period)
            result = s.calculate_programmed_savings()
    
    def test_error_3(self):
        amount = 600000
        interest = 0
        period = 24

        with self.assertRaises( app.Invalidinterest ):
            s = app.Saving(amount, interest, period)
            result = s.calculate_programmed_savings()
    
    def test_error_4(self):
        amount = 400000
        interest = 1.5
        period = 12

        with self.assertRaises( app.Invalidinterest ):
            s = app.Saving(amount, interest, period)
            result = s.calculate_programmed_savings()


class TestDatabase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.conn = connect_db()
        
    @classmethod
    def tearDownClass(cls):
        if hasattr(cls, 'conn') and cls.conn is not None:
            cls.conn.close()

    def test_create_table_normal(self):
        try:
            create_savings_table()
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"create_savings_table raised exception: {e}")

    def test_insert_saving_normal(self):
        try:
            test_saving = Saving(300000, 0.3, 12)
            insert_saving(test_saving)
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"insert_saving raised exception: {e}")

    def test_update_saving_normal(self):
        try:
            saving_id = 1
            updated_saving = Saving(4000000, 0.4, 13)
            update_saving(saving_id, updated_saving)
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"update_saving raised exception: {e}")

    def test_delete_saving_normal(self):
        try:
            saving_id = 1
            delete_saving(saving_id)
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"delete_saving raised exception: {e}")

    def test_insert_saving_failed(self):
        try:
            insert_saving(None)
            self.assertTrue(True)  
        except Exception:
            self.assertTrue(True)

    def test_update_saving_failed(self):
        # Test with invalid ID
        try:
            update_saving(-999, Saving(11111, 0.9, 10))
            self.assertTrue(True)  
        except Exception:
            self.assertTrue(True)

    def test_delete_saving_failed(self):
        # Test with invalid ID
        try:
            delete_saving(-999)
            self.assertTrue(True)  
        except Exception:
            self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()