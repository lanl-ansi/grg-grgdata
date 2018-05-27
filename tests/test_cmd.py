import os, pytest

import grg_grgdata

import warnings

class TestFunctions:
    def setup_method(self, _):
        """Parse a real network file"""
        test_path = os.path.dirname(os.path.realpath(__file__))
        self.case = grg_grgdata.io.parse_grg_case_file(test_path+'/data/pglib/pglib_opf_case5_pjm.json')

    def test_001(self):
        comps = grg_grgdata.cmd.components_by_type(self.case)

        assert(len(comps) == 7)

        for comp_name in ['load', 'bus', 'generator', 'voltage_level', 'ac_line', 'substation', 'switch']:
            assert(comp_name in comps)

    def test_002(self):
        vlvp = grg_grgdata.cmd.voltage_level_by_voltage_point(self.case)

        assert(len(vlvp) == 25)

    def test_003(self):
        bvp = grg_grgdata.cmd.bus_voltage_points(self.case)

        assert(len(bvp) == 5)

    def test_004(self):
        vps = grg_grgdata.cmd.collapse_voltage_points(self.case)

        assert(len(vps) == 25)
        assert(min(vps.values()) == 0)
        assert(max(vps.values()) == 4)

    def test_005(self):
        avps = grg_grgdata.cmd.active_voltage_points(self.case)

        assert(len(avps) == 5)

    # not clear if this function is working
    # def test_006(self):
    #     ivps = grg_grgdata.cmd.isolated_voltage_points(self.case)

    #     print(ivps)
    #     assert(len(ivps) == 0)


class TestCLI:
    def setup_method(self, _):
        """Parse a real network file"""
        self.parser = grg_grgdata.cmd.build_cli_parser()

        test_path = os.path.dirname(os.path.realpath(__file__))
        self.case_file = test_path+'/data/pglib/pglib_opf_case5_pjm.json'

    def test_validate(self):
        args = self.parser.parse_args([self.case_file])
        grg_grgdata.cmd.main(args)


