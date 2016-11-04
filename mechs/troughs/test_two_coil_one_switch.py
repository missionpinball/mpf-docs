from MpfDocsTestCase import MpfDocsTestCase


class TestTwoCoilOneSwitch(MpfDocsTestCase):

    rst_target = 'mechs/troughs/two_coil_one_switch'

    def test_two_coil_one_switch(self):
        self.assertIn('bd_trough', self.machine.ball_devices)
        self.assertIn('bd_drain', self.machine.ball_devices)

        self.assertTrue(self.machine.switch_controller.is_active('s_trough_enter'))
