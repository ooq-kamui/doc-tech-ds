
# unix sever maintenance


## lib が見つからない err

```
fish: error while loading shared libraries: libstdc++.so.6: cannot open shared object file: No such file or directory
```

の err が出たとき

環境変数

```
LD_LIBRARY_PATH
```

を設定する

設定する path を調べる

ある cmd で使用している lib を調べる

ex

```
ldd /home/linuxbrew/.linuxbrew/bin/fish
```

```
/home/linuxbrew/.linuxbrew/bin/fish: /lib64/libstdc++.so.6: version `GLIBCXX_3.4.30' not found (required by /home/linuxbrew/.linuxbrew/bin/fish)
    linux-vdso.so.1 (0x00007ffcb8673000)
    libncursesw.so.6 => /home/linuxbrew/.linuxbrew/opt/ncurses/lib/libncursesw.so.6 (0x00007fbcd26f0000)
    libpcre2-32.so.0 => /home/linuxbrew/.linuxbrew/opt/pcre2/lib/libpcre2-32.so.0 (0x00007fbcd2662000)
    libstdc++.so.6 => /lib64/libstdc++.so.6 (0x00007fbcd2000000)
    libm.so.6 => /lib64/libm.so.6 (0x00007fbcd2325000)
    libc.so.6 => /lib64/libc.so.6 (0x00007fbcd1c00000)
    /home/linuxbrew/.linuxbrew/lib/ld.so => /lib64/ld-linux-x86-64.so.2 (0x00007fbcd2771000)
    libgcc_s.so.1 => /lib64/libgcc_s.so.1 (0x00007fbcd2641000)
```

`/lib64` を `LD_LIBRARY_PATH` に設定する

```
LD_LIBRARY_PATH=/lib64
export LD_LIBRARY_PATH
```

複数 dir 指定する場合は `:` 区切り





