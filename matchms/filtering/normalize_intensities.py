import numpy
from matchms import Spikes


def normalize_intensities(spectrum_in):
    """Normalize intensities to unit height."""

    if spectrum_in is None:
        return None

    spectrum = spectrum_in.clone()

    if spectrum.peaks.intensities.size > 0:
        scale_factor = numpy.max(spectrum.peaks.intensities)
        mz, intensities = spectrum.peaks
        normalized_intensities = intensities / scale_factor
        spectrum.peaks = Spikes(mz=mz, intensities=normalized_intensities)

    return spectrum
