import os, pytest

import grg_grgdata

import warnings

grg_files = []

for wd, directory, files in os.walk(os.path.dirname(os.path.realpath(__file__))+'/data/'):
    for file in files:
        if file.endswith('.json'):
            grg_files.append(wd+'/'+file)
del wd, directory, files


@pytest.mark.parametrize('input_data', grg_files)
def test_valid(input_data):
    # lets be extra strick and flag warnings here as well
    #warnings.filterwarnings('error')

    case = grg_grgdata.io.parse_grg_case_file(input_data)
    assert grg_grgdata.cmd.validate_grg(case)

    # need to set warnings back to default
    # otherwise tests using pytest.warns will fail
    #warnings.resetwarnings()


@pytest.mark.parametrize('input_data', grg_files)
def test_parameters(input_data):
    # lets be extra strick and flag warnings here as well
    #warnings.filterwarnings('error')

    case = grg_grgdata.io.parse_grg_case_file(input_data)
    if grg_grgdata.cmd.validate_grg(case):
        grg_grgdata.cmd.validate_grg_parameters(case)
    else:
        assert False # invalid case

    # need to set warnings back to default
    # otherwise tests using pytest.warns will fail
    #warnings.resetwarnings()