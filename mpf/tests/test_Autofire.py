from unittest.mock import MagicMock

from mpf.platforms.interfaces.driver_platform_interface import PulseSettings

from mpf.core.platform import SwitchSettings, DriverSettings

from mpf.tests.MpfTestCase import MpfTestCase


class TestAutofire(MpfTestCase):
    def getConfigFile(self):
        return 'config.yaml'

    def getMachinePath(self):
        return 'tests/machine_files/autofire/'

    def test_hw_rule_pulse(self):
        self.machine.default_platform.set_pulse_on_hit_rule = MagicMock()
        self.machine.autofires.ac_test.enable()

        self.machine.default_platform.set_pulse_on_hit_rule.assert_called_once_with(
            SwitchSettings(hw_switch=self.machine.switches.s_test.hw_switch, invert=False, debounce=False),
            DriverSettings(hw_driver=self.machine.coils.c_test.hw_driver,
                           pulse_settings=PulseSettings(power=1.0, duration=23), hold_settings=None, recycle=True)
        )

        self.machine.default_platform.clear_hw_rule = MagicMock()
        self.machine.autofires.ac_test.disable()

        self.machine.default_platform.clear_hw_rule.assert_called_once_with(
            SwitchSettings(hw_switch=self.machine.switches.s_test.hw_switch, invert=False, debounce=False),
            DriverSettings(hw_driver=self.machine.coils.c_test.hw_driver,
                           pulse_settings=PulseSettings(power=1.0, duration=23), hold_settings=None, recycle=True))

    def test_hw_rule_pulse_inverted_switch(self):
        self.machine.default_platform.set_pulse_on_hit_rule = MagicMock()
        self.machine.autofires.ac_test_inverted.enable()

        self.machine.default_platform.set_pulse_on_hit_rule.assert_called_once_with(
            SwitchSettings(hw_switch=self.machine.switches.s_test_nc.hw_switch, invert=True, debounce=False),
            DriverSettings(hw_driver=self.machine.coils.c_test2.hw_driver,
                           pulse_settings=PulseSettings(power=1.0, duration=23), hold_settings=None, recycle=True)
        )

        self.machine.default_platform.clear_hw_rule = MagicMock()
        self.machine.autofires.ac_test_inverted.disable()

        self.machine.default_platform.clear_hw_rule.assert_called_once_with(
            SwitchSettings(hw_switch=self.machine.switches.s_test_nc.hw_switch, invert=True, debounce=False),
            DriverSettings(hw_driver=self.machine.coils.c_test2.hw_driver,
                           pulse_settings=PulseSettings(power=1.0, duration=23), hold_settings=None, recycle=True))

    def test_hw_rule_pulse_inverted_autofire(self):
        self.machine.default_platform.set_pulse_on_hit_rule = MagicMock()
        self.machine.autofires.ac_test_inverted2.enable()

        self.machine.default_platform.set_pulse_on_hit_rule.assert_called_once_with(
            SwitchSettings(hw_switch=self.machine.switches.s_test.hw_switch, invert=True, debounce=False),
            DriverSettings(hw_driver=self.machine.coils.c_test2.hw_driver,
                           pulse_settings=PulseSettings(power=1.0, duration=23), hold_settings=None, recycle=True)
        )

        self.machine.default_platform.clear_hw_rule = MagicMock()
        self.machine.autofires.ac_test_inverted2.disable()

        self.machine.default_platform.clear_hw_rule.assert_called_once_with(
            SwitchSettings(hw_switch=self.machine.switches.s_test.hw_switch, invert=True, debounce=False),
            DriverSettings(hw_driver=self.machine.coils.c_test2.hw_driver,
                           pulse_settings=PulseSettings(power=1.0, duration=23), hold_settings=None, recycle=True))
