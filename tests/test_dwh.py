import pytest
from rubixinsights import create_postgres_insert_sql


def test_create_postgres_insert_sql():
    render_parameters = {
        'channel': 'analytics',
        'table_name': 'device_report',
        'processed_columns': {
            'data_source': 'data_source',
            'TO_DATE("ga:date", \'YYYY-MM-DD\')': '"ga:date"',
            '"ga:accountId"': '"ga:accountId"',
            '"ga:country"': '"ga:country"',
            '"ga:region"': '"ga:region"',
            '"ga:metro"': '"ga:metro"',
            '"ga:sourceMedium"': '"ga:sourceMedium"',
            '"ga:source"': '"ga:source"',
            '"ga:medium"': '"ga:medium"',
            '"ga:campaign"': '"ga:campaign"',
            '"ga:deviceCategory"': '"ga:deviceCategory"',
            '"ga:users"::numeric': '"ga:users"',
            '"ga:newUsers"::numeric': '"ga:newUsers"',
            '"ga:pageviews"::numeric': '"ga:pageviews"',
            '"ga:sessions"::numeric': '"ga:sessions"',
            '"ga:sessionDuration"::numeric': '"ga:sessionDuration"',
            '"ga:bounces"::numeric': '"ga:bounces"'
        },
        'dimensions': [
            'data_source',
            '"ga:date"',
            '"ga:accountId"',
            '"ga:country"',
            '"ga:region"',
            '"ga:metro"',
            '"ga:sourceMedium"',
            '"ga:source"',
            '"ga:medium"',
            '"ga:campaign"',
            '"ga:deviceCategory"'
        ],
        'metrics': [
            '"ga:users"',
            '"ga:newUsers"',
            '"ga:pageviews"',
            '"ga:sessions"',
            '"ga:sessionDuration"',
            '"ga:bounces"'
        ]
    }

    expected_sql = """
    WITH processed_raw_analytics_device_report AS (
        SELECT
            data_source AS data_source,
            TO_DATE("ga:date", 'YYYY-MM-DD') AS "ga:date",
            "ga:accountId" AS "ga:accountId",
            "ga:country" AS "ga:country",
            "ga:region" AS "ga:region",
            "ga:metro" AS "ga:metro",
            "ga:sourceMedium" AS "ga:sourceMedium",
            "ga:source" AS "ga:source",
            "ga:medium" AS "ga:medium",
            "ga:campaign" AS "ga:campaign",
            "ga:deviceCategory" AS "ga:deviceCategory",
            "ga:users"::numeric AS "ga:users",
            "ga:newUsers"::numeric AS "ga:newUsers",
            "ga:pageviews"::numeric AS "ga:pageviews",
            "ga:sessions"::numeric AS "ga:sessions",
            "ga:sessionDuration"::numeric AS "ga:sessionDuration",
            "ga:bounces"::numeric AS "ga:bounces"
        FROM raw.raw_analytics_device_report
    )
    INSERT INTO
    analytics.device_report (
        data_source,
        "ga:date",
        "ga:accountId",
        "ga:country",
        "ga:region",
        "ga:metro",
        "ga:sourceMedium",
        "ga:source",
        "ga:medium",
        "ga:campaign",
        "ga:deviceCategory",
        "ga:users",
        "ga:newUsers",
        "ga:pageviews",
        "ga:sessions",
        "ga:sessionDuration",
        "ga:bounces"
    )
    SELECT
    DISTINCT ON (data_source,"ga:date","ga:accountId","ga:country","ga:region","ga:metro","ga:sourceMedium","ga:source","ga:medium","ga:campaign","ga:deviceCategory") * FROM processed_raw_analytics_device_report
    ON CONFLICT (data_source,"ga:date","ga:accountId","ga:country","ga:region","ga:metro","ga:sourceMedium","ga:source","ga:medium","ga:campaign","ga:deviceCategory") DO UPDATE SET 
        "ga:users" = excluded."ga:users",
        "ga:newUsers" = excluded."ga:newUsers",
        "ga:pageviews" = excluded."ga:pageviews",
        "ga:sessions" = excluded."ga:sessions",
        "ga:sessionDuration" = excluded."ga:sessionDuration",
        "ga:bounces" = excluded."ga:bounces"
    ;
    """

    sql = create_postgres_insert_sql(render_parameters)
    assert sql == expected_sql
