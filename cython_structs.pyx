
cdef struct SrcTopoNode:
    int node
    int type
    double unom
    double vzd
    double gsh
    double bsh
    double qg
    double qn
    double unom_orig

cdef struct SrcNodeGeo:
    int node
    int cz_id
    int oes_id
    int zsp_id
    int sub_id

cdef struct SrcTopoLine:
    int node_from,
    int node_to,
    int pnum,
    int type,
    double r,
    double x,
    double g,
    double b,
    double b_from,
    double b_to,
    double ktr,
    double kti

cdef struct SrcTopoSection:
    int sec_num,
    int node_from,
    int node_to,
    double dv

cdef struct SrcTopoRge:
    int rge,
    int node

cdef struct SrcTopoGtpCon:
    str gtp_code,
    int node,
    double dist_coeff

cdef struct SrcOptGes:
    int rge_group,
    int rge,
    int type_opt

cdef struct DictConsumer:
    std gtp_code,
    int sub_id

cdef struct ModelBid:
    int t,
    int rge,
    int node,
    int interval,
    double p,
    double pmin,
    double pmax,
    double price

cdef struct ModelBidCon:
    int t,
    str gtp_code,
    int interval,
    double p_ats,
    double pmax,
    double price

cdef struct ModelBidReasonCode:
    int t,
    int rge,
    double price,
    int code

cdef struct SrcSupply:
    int t,
    int zone,
    double price,
    double volume

cdef struct SrcDemand:
    int t,
    int zone,
    double price,
    double volume

cdef struct srcParallel:
    int t,
    int node_from,
    int node_to,
    int pnum,
    double flow

cdef struct ModelBus:
    int t,
    int node,
    double pg_ats,
    double pn,
    double qg,
    double qn,
    double node_price_ats,
    int type

cdef struct ModelLine:
    int t,
    int node_from,
    int node_to,
    int pnum_actual,
    int pnum_max,
    double ats_flow,
    double p_from,
    double p_to,
    double q_from,
    double q_to

cdef struct ModelRge:
    int t,
    int rge,
    int node,
    double pmin,
    double pmax,
    double p,
    double node_price_ats,
    double pdg

cdef struct ModelSection:
    int t,
    int sec_num,
    int node_from,
    int node_to,
    int vetv_state,
    double dv,
    double sec_flow_ats,
    double sec_flow,
    double pmin,
    double pmax

cdef struct ModelWsum:
    int t,
    int rge_group,
    int rge,
    double wmax,
    double grp_pmin,
    double grp_pmax,
    double grp_p,
    double grp_pmin_so,
    double grp_pmax_so,
    double grp_price

cdef struct SrcConsumer:
    int t,
    str gtp_code,
    double p,
    double pmax,
    double loss

# convert TopoNode list of dicts to C array of TopoNode structs
cdef void makeTopoNodeArray(list df_dict, SrcTopoNode *items, int num_items):

    cdef SrcTopoNode *item
    for i, el in enumerate(df_dict):
        if i >= num_items:
            break
        item = &items[i]
        item.node = el['node']
        item.type = el['type']
        item.unom = el['unom']
        item.vzd = el['vzd']
        item.gsh = el['gsh']
        item.bsh = el['bsh']
        item.qg = el['qg']
        item.qn = el['qn']
        item.unom_orig = el['unom_orig']

# convert NodeGeo list of dicts to C array of NodeGeo structs
cdef void makeNodeGeoArray(list df_dict, SrcNodeGeo *items, int num_items):

    cdef SrcNodeGeo *item
    for i, el in enumerate(df_dict):
        if i >= num_items:
            break
        item = &items[i]
        item.node = el['node']
        item.cz_id = el['cz_id']
        item.oes_id = el['oes_id']
        item.zsp_id = el['zsp_id']
        item.sub_id = el['sub_id']

# convert TopoLine list of dicts to C array of TopoLine structs
cdef void makeTopoLineArray(list df_dict, SrcTopoLine *items, int num_items):

    cdef SrcTopoLine *item
    for i, el in enumerate(df_dict):
        if i >= num_items:
            break
        item = &items[i]
        item.node_from = el['node']
        item.node_to = el['cz_id']
        item.pnum = el['oes_id']
        item.type = el['zsp_id']
        item.r = el['sub_id']
        item.x = el['sub_id']
        item.g = el['sub_id']
        item.b = el['sub_id']
        item.b_from = el['sub_id']
        item.b_to = el['sub_id']
        item.ktr = el['sub_id']
        item.kti = el['sub_id']

