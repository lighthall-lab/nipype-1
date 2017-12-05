# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..developer import JistLaminarProfileCalculator


def test_JistLaminarProfileCalculator_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(deprecated='1.0.0',
    nohash=True,
    usedefault=True,
    ),
    inIntensity=dict(argstr='--inIntensity %s',
    ),
    inMask=dict(argstr='--inMask %s',
    ),
    incomputed=dict(argstr='--incomputed %s',
    ),
    null=dict(argstr='--null %s',
    ),
    outResult=dict(argstr='--outResult %s',
    hash_files=False,
    ),
    terminal_output=dict(deprecated='1.0.0',
    nohash=True,
    ),
    xDefaultMem=dict(argstr='-xDefaultMem %d',
    ),
    xMaxProcess=dict(argstr='-xMaxProcess %d',
    usedefault=True,
    ),
    xPrefExt=dict(argstr='--xPrefExt %s',
    ),
    )
    inputs = JistLaminarProfileCalculator.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_JistLaminarProfileCalculator_outputs():
    output_map = dict(outResult=dict(),
    )
    outputs = JistLaminarProfileCalculator.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
