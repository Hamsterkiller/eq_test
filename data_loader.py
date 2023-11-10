import pandas as pd
from typing import Dict, Union, Iterator
from datetime import date
import logging

import sqlalchemy.engine
import pandas as pd


def load_input_data(dt: date,
                    engine: sqlalchemy.engine.Engine,
                    logger: logging.Logger) -> Dict[str, Dict[str, pd.DataFrame]]:

    """
    Loads all needed input data
    :param dt:
    :param engine:
    :return:
    """

    schema = 'model1'

    ##### TOPOLOGY #####
    logger.debug('Loading TOPO_NODE data...')
    topo_node_query = f""" 
                select
                    node,
                    type,
                    unom,
                    vzd,
                    gsh,
                    bsh,
                    qg,
                    qn
                from
                    {schema}.dict_topo_node
                where
                        version = 0
                    and date = '{dt.isoformat()}'
                order by
                    node
            """
    topo_node_df = pd.read_sql(topo_node_query, engine)

    logger.debug('Loading TOPO_VETV data...')
    topo_vetv_query = f"""
                select
                    node_from,
                    node_to,
                    pnum,
                    type,
                    r,
                    x,
                    g,
                    b,
                    b_from,
                    b_to,
                    ktr,
                    kti
                from
                    {schema}.dict_topo_vetv
                where
                        version = 0
                    and date = '{dt.isoformat()}'
            """
    topo_vetv_df = pd.read_sql(topo_vetv_query, engine)

    logger.debug('Loading NODE_GEO data...')
    node_geo_query = f"""
                select
                    node,
                    cz_id,
                    oes_id,
                    zsp_id,
                    sub_id
                from
                    {schema}.dict_node_geo
                where
                        version = 0
                    and date = '{dt.isoformat()}'
            """
    node_geo_df = pd.read_sql(node_geo_query, engine)

    logger.debug('Loading TOPO_SECTION data...')
    topo_section_query = f"""
                select
                    sec_num,
                    node_from,
                    node_to,
                    dv,
                    forecast_type,
                    cz_id
                from
                    {schema}.dict_topo_section
                where
                        version = 0
                    and date = '{dt.isoformat()}'
            """
    topo_section_df = pd.read_sql(topo_section_query, engine)

    logger.debug('Loading TOPO_RGE data...')
    topo_rge_query = f"""
                    select
                        rge,
                        node,
                        fake_node
                    from
                        {schema}.dict_topo_rge
                    where
                            version = 0
                        and date = '{dt.isoformat()}'
                """
    topo_rge_df = pd.read_sql(topo_rge_query, engine)

    logger.debug('Loading TOPO_GTP_CON data...')
    topo_gtp_con_query = f"""
                        select
                            gtp_code,
                            node,
                            dist_coeff
                        from
                            {schema}.dict_topo_gtp_con
                        where
                                version = 0
                            and date = '{dt.isoformat()}'
                    """
    topo_gtp_con_df = pd.read_sql(topo_gtp_con_query, engine)

    logger.debug('Loading CONSUMERS data...')
    consumers_query = f"""
                        select
                            trader_code,
                            gtp_code,
                            is_own_needs,
                            is_esk,
                            is_gp,
                            is_system,
                            load_profile_type,
                            sub_id
                        from
                            {schema}.dict_consumers
                        where
                                version = 0
                            and date = '{dt.isoformat()}'
                        """
    consumers_df = pd.read_sql(consumers_query, engine)

    logger.debug('Loading TOPO_OPT_GES data...')
    topo_opt_ges_query = f"""
                            select
                                rge_group,
                                rge as rge_num,
                                type_opt
                            from
                                {schema}.dict_topo_opt_ges
                            where
                                    version = 0
                                and date = '{dt.isoformat()}'
                        """
    topo_opt_ges_df = pd.read_sql(topo_opt_ges_query, engine)

    logger.debug('Loading MODEL_BID data...')
    model_bid_query = f"""
                            select
                                hour as t,
                                rge,
                                node,
                                interval,
                                p_ats as p,
                                pmin,
                                pmax,
                                price
                            from
                                {schema}.model_bid
                            where
                                    version = 0
                                and date = '{dt.isoformat()}'
                        """
    model_bid_df = pd.read_sql(model_bid_query, engine)

    logger.debug('Loading MODEL_BID_CON data...')
    model_bid_con_query = f"""
                            select
                                hour as t,
                                gtp_code,
                                interval,
                                p_ats,
                                pmax,
                                price
                            from
                                {schema}.model_bid_con
                            where
                                    version = 0
                                and date = '{dt.isoformat()}'
                        """
    model_bid_con_df = pd.read_sql(model_bid_con_query, engine)

    logger.debug('Loading MODEL_BID_REASON data...')
    model_bid_reason_query = f"""
                                select
                                    hour as t,
                                    rge,
                                    coalesce(node_price_ats, 0) as price,
                                    code
                                from
                                    {schema}.model_bid_reason
                                where
                                        version = 0
                                    and date = '{dt.isoformat()}'
                            """
    model_bid_reason_df = pd.read_sql(model_bid_reason_query, engine)

    logger.debug('Loading SRC_SUPPLY data...')
    src_supply_query = f"""
                            select
                                hour as t,
                                zone,
                                price,
                                volume
                            from
                                {schema}.src_supply
                            where
                                    version = 0
                                and date = '{dt.isoformat()}'
                        """
    src_supply_df = pd.read_sql(src_supply_query, engine)

    logger.debug('Loading SRC_DEMAND data...')
    src_demand_query = f"""
                                select
                                    hour as t,
                                    zone,
                                    price,
                                    volume
                                from
                                    {schema}.src_supply
                                where
                                        version = 0
                                    and date = '{dt.isoformat()}'
                            """
    src_demand_df = pd.read_sql(src_demand_query, engine)

    logger.debug('Loading SRC_CONSUMER data...')
    src_consumer_query = f"""
                            select
                                hour as t,
                                gtp_code as gtp,
                                p,
                                pmax,
                                loss
                            from
                                {schema}.src_consumer
                            where
                                    version = 0
                                and date = '{dt.isoformat()}'
                        """
    src_consumer_df = pd.read_sql(src_consumer_query, engine)

    logger.debug('Loading SRC_PARALLEL data...')
    src_parallel_query = f"""
                            select
                                hour as t,
                                node_from,
                                node_to,
                                pnum,
                                flow
                            from
                                {schema}.src_parallel
                            where
                                    version = 0
                                and date = '{dt.isoformat()}'
                        """
    src_parallel_df = pd.read_sql(src_parallel_query, engine)

    logger.debug('Loading MODEL_BUS data...')
    model_bus_query = f"""
                            select
                                hour as t,
                                node,
                                pg_ats,
                                pn,
                                qg,
                                qn,
                                coalesce(node_price_ats, 0) as node_price_ats,
                                type
                            from
                                {schema}.model_bus
                            where
                                    version = 0
                                and date = '{dt.isoformat()}'
                        """
    model_bus_df = pd.read_sql(model_bus_query, engine)

    logger.debug('Loading MODEL_LINE data...')
    model_line_query = f"""
                                select
                                    hour as t,
                                    node_from,
                                    node_to,
                                    pnum_actual,
                                    pnum_max,
                                    ats_flow,
                                    p_from,
                                    p_to,
                                    q_from,
                                    q_to
                                from
                                    {schema}.model_line
                                where
                                        version = 0
                                    and date = '{dt.isoformat()}'
                            """
    model_line_df = pd.read_sql(model_line_query, engine)

    logger.debug('Loading MODEL_RGE data...')
    model_rge_query = f"""
                                select
                                    hour as t,
                                    rge,
                                    node,
                                    pmin,
                                    pmax,
                                    p_ats,
                                    coalesce(node_price_ats, 0) as node_price_ats,
                                    pdg
                                from
                                    {schema}.model_rge
                                where
                                        version = 0
                                    and date = '{dt.isoformat()}'
                            """
    model_rge_df = pd.read_sql(model_rge_query, engine)

    logger.debug('Loading MODEL_SECTION data...')
    model_section_query = f"""
                                select
                                    hour as t,
                                    sec_num,
                                    node_from,
                                    node_to,
                                    vetv_state,
                                    dv,
                                    flow_ats,
                                    flow_reconstructed,
                                    pmin,
                                    pmax
                                from
                                    {schema}.model_section_lines
                                where
                                        version = 0
                                    and date = '{dt.isoformat()}'
                            """
    model_section_df = pd.read_sql(model_section_query, engine)

    logger.debug('Loading MODEL_WSUM data...')
    model_wsum_query = f"""
                            select
                                hour as t,
                                rge_group,
                                rge,
                                wmax,
                                grp_pmin,
                                grp_pmax,
                                grp_p_ats,
                                grp_pmin_so,
                                grp_pmax_so,
                                grp_node_price_ats
                            from
                                {schema}.model_wsum_group
                            where
                                    version = 0
                                and date = '{dt.isoformat()}'
                        """
    model_wsum_df = pd.read_sql(model_wsum_query, engine)

    result = {
        'topology': {
            'topo_node': topo_node_df,
            'topo_vetv': topo_vetv_df,
            'topo_section': topo_section_df,
            'node_geo': node_geo_df,
            'topo_rge': topo_rge_df,
            'topo_gtp_con': topo_gtp_con_df,
            'topo_opt_ges': topo_opt_ges_df,
            'dict_consumers': consumers_df
        },
        'bid_data': {
            'model_bid': model_bid_df,
            'model_bid_con': model_bid_con_df,
            'model_bid_reason': model_bid_reason_df
        },
        'model_data': {
            'src_supply': src_supply_df,
            'src_demand': src_demand_df,
            'src_consumer': src_consumer_df,
            'parallel_flows': src_parallel_df,
            'model_rge': model_rge_df,
            'model_section': model_section_df,
            'model_bus': model_bus_df,
            'model_line': model_line_df,
            'model_wsum': model_wsum_df
        }
    }

    return result











