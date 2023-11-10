
import ctypes
from typing import Dict, Any, List, Tuple


class TableStructure(ctypes.Structure):

    def __init__(self, df_dict: Dict[str, Any], *args: Any, **kw: Any):
        super().__init__(*args, **kw)
        fields = []
        for k, v in df_dict.items():
            if isinstance(v, int):
                fields.append((k, ctypes.c_int(v)))
            elif isinstance(v, float):
                fields.append((k, ctypes.c_double(v)))
            else:
                fields.append((k, ctypes.c_char_p(v.encode('utf-8'))))

        self._fields = fields


class SrcTopoNode(TableStructure):

    _fields = [
        ('node', ctypes.c_int),
        ('type', ctypes.c_int),
        ('unom', ctypes.c_double),
        ('vzd', ctypes.c_double),
        ('gsh', ctypes.c_double),
        ('bsh', ctypes.c_double),
        ('qg', ctypes.c_double),
        ('qn', ctypes.c_double),
        ('unom_orig', ctypes.c_double)
    ]

    def __init__(self, df_dict: Dict[str, Any], *args: Any, **kw: Any):
        super().__init__(df_dict, *args, **kw)


class SrcNodeGeo(TableStructure):
    _fields = [
        ('node', ctypes.c_int),
        ('cz_id', ctypes.c_int),
        ('oes_id', ctypes.c_int),
        ('zsp_id', ctypes.c_int),
        ('sub_id', ctypes.c_int),
    ]

    def __init__(self, df_dict: Dict[str, Any], *args: Any, **kw: Any):
        super().__init__(df_dict, *args, **kw)


class SrcTopoLine(TableStructure):
    _fields = [
        ('node_from', ctypes.c_int),
        ('node_to', ctypes.c_int),
        ('pnum', ctypes.c_int),
        ('type', ctypes.c_int),
        ('r', ctypes.c_double),
        ('x', ctypes.c_double),
        ('g', ctypes.c_double),
        ('b', ctypes.c_double),
        ('b_from', ctypes.c_double),
        ('b_to', ctypes.c_double),
        ('ktr', ctypes.c_double),
        ('kti', ctypes.c_double)
    ]

    def __init__(self, df_dict: Dict[str, Any], *args: Any, **kw: Any):
        super().__init__(df_dict, *args, **kw)


class SrcTopoSection(TableStructure):
    _fields = [
        ('sec_num', ctypes.c_int),
        ('node_from', ctypes.c_int),
        ('node_to', ctypes.c_int),
        ('dv', ctypes.c_double)
    ]

    def __init__(self, df_dict: Dict[str, Any], *args: Any, **kw: Any):
        super().__init__(df_dict, *args, **kw)


class SrcTopoRge(TableStructure):
    _fields = [
        ('rge', ctypes.c_int),
        ('node', ctypes.c_int)
    ]

    def __init__(self, df_dict: Dict[str, Any], *args: Any, **kw: Any):
        super().__init__(df_dict, *args, **kw)


class SrcTopoGtpCon(TableStructure):
    _fields = [
        ('gtp_code', ctypes.c_char_p),
        ('node', ctypes.c_int),
        ('dist_coeff', ctypes.c_double)
    ]

    def __init__(self, df_dict: Dict[str, Any], *args: Any, **kw: Any):
        super().__init__(df_dict, *args, **kw)


class SrcOptGes(TableStructure):
    _fields = [
        ('rge_group', ctypes.c_int),
        ('rge', ctypes.c_int),
        ('type_opt', ctypes.c_int)
    ]

    def __init__(self, df_dict: Dict[str, Any], *args: Any, **kw: Any):
        super().__init__(df_dict, *args, **kw)


class DictConsumer(TableStructure):
    _fields = [
        ('gtp_code', ctypes.c_char_p),
        ('sub_id', ctypes.c_int)
    ]

    def __init__(self, df_dict: Dict[str, Any], *args: Any, **kw: Any):
        super().__init__(df_dict, *args, **kw)


class ModelBid(TableStructure):
    _fields = [
        ('t', ctypes.c_int),
        ('rge', ctypes.c_int),
        ('node', ctypes.c_int),
        ('interval', ctypes.c_int),
        ('p', ctypes.c_double),
        ('pmin', ctypes.c_double),
        ('pmax', ctypes.c_double),
        ('price', ctypes.c_double)
    ]

    def __init__(self, df_dict: Dict[str, Any], *args: Any, **kw: Any):
        super().__init__(df_dict, *args, **kw)


