# unit-test-in-VS-code
Unit test is working in VS Code
This program works in only visual code.
Clone this repository and then run with:
python3 test_calculator.py
Unit test will be done only on the file name that starts with test and also on methods, those starts with test_
assert is nothing but checks.
asserEqual checks the output of the method with the value we give after comma
Ex:
def test_subtraction(self):
        self.assertEqual(calculator.subtraction(8, 2), 6)
 Here asserEqual checks (8-2=6) value is whether equal to the value after comma(,) Here 6
 If they both matches then it gives OK
 ==========
 In Unit test what happens is unit test will create objects for our class automatically. For each method it will create one object separately, so every method will be tested in isolation.
 So that if tehre are any errors it will throw error by mentioning that particular method. So that it is easy to identify the errors.
 That's why it is called Unit testing.
===============
unittest does not enforce whether a test is unit or integration. It simply executes the test methods you define.
Whether you are doing unit testing or integration testing depends on:
What you are testing (individual vs. combined components).
How you isolate dependencies (e.g., using mocks for unit tests).
===============
Yes, that's correct! Just like pytest, the unittest module in Python can also be used for both unit testing and integration testing. The distinction depends on how you write the tests, not the testing framework itself.
===============
Yes, pytest and unittest are both testing frameworks specifically designed for Python.
==============
The trend in the Python testing ecosystem has shifted strongly in favor of pytest in recent years. While unittest is still widely used, pytest has become the most popular framework for Python testing due to its flexibility, simplicity, and rich feature set.
=============
