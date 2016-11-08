from MpfDocsTestCase import MpfDocsTestCase

class TestModernOpto(MpfDocsTestCase):

    rst_target = 'mechs/troughs/modern_opto'

    def test_modern_opto(self):
        self.assertIn('bd_trough', self.machine.ball_devices)

        self.assertTrue(self.machine.switch_controller.is_active('s_trough1'))
        self.assertTrue(self.machine.switch_controller.is_active('s_trough2'))
        self.assertTrue(self.machine.switch_controller.is_active('s_trough3'))
        self.assertTrue(self.machine.switch_controller.is_active('s_trough4'))
        self.assertTrue(self.machine.switch_controller.is_active('s_trough5'))
        self.assertTrue(self.machine.switch_controller.is_active('s_trough6'))
        self.assertFalse(self.machine.switch_controller.is_active('s_trough_jam'))
