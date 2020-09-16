from persistence.db_read import see_people
import pytest
from mock import Mock


def people_function():
    people_result=see_people()
    return people_result

def test_menu_function_mocked_main_menu (mocker):
    mocker.patch('persistence.db_read.see_people', return_value= 9)
    expected= 9
    
    actual = see_people()
    assert expected == actual

