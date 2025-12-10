create table df
(Region varchar(50), 
Soil_Type varchar(10),
Crop varchar(20),
Rainfall_mm DECIMAL(6,3),
Temperature_Celcius DECIMAL(5,3),
Fertilizer_Used varchar(10),
Irrigation_Used varchar(10),
weather_condition varchar(10),
day_to_harvest smallint,
Yield DECIMAL(4,3)
) ;

SELECT * FROM df 
select count(*) from df
select * from df where crop = 'Maize' order by yield DESC; 

--cek boxplot yang outlier
select crop, weather_condition, count(*) from df where Yield > 9  group by crop, weather_condition;
select crop, weather_condition, count(*) from df where Yield < 2 group by crop, weather_condition;

--cek apakah ada data yang kosong
select
	sum(case when region IS NULL THEN 1 ELSE 0 END) AS null_region,
	sum(case when soil_type IS NULL THEN 1 ELSE 0 END) AS null_soil,
	sum(case when crop IS NULL THEN 1 ELSE 0 END) AS null_crop,
	sum(case when rainfall_mm IS NULL THEN 1 ELSE 0 END) AS null_rainfall,
	sum(case when temperature_celcius IS NULL THEN 1 ELSE 0 END) AS null_temperature,
	sum(case when fertilizer_used IS NULL THEN 1 ELSE 0 END) AS null_fertilizer,
	sum(case when irrigation_used IS NULL THEN 1 ELSE 0 END) AS null_irrigation,
	sum(case when weather_condition IS NULL THEN 1 ELSE 0 END) AS null_weather,
	sum(case when day_to_harvest IS NULL THEN 1 ELSE 0 END) AS null_harvest,
	sum(case when yield IS NULL THEN 1 ELSE 0 END) AS null_yield
from df;

--cek kategori data
select 
	count(distinct region) AS region,
	count(distinct soil_type)AS soil_type,
	count(distinct crop)AS Crop,
	count(distinct weather_condition) AS weather_condition
from df;

--cek duplikasi data
select 
	region, soil_type, crop, rainfall_mm, temperature_celcius,fertilizer_used,
	irrigation_used, weather_condition, day_to_harvest,
	yield,
	COUNT(*) AS Count
from df
group by region, soil_type, crop, rainfall_mm, temperature_celcius,fertilizer_used,
	irrigation_used, weather_condition, day_to_harvest,
	yield
having count(*) > 1;

--cek statistik dasar
SELECT
    COUNT(*) AS total_rows,
    MIN(rainfall_mm) AS min_rainfall,
    MAX(rainfall_mm) AS max_rainfall,
    AVG(rainfall_mm) AS avg_rainfall,
    STDDEV(rainfall_mm) AS stddev_rainfall,
    MIN(temperature_celcius) AS min_temp,
    MAX(temperature_celcius) AS max_temp,
    AVG(temperature_celcius) AS avg_temp,
    STDDEV(temperature_celcius) AS stddev_temp
FROM df;

SELECT
    irrigation_Used,
    COUNT(*) AS irrigation_used,
    AVG(yield) AS avg_yield
FROM df
GROUP BY irrigation_used
ORDER BY avg_yield DESC;


SELECT
    fertilizer_Used, crop,
    AVG(yield) AS avg_yield
FROM df
GROUP BY fertilizer_used, crop
ORDER BY avg_yield DESC;

--cek apa ada imbalance data
SELECT soil_type, COUNT(*) AS total
FROM df
GROUP BY soil_type
ORDER BY total DESC;

SELECT weather_condition, COUNT(*) AS total
FROM df
GROUP BY weather_condition
ORDER BY total DESC;

select CROP, COUNT(crop) from df GROUP BY crop;


