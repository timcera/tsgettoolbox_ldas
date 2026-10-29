r"""
tsgettoolbox command line/library tools to retrieve time series.

This program is a collection of utilities to download data from various
web services.
"""

__all__ = [
    "ldas",
    "ldas_gldas_noah",
    "ldas_gldas_noah_v2_0",
    "ldas_gldas_noah_v2_1",
    "ldas_grace",
    "ldas_merra",
    "ldas_nldas_fora",
    "ldas_nldas_noah",
    "ldas_nldas_vic",
    "ldas_smerge",
]

# Local folder imports
from .ldas import (
    ldas,
    ldas_gldas_noah,
    ldas_gldas_noah_v2_0,
    ldas_gldas_noah_v2_1,
    ldas_grace,
    ldas_merra,
    ldas_nldas_fora,
    ldas_nldas_noah,
    ldas_nldas_vic,
    ldas_smerge,
)
