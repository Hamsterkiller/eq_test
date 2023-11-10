import ctypes

from typing import Dict
import pandas as pd
import cpp_structs as cpps
from create_array_of_structs import create_array_of_structs


def generate_states(data_dict: Dict[str, Dict[str, pd.DataFrame]]) -> ctypes.POINTER:

    states = []
    for h in range(0, 24):
        h_state_fields = [('t', h)]
        for cat, df_dict in data_dict.items():
            cat_fields = []
            for df_name, df in df_dict.items():
                struct_arr = create_array_of_structs(h, df, df_name)
                cat_fields.append((df_name, struct_arr))
            if cat == 'topology':
                key = 'topologyData'
                cat_struct = cpps.TopologyData(cat_fields)
            elif cat == 'bid_data':
                key = 'bidData'
                cat_struct = cpps.BidData(cat_fields)
            else:
                key = 'modelData'
                cat_struct = cpps.ModelData(cat_fields)
            h_state_fields.append((key, cat_struct))
        states.append(cpps.HourState(h_state_fields))

    return states


    # TopologyData
    # topologyData;
    # topologyData.SrcTopoNodeTable = createSrcBusTable(inFolderStr + "/topo_node.csv");
    # topologyData.SrcNodeGeoTable = createSrcBusGeoTable(inFolderStr + "/node_geo.csv");
    # topologyData.SrcTopoLineTable = createSrcLineTable(inFolderStr + "/topo_vetv.csv");
    # topologyData.SrcTopoSectionTable = createSrcSectionTable(inFolderStr + "/topo_section.csv");
    # topologyData.SrcTopoRgeTable = createSrcRgeTable(inFolderStr + "/topo_rge.csv");
    # topologyData.SrcTopoGtpConTable = createSrcTopoGtpConTable(inFolderStr + "/topo_gtp_con.csv");
    # topologyData.DictConsumers = createDictConsumerTable(inFolderStr + "/dict_consumers.csv");
    # topologyData.SrcOptGesTable = createSrcOptGesTable(inFolderStr + "/topo_opt_ges.csv");
    # BidData
    # bidData;
    # bidData.ModelBidTable = createModelBidTable(inFolderStr + "/model_bid.csv");
    # bidData.ModelBidConTable = createModelBidConTable(inFolderStr + "/model_bid_con.csv");
    # bidData.ModelBidReasonTable = createModelBidReasonTable(inFolderStr + "/model_bid_reason.csv");
    # ModelData
    # modelData;
    # modelData.SrcSupplyTable = createSupplyTable(inFolderStr + "/src_supply.csv");
    # modelData.SrcDemandTable = createDemandTable(inFolderStr + "/src_demand.csv");
    # modelData.SrcConsumer = createSrcConsumerTable(inFolderStr + "/src_consumer.csv");
    # modelData.SrcParallelTable = createParallelTable(inFolderStr + "/parallel_flows.csv");
    # modelData.ModelBusTable = createModelBusTable(inFolderStr + "/model_bus.csv");
    # modelData.ModelLineTable = createModelLineTable(inFolderStr + "/model_line.csv");
    # modelData.ModelRgeTable = createModelRgeTable(inFolderStr + "/model_rge.csv");
    # modelData.ModelSectionTable = createModelSectionTable(inFolderStr + "/model_section.csv");
    # modelData.ModelWsumTable = createModelWsumTable(inFolderStr + "/model_wsum.csv");
    # std::vector < HourState > State;
    # State.reserve(PERIODS_NUM);
    # for (int h: all_hours) {
    #     HourState state(h, topologyData);
    # state.t = h;
    # state.bidData.ModelBidTable = sliceDayData(bidData.ModelBidTable, h);
    # state.bidData.ModelBidConTable = sliceDayData(bidData.ModelBidConTable, h);
    # state.bidData.ModelBidReasonTable = sliceDayData(bidData.ModelBidReasonTable, h);
    # state.modelData.SrcSupplyTable = sliceDayData(modelData.SrcSupplyTable, h);
    # state.modelData.SrcConsumer = sliceDayData(modelData.SrcConsumer, h);
    # state.modelData.SrcDemandTable = sliceDayData(modelData.SrcDemandTable, h);
    # state.modelData.SrcParallelTable = sliceDayData(modelData.SrcParallelTable, h);
    # state.modelData.ModelBusTable = sliceDayData(modelData.ModelBusTable, h);
    # state.modelData.ModelLineTable = sliceDayData(modelData.ModelLineTable, h);
    # state.modelData.ModelRgeTable = sliceDayData(modelData.ModelRgeTable, h);
    # state.modelData.ModelSectionTable = sliceDayData(modelData.ModelSectionTable, h);
    # state.modelData.ModelWsumTable = sliceDayData(modelData.ModelWsumTable, h);
    # State.emplace_back(state);
    # }

