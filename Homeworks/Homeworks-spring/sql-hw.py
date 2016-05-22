import sqlite3 as sq


def unpaid(user_id):
    with sq.connect("/home/hamster/data.sqlite") as database:
        cur = database.cursor()
    query = ("select Users.name, Orders.id, sum(Goods.price) from Users "
             "inner join Orders on Orders.user_id = Users.id inner join "
             "GoodsInOrders on GoodsInOrders.order_id = Orders.id inner "
             "join Goods on Goods.id = GoodsInOrders.good_id where "
             "Users.id = ? and Orders.paid = 0 group by Orders.id;")
    data = cur.execute(query, [user_id]). fetchall()
    return data

print(unpaid(23))