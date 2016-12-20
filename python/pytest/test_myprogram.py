# coding=utf-8
"""
pytest unit test code for the myprogram.py module.
"""
import os
import shutil

import pytest

import myprogram


class TestDoubleIt(object):
    """ pytest test suite class to test the myprogram module's doubleit() and doublelines() functions """
    numbers_file_template = 'nums_template.txt'
    numbers_file_testor = 'testnums.txt'

    def setup_class(self):
        """ TestSuite setup method to do test prep"""
        shutil.copy(TestDoubleIt.numbers_file_template, TestDoubleIt.numbers_file_testor)

    def teardown_class(self):
        """ TestSuite teardown method to clean up after tests"""
        os.remove(TestDoubleIt.numbers_file_testor)

    def test_doublelines(self):
        """ test doublelines() function """
        myprogram.doublelines(TestDoubleIt.numbers_file_testor)
        old_vals = [int(line) for line in open(TestDoubleIt.numbers_file_template)]
        new_vals = [int(line) for line in open(TestDoubleIt.numbers_file_testor)]
        for old_val, new_val in zip(old_vals, new_vals):
            assert int(new_val) == int(old_val) * 2

    def test_doubleit_value(self):
        """ test doubleit() basic behavior """
        assert myprogram.doubleit(10) == 20

    def test_doubleit_type(self):
        """ test doubleit() type safety """
        with pytest.raises(TypeError):
            myprogram.doubleit('hello')
