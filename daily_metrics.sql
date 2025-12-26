CREATE OR REPLACE TABLE `raw_data.daily_metrics` AS
SELECT
  event_date,
  country,
  platform,


  COUNT(DISTINCT user_id) as DAU,

  
  SUM(iap_revenue) as total_iap_revenue,
  SUM(ad_revenue) as total_ad_revenue,

 
  SAFE_DIVIDE(SUM(iap_revenue + ad_revenue), COUNT(DISTINCT user_id)) as arpdau,

 
  SUM(match_start_count) as matches_started,
  SAFE_DIVIDE(SUM(match_start_count), COUNT(DISTINCT user_id)) as match_per_dau,

  
  SAFE_DIVIDE(SUM(victory_count), SUM(match_end_count)) as win_ratio,

  
  SAFE_DIVIDE(SUM(server_connection_error), COUNT(DISTINCT user_id)) as server_error_per_dau

FROM
  `raw_data.daily_metrics_raw`
GROUP BY
  1, 2, 3;