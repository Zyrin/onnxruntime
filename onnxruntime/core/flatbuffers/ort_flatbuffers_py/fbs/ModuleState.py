# automatically generated by the FlatBuffers compiler, do not modify

# namespace: fbs

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ModuleState(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ModuleState()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsModuleState(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    @classmethod
    def ModuleStateBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x4F\x44\x54\x43", size_prefixed=size_prefixed)

    # ModuleState
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ModuleState
    def RequiresGradParams(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from ort_flatbuffers_py.fbs.Tensor import Tensor
            obj = Tensor()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # ModuleState
    def RequiresGradParamsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ModuleState
    def RequiresGradParamsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        return o == 0

    # ModuleState
    def FrozenParams(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from ort_flatbuffers_py.fbs.Tensor import Tensor
            obj = Tensor()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # ModuleState
    def FrozenParamsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ModuleState
    def FrozenParamsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        return o == 0

    # ModuleState
    def IsNominalState(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # ModuleState
    def HasExternalData(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

def ModuleStateStart(builder):
    builder.StartObject(4)

def Start(builder):
    ModuleStateStart(builder)

def ModuleStateAddRequiresGradParams(builder, requiresGradParams):
    builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(requiresGradParams), 0)

def AddRequiresGradParams(builder, requiresGradParams):
    ModuleStateAddRequiresGradParams(builder, requiresGradParams)

def ModuleStateStartRequiresGradParamsVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartRequiresGradParamsVector(builder, numElems: int) -> int:
    return ModuleStateStartRequiresGradParamsVector(builder, numElems)

def ModuleStateAddFrozenParams(builder, frozenParams):
    builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(frozenParams), 0)

def AddFrozenParams(builder, frozenParams):
    ModuleStateAddFrozenParams(builder, frozenParams)

def ModuleStateStartFrozenParamsVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartFrozenParamsVector(builder, numElems: int) -> int:
    return ModuleStateStartFrozenParamsVector(builder, numElems)

def ModuleStateAddIsNominalState(builder, isNominalState):
    builder.PrependBoolSlot(2, isNominalState, 0)

def AddIsNominalState(builder, isNominalState):
    ModuleStateAddIsNominalState(builder, isNominalState)

def ModuleStateAddHasExternalData(builder, hasExternalData):
    builder.PrependBoolSlot(3, hasExternalData, 0)

def AddHasExternalData(builder, hasExternalData):
    ModuleStateAddHasExternalData(builder, hasExternalData)

def ModuleStateEnd(builder):
    return builder.EndObject()

def End(builder):
    return ModuleStateEnd(builder)