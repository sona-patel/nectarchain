import logging

import numpy as np
from ctapipe.containers import Container, Field, Map, partial

logging.basicConfig(format="%(asctime)s %(name)s %(levelname)s %(message)s")
log = logging.getLogger(__name__)
log.handlers = logging.getLogger("__main__").handlers


__all__ = ["ArrayDataContainer", "TriggerMapContainer"]


class NectarCAMContainer(Container):
    """base class for the NectarCAM containers. This contaner cannot berecursive,
    to be directly written with a HDF5TableWriter"""


class ArrayDataContainer(NectarCAMContainer):
    """
    A container that holds information about waveforms from a specific run.

    Attributes:
        run_number (int): The run number associated with the waveforms.
        nevents (int): The number of events.
        npixels (int): The number of pixels.
        camera (str): The name of the camera.
        pixels_id (np.ndarray): An array of pixel IDs.
        broken_pixels_hg (np.ndarray): An array of high gain broken pixels.
        broken_pixels_lg (np.ndarray): An array of low gain broken pixels.
        ucts_timestamp (np.ndarray): An array of events' UCTS timestamps.
        ucts_busy_counter (np.ndarray): An array of UCTS busy counters.
        ucts_event_counter (np.ndarray): An array of UCTS event counters.
        event_type (np.ndarray): An array of trigger event types.
        event_id (np.ndarray): An array of event IDs.
        trig_pattern_all (np.ndarray): An array of trigger patterns.
        trig_pattern (np.ndarray): An array of reduced trigger patterns.
        multiplicity (np.ndarray): An array of events' multiplicities.
    """

    run_number = Field(
        type=int,
        description="run number associated to the waveforms",
    )
    nevents = Field(
        type=int,
        description="number of events",
    )
    npixels = Field(
        type=int,
        description="number of effective pixels",
    )
    pixels_id = Field(type=np.ndarray, dtype=np.uint16, ndim=1, description="pixel ids")
    broken_pixels_hg = Field(
        type=np.ndarray, dtype=bool, ndim=2, description="high gain broken pixels"
    )
    broken_pixels_lg = Field(
        type=np.ndarray, dtype=bool, ndim=2, description="low gain broken pixels"
    )
    camera = Field(
        type=str,
        description="camera name",
    )
    ucts_timestamp = Field(
        type=np.ndarray, dtype=np.uint64, ndim=1, description="events ucts timestamp"
    )
    ucts_busy_counter = Field(
        type=np.ndarray, dtype=np.uint32, ndim=1, description="ucts busy counter"
    )
    ucts_event_counter = Field(
        type=np.ndarray, dtype=np.uint32, ndim=1, description="ucts event counter"
    )
    event_type = Field(
        type=np.ndarray, dtype=np.uint8, ndim=1, description="trigger event type"
    )
    event_id = Field(type=np.ndarray, dtype=np.uint32, ndim=1, description="event ids")
    trig_pattern_all = Field(
        type=np.ndarray, dtype=bool, ndim=3, description="trigger pattern"
    )
    trig_pattern = Field(
        type=np.ndarray, dtype=bool, ndim=2, description="reduced trigger pattern"
    )
    multiplicity = Field(
        type=np.ndarray, dtype=np.uint16, ndim=1, description="events multiplicity"
    )


class TriggerMapContainer(Container):
    containers = Field(
        default_factory=partial(Map, Container),
        description="trigger mapping of Container",
    )
