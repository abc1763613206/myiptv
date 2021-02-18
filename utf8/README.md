### UTF-8 万岁
本目录提供了 UTF-8 格式的各节目源，可用于应付对编码要求严格的播放器或供 Git 比较用。   
目前采用如下指令人工生成：
```bash
find . -type f -name '*.txt' -exec sh -c "iconv -f GBK -t UTF-8 {}  > ~/temp" \; -exec mv ~/temp utf8/{} \;
iconv -f GBK -t UTF-8 data.csv > utf8/data.csv
```

-----

- 总合并直播源：
  - 带来源：[`https://cdn.jsdelivr.net/gh/abc1763613206/myiptv@latest/utf8/merged.txt`](https://cdn.jsdelivr.net/gh/abc1763613206/myiptv@latest/utf8/merged.txt)
  - 不带来源： [`https://cdn.jsdelivr.net/gh/abc1763613206/myiptv@latest/utf8/merged-simple.txt`](https://cdn.jsdelivr.net/gh/abc1763613206/myiptv@latest/utf8/merged-simple.txt)
- 分类
  - `cctv`
    - 带来源：[`https://cdn.jsdelivr.net/gh/abc1763613206/myiptv@latest/utf8/groups/cctv.txt`](https://cdn.jsdelivr.net/gh/abc1763613206/myiptv@latest/utf8/groups/cctv.txt)
    - 不带来源：[`https://cdn.jsdelivr.net/gh/abc1763613206/myiptv@latest/utf8/groups/cctv-simple.txt`](https://cdn.jsdelivr.net/gh/abc1763613206/myiptv@latest/utf8/groups/cctv-simple.txt)
  - `difang`
    - 带来源：[`https://cdn.jsdelivr.net/gh/abc1763613206/myiptv@latest/utf8/groups/weishi.txt`](https://cdn.jsdelivr.net/gh/abc1763613206/myiptv@latest/utf8/groups/weishi.txt)
    - 不带来源：[`https://cdn.jsdelivr.net/gh/abc1763613206/myiptv@latest/utf8/groups/weishi-simple.txt`](https://cdn.jsdelivr.net/gh/abc1763613206/myiptv@latest/utf8/groups/weishi-simple.txt)
  - `difang`
    - 带来源：[`https://cdn.jsdelivr.net/gh/abc1763613206/myiptv@latest/utf8/groups/difang.txt`](https://cdn.jsdelivr.net/gh/abc1763613206/myiptv@latest/utf8/groups/difang.txt)
    - 不带来源：[`https://cdn.jsdelivr.net/gh/abc1763613206/myiptv@latest/utf8/groups/difang-simple.txt`](https://cdn.jsdelivr.net/gh/abc1763613206/myiptv@latest/utf8/groups/difang-simple.txt)