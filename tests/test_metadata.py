    metadata = Metadata(
        'postgres://insights_analyst:jXVaexgZ86CcLH3y@dev-insights-dwh.c5adq8vkoh3l.us-east-1.rds.amazonaws.com:5432/insightsdwh', 
        'facebook'
    )
    # metadata.update_as_succeeded("test", "test", "2021-01-01")
    metadata.validate_if_need_the_load("act_283849375686242", "age_gender_report", "2021-03-24")