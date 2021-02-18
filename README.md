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

**现已提供从 [ EPG 频道列表](http://epg.51zmt.top:8000/) 匹配的 `m3u8` 文件！详见 [epg/README.md](epg/README.md)**


- 由于目前主要还是自用，故打算每次手动生成。
- `merged` 为全部直播源，`groups` 文件夹里为各个直播源的分类。
- 带 `simple` 的为纯净格式**（不带来源与分辨率）**
- 目前~~只输出了 `txt` 格式~~，急着用的可以自行用 [Telelist](https://guihet.com/tvlive-telelist.html) 进行转换，其他格式慢慢写。
- 关于**分类**： `difang` 分类为地方频道与 IPTV 特色频道（含部分海外频道），`cctv` 为 CCTV 下属频道（含部分特色频道与 CGTN），`weishi` 为地方卫视（含凤凰卫视）
- 关于来源与命名：频道命名尽量遵循[ EPG 频道列表](http://epg.51zmt.top:8000/) 中的格式进行命名统一以确保正确匹配；来源命名多使用 IPIP 进行 IP 段标注，`difang` 分类为目测（小地方台基本上只有官方供源，要是挨个查 IP 的话会出事）
- 尽量进行命名统一，详见[命名映射表](MAPPING.md)
- ~~现阶段可以下载直播源上传至 [ EPG 频道列表](http://epg.51zmt.top:8000/)自动匹配节目表。~~
- 脚本所做的工作：通过 `requests` 和 `ffprobe` 检测直播源，后进行分类，最后用有效信息输出新的 `csv`。
- 比较重要的一点：我主要使用家机（当前是北方移动）进行检测，直播源可用性对地区依赖较大，有必要时请自行跑脚本检测。
- 脚本会去除仅音频/视频的直播源，所以该源**显然不含音频广播/无声直播**。
- 部分直播源限制连接数，如有需要请自行设置延时。
- 不加组播地址，理论上公网均可看。
- TODO：添加新格式、新直播源，优化脚本。

## 免责声明

请注意，本仓库中收集的节目源**全部来自网络**，仅供教学交流用途，具体版权**归各个版权方所有**。        
本仓库中并没有存储版权相关的视频文件，仅包含其他用户所提供的公开可用的视频流链接。且据我们了解，这些链接也是版权所有者故意公开的。    
如果这些节目源中的任何链接侵犯了您作为版权所有者的权利，您可以通过发送 Pull Request 或打开一个 Issue 来删除它们。     

另外请注意，我们**无法控制**链接的目的地及其要显示的内容，因此仅仅从我们的仓库中删除链接并不能从网络上彻底删除该内容。链接并不直接侵犯版权，且我们并不提供相关节目的复制，因此这并不是发送 DMCA 的正当理由。如果您要从网络上**彻底**删除这些内容，您应当联系该节目源的**原始提供者**以及**实际托管这些内容的网站主机**（不是 GitHub 本身，更不是该仓库的维护者）。

该免责声明参考了 [iptv-org/iptv](https://github.com/iptv-org/iptv) ，在此表示感谢。    

下面列出了**显式**引用节目源的来源，在此向提供者一并表示感谢：  
- [iptv-org/iptv](https://github.com/iptv-org/iptv)
- [北邮 IVI 测试](http://ivi.bupt.edu.cn/)
- [imDazui/Tvlist-awesome-m3u-m3u8](https://github.com/imDazui/Tvlist-awesome-m3u-m3u8)