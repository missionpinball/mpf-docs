from MpfDocsTestCase import MpfDocsTestCase


class TestSingleWound(MpfDocsTestCase):

    rst_target = 'mechs/flippers/single_wound'

    def test_single_wound(self):
        self.assertIn('s_left_flipper', self.machine.switches)
        self.assertIn('s_right_flipper', self.machine.switches)
        self.assertIn('c_flipper_left', self.machine.coils)
        self.assertIn('c_flipper_right', self.machine.coils)
        self.assertIn('left_flipper', self.machine.flippers)
        self.assertIn('right_flipper', self.machine.flippers)

        # flippers should enable on machine_reset_phase_3
        self.assertTrue(self.machine.flippers.left_flipper._enabled)
        self.assertTrue(self.machine.flippers.right_flipper._enabled)
