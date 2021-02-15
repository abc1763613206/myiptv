# myiptv
自用直播源集合，附带检测与分类功能。

### 为啥搞
TLDR: 太闲了。

- 自己有收集直播源的爱好，和录制直播源的需求。
- 一些软件自带的直播源太过难用。
- 网上现有的直播源太杂，且缺乏检测。
- 一些大源缺乏持续更新，如 `iptv-org`。

### 使用指南与 TODO

每次进行大更新后都会进行一次 release ，所以您可以在 jsDelivr 获得最新更新。
（可能会出现编码问题，如有此类症状请 Issue 区提一下，附上所用软件。）

- 总合并直播源：
  - 带来源：[`https://cdn.jsdelivr.net/gh/abc1763613206/myiptv@latest/merged.txt`](https://cdn.jsdelivr.net/gh/abc1763613206/myiptv@latest/merged.txt)
  - 不带来源： [`https://cdn.jsdelivr.net/gh/abc1763613206/myiptv@latest/merged-simple.txt`](https://cdn.jsdelivr.net/gh/abc1763613206/myiptv@latest/merged-simple.txt)
- 分类
  - `cctv`
    - 带来源：[`https://cdn.jsdelivr.net/gh/abc1763613206/myiptv@latest/groups/cctv.txt`](https://cdn.jsdelivr.net/gh/abc1763613206/myiptv@latest/groups/cctv.txt)
    - 不带来源：[`https://cdn.jsdelivr.net/gh/abc1763613206/myiptv@latest/groups/cctv-simple.txt`](https://cdn.jsdelivr.net/gh/abc1763613206/myiptv@latest/groups/cctv-simple.txt)
  - `difang`
    - 带来源：[`https://cdn.jsdelivr.net/gh/abc1763613206/myiptv@latest/groups/weishi.txt`](https://cdn.jsdelivr.net/gh/abc1763613206/myiptv@latest/groups/weishi.txt)
    - 不带来源：[`https://cdn.jsdelivr.net/gh/abc1763613206/myiptv@latest/groups/weishi-simple.txt`](https://cdn.jsdelivr.net/gh/abc1763613206/myiptv@latest/groups/weishi-simple.txt)
  - `difang`
    - 带来源：[`https://cdn.jsdelivr.net/gh/abc1763613206/myiptv@latest/groups/difang.txt`](https://cdn.jsdelivr.net/gh/abc1763613206/myiptv@latest/groups/difang.txt)
    - 不带来源：[`https://cdn.jsdelivr.net/gh/abc1763613206/myiptv@latest/groups/difang-simple.txt`](https://cdn.jsdelivr.net/gh/abc1763613206/myiptv@latest/groups/difang-simple.txt)



-----

- 由于目前主要还是自用，故打算每次手动生成。
- `merged` 为全部直播源，`groups` 文件夹里为各个直播源的分类。
- 带 `simple` 的为纯净格式**（不带来源与分辨率）**
- 目前只输出了 `txt` 格式，急着用的可以自行用 [Telelist](https://guihet.com/tvlive-telelist.html) 进行转换，其他格式慢慢写。
- 关于**分类**： `difang` 分类为地方频道与 IPTV 特色频道（含部分海外频道），`cctv` 为 CCTV 下属频道（含部分特色频道与 CGTN），`weishi` 为地方卫视（含凤凰卫视）
- 关于来源与命名：频道命名尽量遵循[ EPG 频道列表](http://epg.51zmt.top:8000/) 中的格式进行命名统一以确保正确匹配；来源命名多使用 IPIP 进行 IP 段标注，`difang` 分类为目测（小地方台基本上只有官方供源，要是挨个查 IP 的话会出事）
- 现阶段可以下载直播源上传至 [ EPG 频道列表](http://epg.51zmt.top:8000/)自动匹配节目表。
- 脚本所做的工作：通过 `requests` 和 `ffprobe` 检测直播源，后进行分类，最后用有效信息输出新的 `csv`。
- 比较重要的一点：我主要使用家机（当前是北方移动）进行检测，直播源可用性对地区依赖较大，有必要时请自行跑脚本检测。
- 脚本会去除仅音频/视频的直播源，所以该源显然不含音频广播/无声直播。
- 部分直播源限制连接数，如有需要请自行设置延时。
- TODO：添加新格式、新直播源，优化脚本。