# convert TopoSection list of dicts to C array of TopoSection structs
cdef void makeTopoSectionArray(list df_dict, SrcTopoSection *items, int num_items):

    cdef SrcTopoSection *item
    for i, el in enumerate(df_dict):
        if i >= num_items:
            break
        item = &items[i]
        item.sec_num = el['sec_num']
        item.node_from = el['node_from']
        item.node_to = el['node_to']
        item.dv = el['dv']

# convert TopoSection list of dicts to C array of TopoSection structs
cdef void makeTopoRgeArray(list df_dict, SrcTopoRge *items, int num_items):

    cdef SrcTopoRge *item
    for i, el in enumerate(df_dict):
        if i >= num_items:
            break
        item = &items[i]
        item.rge = el['rge']
        item.node = el['node']

# convert TopoSection list of dicts to C array of TopoSection structs
cdef void makeTopoGtpConArray(list df_dict, SrcTopoGtpCon *items, int num_items):

    cdef SrcTopoGtpCon *item
    for i, el in enumerate(df_dict):
        if i >= num_items:
            break
        item = &items[i]
        item.gtp_code = el['gtp_code']
        item.node = el['node']
        item.dist_coeff = el['dist_coeff']

# convert TopoSection list of dicts to C array of TopoSection structs
cdef void makeTopoOptGesArray(list df_dict, SrcOptGesCon *items, int num_items):

    cdef SrcOptGesCon *item
    for i, el in enumerate(df_dict):
        if i >= num_items:
            break
        item = &items[i]
        item.rge_group = el['rge_group']
        item.rge = el['rge']
        item.type_opt = el['type_opt']

# convert DictConsumer list of dicts to C array of DictConsumer structs
cdef void makeDictConsumerArray(list df_dict, DictConsumer *items, int num_items):

    cdef DictConsumer *item
    for i, el in enumerate(df_dict):
        if i >= num_items:
            break
        item = &items[i]
        item.gtp_code = el['gtp_code']
        item.sub_id = el['sub_id']

# convert ModelBid list of dicts to C array of ModelBid structs
cdef void makeModelBidArray(list df_dict, ModelBid *items, int num_items):

    cdef ModelBid *item
    for i, el in enumerate(df_dict):
        if i >= num_items:
            break
        item = &items[i]
        item.t = el['t']
        item.rge = el['rge']
        item.node = el['node']
        item.rge = el['interval']
        item.rge = el['p']
        item.rge = el['pmin']
        item.rge = el['pmax']
        item.rge = el['price']

# convert ModelBidCon list of dicts to C array of ModelBidCon structs
cdef void makeModelBidConArray(list df_dict, ModelBidCon *items, int num_items):

    cdef ModelBidCon *item
    for i, el in enumerate(df_dict):
        if i >= num_items:
            break
        item = &items[i]
        item.t = el['t']
        item.gtp_code = el['gtp_code']
        item.interval = el['interval']
        item.p_ats = el['p_ats']
        item.pmax = el['pmax']
        item.price = el['price']

# convert ModelBidReason list of dicts to C array of ModelBidReason structs
cdef void makeModelBidReasonCodeArray(list df_dict, ModelBidReasonCode *items, int num_items):

    cdef ModelBidReasonCode *item
    for i, el in enumerate(df_dict):
        if i >= num_items:
            break
        item = &items[i]
        item.t = el['t']
        item.rge = el['rge']
        item.price = el['price']
        item.code = el['code']

# convert SrcSupply list of dicts to C array of SrcSupply structs
cdef void makeSrcSupplyArray(list df_dict, SrcSupply *items, int num_items):

    cdef SrcSupplyCode *item
    for i, el in enumerate(df_dict):
        if i >= num_items:
            break
        item = &items[i]
        item.t = el['t']
        item.zone = el['zone']
        item.price = el['price']
        item.volume = el['volume']

