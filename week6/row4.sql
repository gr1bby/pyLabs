select operator, cast(count(*)*100/(select count(*) 
                                    from expression_data) as decimal)
from expression_data 
group by operator;