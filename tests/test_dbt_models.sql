-- exmpl: Unit-Test for DBT-Models
SELECT * FROM {{ ref('staging_weather') }} WHERE temperature IS NOT NULL;