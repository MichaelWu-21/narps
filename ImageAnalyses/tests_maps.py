# tests for narps code
# - currently these are all just smoke tests

import pytest
import os
from narps import Narps
from AnalyzeMaps import mk_overlap_maps,\
    mk_range_maps, mk_std_maps,\
    mk_correlation_maps_unthresh, analyze_clusters,\
    plot_distance_from_mean, get_thresh_similarity
# Use a fixed base dir so that we can
# access the results as a circleci artifact


@pytest.fixture(scope="session")
def narps():
    basedir = '/tmp/data'
    assert os.path.exists(basedir)
    narps = Narps(basedir)
    narps.load_data()
    return(narps)


# tests
# AnalyzeMaps
def test_mk_overlap_maps(narps):
    # create maps showing overlap of thresholded images
    mk_overlap_maps(narps)


def test_mk_range_maps(narps):
    mk_range_maps(narps)


def test_mk_std_maps(narps):
    mk_std_maps(narps)


def test_unthresh_correlation_analysis(narps):
    # conbine these into a single test
    # since they share data
    corr_type = 'spearman'
    dendrograms, membership = mk_correlation_maps_unthresh(
        narps, corr_type=corr_type)

    _ = analyze_clusters(
        narps,
        dendrograms,
        membership,
        corr_type=corr_type)


def test_plot_distance_from_mean(narps):
    plot_distance_from_mean(narps)


def test_get_thresh_similarity(narps):
    get_thresh_similarity(narps)
