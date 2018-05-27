import os, pytest

import grg_grgdata

import warnings

class TestCLI:
    def setup_method(self, _):
        """Parse a real network file"""
        self.parser = grg_grgdata.io.build_cli_parser()

        test_path = os.path.dirname(os.path.realpath(__file__))
        self.case_file = test_path+'/data/pglib/pglib_opf_case5_pjm.json'

    def test_view(self):
        args = self.parser.parse_args(['view', self.case_file])
        grg_grgdata.io.main(args)

    def test_smry(self):
        args = self.parser.parse_args(['smry', self.case_file])
        grg_grgdata.io.main(args)