# convert SrcSupply list of dicts to C array of SrcSupply structs
cdef void makeSrcDemandArray(list df_dict, SrcDemand *items, int num_items):

    cdef SrcDemandCode *item
    for i, el in enumerate(df_dict):
        if i >= num_items:
            break
        item = &items[i]
        item.t = el['t']
        item.zone = el['zone']
        item.price = el['price']
        item.volume = el['volume']

# convert SrcParallel list of dicts to C array of SrcParallel structs
cdef void makeSrcParallelArray(list df_dict, SrcParallel *items, int num_items):

    cdef SrcParallel *item
    for i, el in enumerate(df_dict):
        if i >= num_items:
            break
        item = &items[i]
        item.t = el['t']
        item.node_from = el['node_from']
        item.node_to = el['node_to']
        item.flow = el['flow']

# convert ModelBus list of dicts to C array of ModelBus structs
cdef void makeModelBusArray(list df_dict, ModelBus *items, int num_items):

    cdef ModelBus *item
    for i, el in enumerate(df_dict):
        if i >= num_items:
            break
        item = &items[i]
        item.t = el['t']
        item.node = el['node']
        item.pg_ats = el['pg_ats']
        item.pn = el['pn']
        item.qg = el['qg']
        item.qn = el['qn']
        item.node_price_ats = el['node_price_ats']
        item.type = el['type']

# convert ModelLine list of dicts to C array of ModelLine structs
cdef void makeModelLineArray(list df_dict, ModelLine *items, int num_items):

    cdef ModelLine *item
    for i, el in enumerate(df_dict):
        if i >= num_items:
            break
        item = &items[i]
        item.t = el['t']
        item.node_from = el['node_from']
        item.node_to = el['node_to']
        item.pnum_actual = el['pnum_actual']
        item.pnum_max = el['pnum_max']
        item.ats_flow = el['ats_flow']
        item.p_from = el['p_from']
        item.p_to = el['p_to']
        item.q_from = el['q_from']
        item.q_to = el['q_to']

# convert ModelRge list of dicts to C array of ModelRge structs
cdef void makeModelRgeArray(list df_dict, ModelRge *items, int num_items):

    cdef ModelRge *item
    for i, el in enumerate(df_dict):
        if i >= num_items:
            break
        item = &items[i]
        item.t = el['t']
        item.rge = el['rge']
        item.node = el['node']
        item.pmin = el['pmin']
        item.pmax = el['pmax']
        item.p = el['p']
        item.node_price_ats = el['node_price_ats']
        item.pdg = el['pdg']

# convert ModelSection list of dicts to C array of ModelSection structs
cdef void makeModelSectionArray(list df_dict, ModelSection *items, int num_items):

    cdef ModelSection *item
    for i, el in enumerate(df_dict):
        if i >= num_items:
            break
        item = &items[i]
        item.t = el['t']
        item.sec_num = el['sec_num']
        item.node_from = el['node_from']
        item.node_to = el['node_to']
        item.vetv_state = el['vetv_state']
        item.dv = el['dv']
        item.sec_flow_ats = el['sec_flow_ats']
        item.sec_flow = el['sec_flow']
        item.pmin = el['pmin']
        item.pmax = el['pmax']

# convert ModelWsum list of dicts to C array of ModelWsum structs
cdef void makeModelWsumArray(list df_dict, ModelWsum *items, int num_items):

    cdef ModelWsum *item
    for i, el in enumerate(df_dict):
        if i >= num_items:
            break
        item = &items[i]
        item.t = el['t']
        item.rge_group = el['rge_group']
        item.rge = el['rge']
        item.wmax = el['wmax']
        item.grp_pmin = el['grp_pmin']
        item.grp_pmax = el['grp_pmax']
        item.grp_p = el['grp_p']
        item.grp_pmin_so = el['grp_pmin_so']
        item.grp_pmax_so = el['grp_pmax_so']
        item.grp_price = el['grp_price']

# convert SrcConsumer list of dicts to C array of SrcConsumer structs
cdef void makeSrcConsumerArray(list df_dict, SrcConsumer *items, int num_items):

    cdef SrcConsumer *item
    for i, el in enumerate(df_dict):
        if i >= num_items:
            break
        item = &items[i]
        item.gtp_code = el['gtp_code']
        item.p = el['p']
        item.pmax = el['pmax']
        item.loss = el['loss']