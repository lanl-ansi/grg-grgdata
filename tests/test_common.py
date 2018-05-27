import os, pytest

import grg_grgdata

import warnings

class TestFunctions:
    def setup_method(self, _):
        """Parse a real network file"""
        test_path = os.path.dirname(os.path.realpath(__file__))
        self.case = grg_grgdata.io.parse_grg_case_file(test_path+'/data/pglib/pglib_opf_case14_ieee.json')
        self.ac_line = self.case['network']['components']['line_01']
        self.transformer = self.case['network']['components']['substation_04']['substation_components']['transformer_01']

    # TODO, update to a case that has has_current_limits
    def test_001(self):
        if grg_grgdata.common.has_current_limits(self.ac_line):
            rate_a, rate_b, rate_c = grg_grgdata.common.get_current_rates(self.ac_line)
            assert(rate_a == 1.0)
            assert(rate_b == 1.0)
            assert(rate_c == 1.0)

            ml = grg_grgdata.common.max_limit(self.ac_line['current_limits_1'], 100)
            assert(ml == 1.0)

    def test_002(self):
        if grg_grgdata.common.has_thermal_limits(self.ac_line):
            rate_a, rate_b, rate_c = grg_grgdata.common.get_thermal_rates(self.ac_line)
            assert(rate_a == 4.72)
            assert(rate_b == 4.72)
            assert(rate_c == 4.72)

            ml = grg_grgdata.common.max_limit(self.ac_line['thermal_limits_1'], 100)
            assert(ml == 4.72)

    def test_003(self):
        setting = grg_grgdata.common.tap_setting(self.transformer['tap_changer'], 0)

        assert(len(setting) == 5)
        assert(setting['position'] == 0)
        assert(len(setting['impedance']) == 2)
        assert(len(setting['shunt']) == 2)
        assert(setting['tap_ratio'] == 0.978)
        assert(setting['angle_shift'] == 0.0)


    # def test_004(self):
    #     vps = grg_grgdata.cmd.collapse_voltage_points(self.case)

    #     assert(len(vps) == 25)
    #     assert(min(vps.values()) == 0)
    #     assert(max(vps.values()) == 4)

    # def test_005(self):
    #     avps = grg_grgdata.cmd.active_voltage_points(self.case)

    #     assert(len(avps) == 5)

    # not clear if this function is working
    # def test_006(self):
    #     ivps = grg_grgdata.cmd.isolated_voltage_points(self.case)

    #     print(ivps)
    #     assert(len(ivps) == 0)
