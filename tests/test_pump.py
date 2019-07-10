from gpiozero import *


def test_pump_on(mock_factory):
    pump1 = mock_factory.pin(4)

    with OutputDevice(4) as device:

        device.on()
        assert pump1.state
        device.off()

    assert not pump1.state


def test_pump_time():
    pass


def test_pump_stop(mock_factory):
    pass


def test_pump_series():
    pass
