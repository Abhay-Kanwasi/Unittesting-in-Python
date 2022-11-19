import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    def test_email(self):
        emp_1 = Employee('Abhay','Kanwasi',120000)
        emp_2 = Employee('Abhay','Bhardwaj',120000)

        self.assertEqual(emp_1.email, 'AbhayKanwasi@email.com')
        self.assertEqual(emp_2.email, 'AbhayBhardwaj@email.com')

        emp_1.first = 'Rajat'
        emp_2.first = 'Abhishek'

        self.assertEqual(emp_1.email,'RajatKanwasi@email.com')
        self.assertEqual(emp_2.email,'AbhishekBhardwaj@email.com')
    
    def test_fullname(self):
        emp_1 = Employee('Anubhav','Sharma',128000)
        emp_2 = Employee('Ajay','Sharma',232300)

        self.assertEqual(emp_1.full_name,'Anubhav Sharma')
        self.assertEqual(emp_2.full_name,'Ajay Sharma')

        emp_1.first = 'Abhay'
        emp_1.last = 'Kanwasi'
        self.assertEqual(emp_1.full_name,'Abhay Kanwasi')

        emp_2.first = 'Rajat'
        emp_2.last = 'Sirswal'
        self.assertEqual(emp_2.full_name,'Rajat Sirswal')
    
    def test_apply_raise(self):
        emp_1 = Employee('Corey','Jonson',120000)
        emp_2 = Employee('David','Anderson',130090)

        emp_1.apply_raise()
        emp_2.apply_raise()

        self.assertEqual(emp_1.pay,126000)
        self.assertEqual(emp_2.pay,136594)

if __name__ == "__main__":
    unittest.main()

