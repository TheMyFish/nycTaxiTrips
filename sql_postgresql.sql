select avg(trip_distance) as media_distancia_com_ate_dois_passageiros from tripstest
where passenger_count <=2

select vendor_id,sum(total_amount) from tripstest
group by vendor_id

select vendor_id,pickup_datetime,tip_amount,tolls_amount,total_amount from tripstest
where payment_type like 'Cash'
order by pickup_datetime

select vendor_id,pickup_datetime,tip_amount from tripstest
where pickup_datetime like '2012-03%'