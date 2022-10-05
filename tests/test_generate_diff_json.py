#from doctest import DocTest
import pytest
from gendiff.modules.generate_diff import generate_diff


@pytest.fixture()
def input_filepaths1_1():
    file_path1_1 = 'tests/fixtures/file1_1.json'
    return file_path1_1


@pytest.fixture()
def input_filepaths1_2():
    file_path1_2 = 'tests/fixtures/file1_2.json'
    return file_path1_2


@pytest.fixture()
def output_generate_diff_test1():
    with open('tests/fixtures/generate_diff_test1.txt') as f1:
        output_result1 = f1.read()
    return output_result1


@pytest.fixture()
def input_filepaths2_1():
    file_path2_1 = 'tests/fixtures/file2_1.json'
    return file_path2_1


@pytest.fixture()
def input_filepaths2_2():
    file_path2_2 = 'tests/fixtures/file2_2.json'
    return file_path2_2


@pytest.fixture()
def output_generate_diff_test2():
    with open('tests/fixtures/generate_diff_test2.txt') as f2:
        output_result2 = f2.read()
    return output_result2


def test_generate_diff1(input_filepaths1_1, input_filepaths1_2, output_generate_diff_test1):
    result = generate_diff(input_filepaths1_1, input_filepaths1_2)
    assert result == output_generate_diff_test1


def test_generate_diff2(input_filepaths2_1, input_filepaths2_2, output_generate_diff_test2):
    result = generate_diff(input_filepaths2_1, input_filepaths2_2)
    assert result == output_generate_diff_test2
