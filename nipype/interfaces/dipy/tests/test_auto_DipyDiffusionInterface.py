# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..base import DipyDiffusionInterface


def test_DipyDiffusionInterface_inputs():
    input_map = dict(b0_thres=dict(usedefault=True,
    ),
    ignore_exception=dict(deprecated='1.0.0',
    nohash=True,
    usedefault=True,
    ),
    in_bval=dict(mandatory=True,
    ),
    in_bvec=dict(mandatory=True,
    ),
    in_file=dict(mandatory=True,
    ),
    out_prefix=dict(),
    )
    inputs = DipyDiffusionInterface.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value

