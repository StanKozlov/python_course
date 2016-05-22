select * from Users;
select count(*) from Users;
select count(*) from Users where birth_date <= date("1970-05-12");
select country, count(*) from Users group by country;
select name, count(*) from Users group by name having count(*) > 1;
select count(*) from Orders where created like "2016%";
select date(created), count(*) from Orders group by date(created) order by count(date(created)) desc limit 1;
select (select count(*) from Orders where paid = 0) * 100.0 / (select count(*) from Orders);
select * from Goods where name like "%bread%";
select good_id, Goods.name, count(*) from GoodsInOrders inner join Goods on good_id = Goods.id group by good_id order by count(good_id) desc limit 10);
select sum(Goods.price) from Goods inner join GoodsInOrders on Goods.id = GoodsInOrders.good_id where Goods.id in (select GoodsInOrders.good_id from GoodsInOrders inner join Orders on GoodsInOrders.order_id = Orders.id where Orders.id in (select id from Orders where paid = 1 and date(created) >= date("2016-01-01")));

select name from Goods inner join GoodsInOrders on Goods.id = GoddsInOrders.good_id where GoodsInOrders.good_id in (select Orders.id from Orders inner join Users on Orders.user_id = Users.id where Users.id in (select id from Users where gender = "F")) and GoodsInOrders.good_id order by count(GoodsInOrders.good_id) desc limit 10;

select name from Users inner join Orders on Users.id = Orders.user_id where Orders.user_id in (select Orders.user_id from Orders inner join GoodsInOrders on Orders.id = GoodsInOrders.order_id where GoodsInOrders.order_id in (select GoodsInOrders inner join Goods on GoodsInOrders.good_id = Goods.id where Goods.id in (select id from Goods where Goods.units = "KG" and Goods.quantity order by Goods.quantity desc))) limit 1;
