select duplicated_count, unique_count from 
        (select sum(count) - 1 as duplicated_count from
        (select operator, num1, num2, count(*)
        from expression_data 
        group by operator, num1, num2
        having count(*) > 1) as d) as duplicated,
        
        (select sum(count) as unique_count from
        (select operator, num1, num2, count(*)
        from expression_data 
        group by operator, num1, num2
        having count(*) = 1) as u) as uniq

group by duplicated_count, unique_count;