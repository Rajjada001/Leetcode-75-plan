# Write your MySQL query statement below
SELECT
eu.unique_id as unique_id, e.name from Employees e left Join
EmployeeUNI eu on eu.id = e.id