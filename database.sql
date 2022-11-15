-- https://leetcode.com/problems/capital-gainloss/description/
-- Write an SQL query to report the Capital gain/loss for each stock.
-- The Capital gain/loss of a stock is the total gain or loss after buying and selling the stock one or many times.
-- Return the result table in any order.

select s.stock_name, sum(
    case when operation = 'Buy' then -1 * s.price
    else s.price
    end) capital_gain_loss
from Stocks s
group by s.stock_name;

-- https://leetcode.com/problems/market-analysis-i/
-- Write an SQL query to find for each user, the join date and the number of orders they made as a buyer in 2019.
-- Return the result table in any order.
select u.user_id buyer_id,
       u.join_date,
       (select count(*) from Orders o where YEAR(o.order_date) = '2019' and u.user_id = o.buyer_id) as "orders_in_2019"
from Users u;

-- https://leetcode.com/problems/combine-two-tables/description/
-- Write an SQL query to report the first name, last name, city, and state of each person in the Person table. If the address of a personId is not present in the Address table, report null instead.
select p.firstName, p.lastName, a.city, a.state
from Person p left join Address a on p.personId = a.personId;
