"""
Distributed under the terms of the MIT License.

The full license is in the file LICENSE, distributed with this software.

Copyright (C) Jun Zhu. All rights reserved.
"""
from collections import abc


class _Config(abc.Mapping):
    """Readonly config."""

    _data = {
        # foreground/background color (r, g, b, alpha)
        "FOREGROUND_COLOR": (0, 0, 0, 255),
        "BACKGROUND_COLOR": (225, 225, 225, 255),
        # color map in contour plots, valid options are: thermal, flame,
        # yellowy, bipolar, spectrum, cyclic, greyclip, grey, viridis,
        # inferno, plasma, magma
        "COLOR_MAP": 'plasma',
        # colors of for ROI bounding boxes 1 to 4
        "ROI_COLORS": ('b', 'r', 'g', 'o'),
        # interval for timed plot widgets and image views, in milliseconds
        "PLOT_WIDGET_TIMER": 1000,
        "IMAGE_VIEW_TIMER": 1000,
    }

    def __init__(self):
        super().__init__()

    def __contains__(self, key):
        """Override."""
        return self._data.__contains__(key)

    def __getitem__(self, key):
        """Override."""
        return self._data.__getitem__(key)

    def __len__(self):
        """Override."""
        return self._data.__len__()

    def __iter__(self):
        """Override."""
        return self._data.__iter__()


config = _Config()
