import pytest
import commandline

def test_single_id():
    args = commandline.parse(['--id', 'xy-22'])
    assert args['id'] == ['xy-22']  


def test_multiple_ids():
    args = commandline.parse(['--id', 'xy-22', 'zz-11', 'xyz-101'])
    assert args['id'] == ['xy-22', 'zz-11', 'xyz-101']


