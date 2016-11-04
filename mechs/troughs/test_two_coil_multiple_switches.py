from MpfDocsTestCase import MpfDocsTestCase


class TestTwoCoilMultipleSwitches(MpfDocsTestCase):

    rst_target = 'mechs/troughs/two_coil_multiple_switches'

    def test_modern_mechanical(self):
        self.assertIn('bd_trough', self.machine.ball_devices)
        self.assertIn('bd_drain', self.machine.ball_devices)

        self.assertTrue(self.machine.switch_controller.is_active('s_trough1'))
        self.assertTrue(self.machine.switch_controller.is_active('s_trough2'))
        self.assertTrue(self.machine.switch_controller.is_active('s_trough3'))
