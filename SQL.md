1. Get all statuses, not repeating, alphabetically ordered
```bash
SELECT DISTINCT status
FROM tasks
ORDER BY status;
```
2. Get the count of all tasks in each project, ordered by task count descending
```bash
SELECT p.name AS project_name, COUNT(t.id) AS task_count
FROM projects AS p
JOIN tasks AS t ON t.project_id = p.id
GROUP BY p.id, p.name
ORDER BY task_count DESC;
```
3. Get the count of all tasks in each project, ordered by project name
```bash
SELECT p.name AS project_name, COUNT(t.id) AS task_count
FROM projects AS p
JOIN tasks AS t ON t.project_id = p.id
GROUP BY p.id, p.name
ORDER BY p.name;
```
4. Get tasks for all projects whose name begins with the letter "N"
```bash
SELECT t.* FROM tasks AS t
JOIN projects AS p ON p.id = t.project_id
WHERE p.name LIKE 'N%';
```
5. Projects containing 'a' in the middle of the name, with task count
```bash
SELECT p.name AS project_name,COUNT(t.id) AS task_count
FROM projects AS p
LEFT JOIN tasks AS t ON t.project_id = p.id
WHERE p.name LIKE '%a%'          
  AND p.name NOT LIKE 'a%'       
  AND p.name NOT LIKE '%a'       
GROUP BY p.id, p.name
ORDER BY p.name;
```
6. Tasks with duplicate names, ordered alphabetically
```bash
SELECT name FROM tasks
GROUP BY name
HAVING COUNT(*) > 1
ORDER BY name;
```
7. Tasks with several exact matches of both name AND status, from project 'Delivery', ordered by match count
```bash
SELECT t.name, t.status, COUNT(*) AS match_count
FROM tasks AS t
JOIN projects AS p ON p.id = t.project_id
WHERE p.name = 'Delivery'
GROUP BY t.name, t.status
HAVING COUNT(*) > 1
ORDER BY match_count DESC;
```
8.Project names with more than 10 tasks in status 'completed', ordered by project_id
```bash
SELECT p.name AS project_name
FROM projects AS p
JOIN tasks AS t ON t.project_id = p.id
WHERE t.status = 'completed'
GROUP BY p.id, p.name
HAVING COUNT(t.id) > 10
ORDER BY p.id;
```