class ModelBidCon(TableStructure):
    _fields = [
        ('t', ctypes.c_int),
        ('gtp_code', ctypes.c_char_p),
        ('interval', ctypes.c_int),
        ('p_ats', ctypes.c_double),
        ('pmax', ctypes.c_double),
        ('price', ctypes.c_double)
    ]

    def __init__(self, df_dict: Dict[str, Any], *args: Any, **kw: Any):
        super().__init__(df_dict, *args, **kw)


class ModelBidReasonCode(TableStructure):
    _fields = [
        ('t', ctypes.c_int),
        ('rge', ctypes.c_int),
        ('price', ctypes.c_double),
        ('code', ctypes.c_int)
    ]

    def __init__(self, df_dict: Dict[str, Any], *args: Any, **kw: Any):
        super().__init__(df_dict, *args, **kw)


class SrcSupply(TableStructure):
    _fields = [
        ('t', ctypes.c_int),
        ('zone', ctypes.c_int),
        ('price', ctypes.c_double),
        ('volume', ctypes.c_int)
    ]

    def __init__(self, df_dict: Dict[str, Any], *args: Any, **kw: Any):
        super().__init__(df_dict, *args, **kw)


class SrcDemand(TableStructure):
    _fields = [
        ('t', ctypes.c_int),
        ('zone', ctypes.c_int),
        ('price', ctypes.c_double),
        ('volume', ctypes.c_int)
    ]

    def __init__(self, df_dict: Dict[str, Any], *args: Any, **kw: Any):
        super().__init__(df_dict, *args, **kw)


class SrcParallel(TableStructure):
    _fields = [
        ('t', ctypes.c_int),
        ('node_from', ctypes.c_int),
        ('node_to', ctypes.c_double),
        ('pnum', ctypes.c_int),
        ('flow', ctypes.c_double)
    ]

    def __init__(self, df_dict: Dict[str, Any], *args: Any, **kw: Any):
        super().__init__(df_dict, *args, **kw)


class ModelBus(TableStructure):
    _fields = [
        ('t', ctypes.c_int),
        ('node', ctypes.c_int),
        ('pg_ats', ctypes.c_double),
        ('pn', ctypes.c_double),
        ('qg', ctypes.c_double),
        ('qn', ctypes.c_double),
        ('node_price_ats', ctypes.c_double),
        ('type', ctypes.c_int)
    ]

    def __init__(self, df_dict: Dict[str, Any], *args: Any, **kw: Any):
        super().__init__(df_dict, *args, **kw)


class ModelLine(TableStructure):
    _fields = [
        ('t', ctypes.c_int),
        ('node_from', ctypes.c_int),
        ('node_to', ctypes.c_int),
        ('pnum_actual', ctypes.c_int),
        ('pnum_max', ctypes.c_int),
        ('ats_flow', ctypes.c_double),
        ('p_from', ctypes.c_double),
        ('p_to', ctypes.c_double),
        ('q_from', ctypes.c_double),
        ('q_to', ctypes.c_double)
    ]

    def __init__(self, df_dict: Dict[str, Any], *args: Any, **kw: Any):
        super().__init__(df_dict, *args, **kw)


class ModelRge(TableStructure):
    _fields = [
        ('t', ctypes.c_int),
        ('rge', ctypes.c_int),
        ('node', ctypes.c_int),
        ('pmin', ctypes.c_int),
        ('pmax', ctypes.c_int),
        ('p', ctypes.c_double),
        ('node_price_ats', ctypes.c_double),
        ('pdg', ctypes.c_double)
    ]

    def __init__(self, df_dict: Dict[str, Any], *args: Any, **kw: Any):
        super().__init__(df_dict, *args, **kw)


class ModelSection(TableStructure):
    _fields = [
        ('t', ctypes.c_int),
        ('sec_num', ctypes.c_int),
        ('node_from', ctypes.c_int),
        ('node_to', ctypes.c_int),
        ('vetv_state', ctypes.c_int),
        ('dv', ctypes.c_double),
        ('sec_flow_ats', ctypes.c_double),
        ('sec_flow', ctypes.c_double),
        ('pmin', ctypes.c_double),
        ('pmax', ctypes.c_double)
    ]

    def __init__(self, df_dict: Dict[str, Any], *args: Any, **kw: Any):
        super().__init__(df_dict, *args, **kw)


