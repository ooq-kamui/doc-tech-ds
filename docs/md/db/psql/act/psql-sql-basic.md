
# psql


## select

```
select * from tst;
```


## ins

```
insert into tbl01
  (id,     name) VALUES
  ( 1, 'name01'),
  ( 2, 'name02')
;
```


## upd

```
update tbl01 set
  col01 = val01,
  col02 = val02
where col03 = val03
  and col04 = val04
;
```


## delete

```
delete from tbl01
where col03 = val03
  and col04 = val04
;
```


