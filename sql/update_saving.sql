UPDATE savings
SET 
amount = %s,
interest = %s,
period = %s
WHERE id = %s;