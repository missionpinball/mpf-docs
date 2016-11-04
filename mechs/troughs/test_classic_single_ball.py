from MpfDocsTestCase import MpfDocsTestCase


class TestClassicSingleBall(MpfDocsTestCase):

    rst_target = 'mechs/troughs/classic_single_ball'

    def test_classic_single_ball(self):
        self.assertIn('bd_drain', self.machine.ball_devices)

        self.assertTrue(self.machine.switch_controller.is_active('s_drain'))
