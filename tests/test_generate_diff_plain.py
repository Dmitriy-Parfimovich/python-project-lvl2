import pytest
from gendiff.generate_diff import generate_diff


@pytest.fixture()
def input_filepaths1():
    file_path1 = 'tests/fixtures/file1_recur.json'
    return file_path1


@pytest.fixture()
def input_filepaths2():
    file_path2 = 'tests/fixtures/file2_recur.json'
    return file_path2


@pytest.fixture()
def output_generate_diff_test_plain():
    with open('tests/fixtures/generate_diff_test_plain.txt') as f:
        output_result = f.read()
    return output_result


def test_generate_diff_plain(input_filepaths1, input_filepaths2, output_generate_diff_test_plain):
    result = generate_diff(input_filepaths1, input_filepaths2, 'plain')
    assert result == output_generate_diff_test_plain
