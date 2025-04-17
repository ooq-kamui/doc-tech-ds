
# postgres


## serial seq

### seq list 取得

```
SELECT * FROM pg_sequences;
```

### table, col の serial seq name 確認

```
select pg_get_serial_sequence('t_kaikake_zandaka', 'id');
```

### serial seq val 確認

```
select currval('public.animal_id_seq');

 currval 
---------
     1
```

or

```
select last_value from test_record_id_seq ;
```


### serial seq val set

```
SELECT setval('public.animal_id_seq', 10000);
 setval 
---------
 10000
```

### seq 1 up

```
select nextval ('test_record_id_seq');
```



## unique key

### unique key 変更

```
ALTER TABLE t_kaikake_zandaka
ADD constraint xxxxxxxxxx_key
unique(shiharai_saki_no,konkai_shime_day);

-- UNIQUE (shiharai_saki_no,konkai_shime_day)
```

### unique key 削除

```
ALTER TABLE t_kaikake_zandaka
DROP constraint t_kaikake_zandaka_konkai_shime_day_key ;

ALTER TABLE t_kaikake_zandaka
DROP constraint t_kaikake_zandaka_shiharai_saki_no_key ;
```


