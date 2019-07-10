from gpiozero import *


def test_run_pump(mock_factory):
    pump1 = mock_factory.pin(4)

    with OutputDevice(4) as device:
        device.on()
        assert pump1.state
        device.off()

    assert not pump1.state

