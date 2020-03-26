# -*- coding: utf-8 -*-
"""Documentation about matchms"""

import matchms.helper_functions
import matchms.ms_functions
import matchms.ms_library_search
import matchms.ms_similarity_classical
import matchms.networking
import matchms.plotting_functions
import matchms.similarity_measure

from .similarity_measure import SimilarityMeasures

from .__version__ import __version__

import logging
logging.getLogger(__name__).addHandler(logging.NullHandler())

# remove unnecessary members
# del logging

__author__ = "Netherlands eScience Center"
__email__ = 'generalization@esciencecenter.nl'
