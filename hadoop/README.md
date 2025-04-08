# hadoop command

- `ls`: 폴더, 파일 목록 출력
    - hdfs dfs -ls <경로>
    - `hdfs dfs -ls /`

- `mkdir`: 폴더 생성
    - hdfs dfs -mkdir <폴더명>
    - `hdfs dfs -mkdir /bm`

- `put`: 파일 업로드
    - hdfs dfs -put <파일 경로> <위치>
    - `hdfs dfs -put /kawai/ruka.txt /bm`

- `cat`: 파일 전체 출력
    - hdfs dfs -cat <파일 경로>
    - `hdfs dfs -cat /bm/ruka.txt`

- `head`: 파일의 앞부분 출력
    - hdfs dfs -head <파일 경로>
    - `hdfs dfs -head /bm/ruka.txt`

- `tail`: 파일의 뒷부분 출력
    - hdfs dfs -tail <파일 경로>
    - `hdfs dfs -tail /bm/ruka.txt`

- `rm`: 파일 삭제
    - hdfs dfs -rm <파일 경로>
    - `hdfs dfs -rm /bm/ruka.txt`

- `rm -r`: 폴더 삭제
    - hdfs dfs -rm -r <폴더 경로>
    - `hdfs dfs -rm -r /bm`

# MapReduce
## 0. wordcount
- `hdfs dfs -put text.txt /TIL/input`
```
hadoop jar ~/hadoop-3.3.6/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar\
 -input /TIL/input/text.txt\
 -output /TIL/output/wordcount\
 -mapper 'python3 /home/ubuntu/damf2/TIL/hadoop/0.wordcount/mapper.py'\
 -reducer 'python3 /home/ubuntu/damf2/TIL/hadoop/0.wordcount/reducer.py'
```

## 1. movie-rate-avg
- `hdfs dfs -put ~/damf2/data/ml-25m/ratings.csv /TIL/input`
```
hadoop jar ~/hadoop-3.3.6/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar\
 -input TIL/input/ratings.csv\
 -output TIL/output/movie-rate-avg\
 -mapper 'python3 /home/ubuntu/damf2/TIL/hadoop/1.movie-rate-avg/mapper.py'\
 -reducer 'python3 /home/ubuntu/damf2/TIL/hadoop/1.movie-rate-avg/reducer.py'
```

## 2. log-time
- `hdfs dfs -put ~/damf2/data/access.log /TIL/input`
```
hadoop jar ~/hadoop-3.3.6/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar\
 -input /TIL/input/access.log\
 -output /TIL/output/log-time\
 -mapper 'python3 /home/ubuntu/damf2/TIL/hadoop/2.log-time/mapper.py'\
 -reducer 'python3 /home/ubuntu/damf2/TIL/hadoop/2.log-time/reducer.py'
```