class ModelWsum(TableStructure):
    _fields = [
        ('t', ctypes.c_int),
        ('rge_group', ctypes.c_int),
        ('rge', ctypes.c_int),
        ('wmax', ctypes.c_double),
        ('grp_pmin', ctypes.c_double),
        ('grp_pmax', ctypes.c_double),
        ('grp_p', ctypes.c_double),
        ('grp_pmin_so', ctypes.c_double),
        ('grp_pmax_so', ctypes.c_double),
        ('grp_price', ctypes.c_double)
    ]

    def __init__(self, df_dict: Dict[str, Any], *args: Any, **kw: Any):
        super().__init__(df_dict, *args, **kw)


class SrcConsumer(TableStructure):
    _fields = [
        ('t', ctypes.c_int),
        ('gtp_code', ctypes.c_char_p),
        ('p', ctypes.c_double),
        ('pmax', ctypes.c_double),
        ('loss', ctypes.c_double)
    ]

    def __init__(self, df_dict: Dict[str, Any], *args: Any, **kw: Any):
        super().__init__(df_dict, *args, **kw)


class TopologyData(ctypes.Structure):
    _fields = [
        ('SrcTopoNodeTable', ctypes.POINTER(SrcTopoNode)),
        ('SrcNodeGeoTable', ctypes.POINTER(SrcNodeGeo)),
        ('SrcTopoLineTable', ctypes.POINTER(SrcTopoLine)),
        ('SrcTopoSectionTable', ctypes.POINTER(SrcTopoSection)),
        ('SrcTopoRgeTable', ctypes.POINTER(SrcTopoRge)),
        ('SrcTopoGtpConTable', ctypes.POINTER(SrcTopoGtpCon)),
        ('SrcOptGesTable', ctypes.POINTER(SrcOptGes)),
        ('DictConsumers', ctypes.POINTER(DictConsumer))
    ]
    
    def __init__(self, fields: List[Tuple[str, ctypes.POINTER]], *args: Any, **kw: Any):
        super().__init__(*args, **kw)
        self._fields = fields
        

class BidData(ctypes.Structure):
    _fields = [
        ('ModelBidTable', ctypes.POINTER(ModelBid)),
        ('ModelBidConTable', ctypes.POINTER(ModelBidCon)),
        ('ModelBidReasonTable', ctypes.POINTER(ModelBidReasonCode))
    ]
    
    def __init__(self, fields: List[Tuple[str, ctypes.POINTER]], *args: Any, **kw: Any):
        super().__init__(*args, **kw)
        self._fields = fields


class ModelData(ctypes.Structure):
    _fields = [
        ('SrcSupplyTable', ctypes.POINTER(SrcSupply)),
        ('SrcDemandTable', ctypes.POINTER(SrcDemand)),
        ('SrcParallelTable', ctypes.POINTER(SrcParallel)),
        ('ModelBusTable', ctypes.POINTER(ModelBus)),
        ('ModelLineTable', ctypes.POINTER(ModelLine)),
        ('ModelRgeTable', ctypes.POINTER(ModelRge)),
        ('ModelSectionTable', ctypes.POINTER(ModelSection)),
        ('ModelWsumTable', ctypes.POINTER(ModelWsum)),
        ('SrcConsumer', ctypes.POINTER(SrcConsumer))
    ]
    
    def __init__(self, fields: List[Tuple[str, ctypes.POINTER]], *args: Any, **kw: Any):
        super().__init__(*args, **kw)
        self._fields = fields


class HourState(ctypes.Structure):

    # _fields = [
    #     ('t', ctypes.c_int),
    #     ('topologyData', ctypes.POINTER(TopologyData)),
    #     ('bidData', ctypes.POINTER(BidData)),
    #     ('modelData', ctypes.POINTER(ModelData))
    # ]
    
    def __init__(self, fields: List[Tuple[str, ctypes.POINTER]], *args: Any, **kw: Any):
        super().__init__(*args, **kw)
        self._fields = fields


class_dict = {
    'topo_node': SrcTopoNode,
    'topo_vetv': SrcTopoLine,
    'topo_section': SrcTopoSection,
    'node_geo': SrcNodeGeo,
    'topo_rge': SrcTopoRge,
    'topo_gtp_con': SrcTopoGtpCon,
    'topo_opt_ges': SrcOptGes,
    'dict_consumers': DictConsumer,
    'model_bid': ModelBid,
    'model_bid_con': ModelBidCon,
    'model_rge': ModelRge,
    'model_section': ModelSection,
    'model_bid_reason': ModelBidReasonCode,
    'model_bus': ModelBus,
    'model_line': ModelLine,
    'model_wsum': ModelWsum,
    'src_supply': SrcSupply,
    'src_demand': SrcDemand,
    'src_consumer': SrcConsumer,
    'parallel_flows': SrcParallel
}
