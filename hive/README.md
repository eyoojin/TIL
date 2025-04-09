# hive
- hive 서버 실행
    - 위치: `~/hive-3.1.3`
    - `hiveserver2 --hiveconf hive.server2.thrift.port=10000 --hiveconf hive.root.logger=DEBUG, console`

- beeline 실행
    - 새 터미널 생성
    - `beeline> !connect jdbc:hive2://localhost:10000`

# HiveQl

## managed table
- 테이블 생성
```sql
CREATE TABLE employees
(
    emp_no      INT,
    birth_date  DATE,
    firsh_name  STRING,
    last_name   STRING,
    gender      STIING,
    hire_date   DATE,
    dept_no     STRING
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n';
```

- 테이블 확인 `SHOW tables;`

- 데이터 업로드
```sql
LOAD DATA LOCAL INPATH '/home/ubuntu/damf2/data/employees'
INTO TABLE empolyees;
```

- 데이터 확인
```sql
SELECT * FROM employees LIMIT 10;
```

- 전체 데이터 확인
```sql
SELECT COUNT(*) FROM employees;
```

- 생일이 같은 사람 수 카운트
```sql
SELECT birth_date, COUNT(birth_date)
FROM employees
GROUP BY birth_date
LIMIT 10;
```

- 테이블 삭제 `DROP TABLE employees;`
    - HDFS에 올라간 파일도 같이 삭제
