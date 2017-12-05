# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..utils import BrickStat


def test_BrickStat_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(deprecated='1.0.0',
    nohash=True,
    usedefault=True,
    ),
    in_file=dict(argstr='%s',
    mandatory=True,
    position=-1,
    ),
    mask=dict(argstr='-mask %s',
    position=2,
    ),
    max=dict(argstr='-max',
    ),
    mean=dict(argstr='-mean',
    ),
    min=dict(argstr='-min',
    position=1,
    ),
    percentile=dict(argstr='-percentile %.3f %.3f %.3f',
    ),
    slow=dict(argstr='-slow',
    ),
    sum=dict(argstr='-sum',
    ),
    terminal_output=dict(deprecated='1.0.0',
    nohash=True,
    ),
    var=dict(argstr='-var',
    ),
    )
    inputs = BrickStat.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_BrickStat_outputs():
    output_map = dict(min_val=dict(),
    )
    outputs = BrickStat.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
