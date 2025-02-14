## 「事实上」的停止更新
`myiptv` 这个项目已经过去了接近4年的时间，从最初的手动筛选到后来的自动化脚本，我们不难得到一个事实：要想在国内维护一个「全国通用」的、门槛较低的 IPTV 直播源，已经变得越来越难。   
或许是出于版权原因，又或许是出于典中典的跨省结算政策，以往的公开源正在慢慢退化。其中有的是走向了强鉴权，不得不使用第三方不太可信的 PHP 进行中转（连什么时候被替换成广告都不知道），有的则采取更省事的方法：仅省内同运营商可用。后者的方式诚然省事，但也丧失了这个项目「全国通用」的意义。      
4年过去，我们也可以看到一批又一批的项目如雨后春笋般出现，其中一些「自动更新」的仓库基本上都采取了竭泽而渔的方式：扫描更上层的仓库，或者直接使用 Fofa 等网络测绘平台对着「酒店源」等平台一通爆搜，甚至滥用各类防护不当的 udpxy 组播转发。这样做的结果是，源的质量越来越差，而且一旦被发布出来基本上就是见光死，这对于私有源的维护者来说是一种极大的打击。
综上所述，我认为这个项目事实上已经失去了继续维护的意义，如果您是一般路过的游客，您可以在 GitHub 上找到更暴力省事的实现，只需定时更新一下就行；如果您是源的制作者，我将工具链稍微打磨了下，您可以根据您的需要自行使用。

再见！

-------

# myiptv


### 为啥搞
TLDR: 太闲了。

- 自己有收集直播源的爱好，和录制直播源的需求。
- 一些软件自带的直播源太过难用。
- 网上现有的直播源太杂，且缺乏检测。
- 一些大源缺乏持续更新，如 `iptv-org`。

### 使用指南

**提前声明：出于自用，内含大量山东移动源，非对应线路的用户如遇这类标注请直接跳过！**

~~每次进行大更新后都会进行一次 release ，所以您可以在 jsDelivr 获得最新更新。~~
**现已不再进行人工 release！** 不过这并不妨碍您去 jsDelivr 获得最新更新。
（可能会出现编码问题，如有此类症状请 Issue 区提一下，附上所用软件。）

- 总合并直播源：
  - 带来源：[`https://cdn.jsdelivr.net/gh/abc1763613206/myiptv@latest/merged.txt`](https://cdn.jsdelivr.net/gh/abc1763613206/myiptv@latest/merged.txt)
  - 不带来源： [`https://cdn.jsdelivr.net/gh/abc1763613206/myiptv@latest/merged-simple.txt`](https://cdn.jsdelivr.net/gh/abc1763613206/myiptv@latest/merged-simple.txt)
- 分类
  - `cctv`（央视系频道）
    - 带来源：[`https://cdn.jsdelivr.net/gh/abc1763613206/myiptv@latest/groups/cctv.txt`](https://cdn.jsdelivr.net/gh/abc1763613206/myiptv@latest/groups/cctv.txt)
    - 不带来源：[`https://cdn.jsdelivr.net/gh/abc1763613206/myiptv@latest/groups/cctv-simple.txt`](https://cdn.jsdelivr.net/gh/abc1763613206/myiptv@latest/groups/cctv-simple.txt)
  - `weishi`（卫视频道）
    - 带来源：[`https://cdn.jsdelivr.net/gh/abc1763613206/myiptv@latest/groups/weishi.txt`](https://cdn.jsdelivr.net/gh/abc1763613206/myiptv@latest/groups/weishi.txt)
    - 不带来源：[`https://cdn.jsdelivr.net/gh/abc1763613206/myiptv@latest/groups/weishi-simple.txt`](https://cdn.jsdelivr.net/gh/abc1763613206/myiptv@latest/groups/weishi-simple.txt)
  - `difang`（地方频道）
    - 带来源：[`https://cdn.jsdelivr.net/gh/abc1763613206/myiptv@latest/groups/difang.txt`](https://cdn.jsdelivr.net/gh/abc1763613206/myiptv@latest/groups/difang.txt)
    - 不带来源：[`https://cdn.jsdelivr.net/gh/abc1763613206/myiptv@latest/groups/difang-simple.txt`](https://cdn.jsdelivr.net/gh/abc1763613206/myiptv@latest/groups/difang-simple.txt)
  - `special`（IPTV 等特色频道）
    - 带来源：[`https://cdn.jsdelivr.net/gh/abc1763613206/myiptv@latest/groups/special.txt`](https://cdn.jsdelivr.net/gh/abc1763613206/myiptv@latest/groups/special.txt)
    - 不带来源：[`https://cdn.jsdelivr.net/gh/abc1763613206/myiptv@latest/groups/special-simple.txt`](https://cdn.jsdelivr.net/gh/abc1763613206/myiptv@latest/groups/special-simple.txt)


关于分类：
目前的分类实在粗浅，如果有更好的分类方式欢迎指明。
| 标记 | 类别 | 备注 |
| ---- | ---- | ---- |  
| `cctv` | 央视系频道 | 包含 **CGTN**，**中央新影**系 |
| `weishi` | 卫视频道 | 一般是上星频道，额外包含**凤凰卫视**、**星空卫视**（其他地方的难以分类，会归入 `difang` 分支，如**台视**，**华视**，**ABC** |
| `difang` | 地方自建频道 | 名声较好的地方自建频道会归类到这里，如**金鹰卡通**；如果该频道有明显的地方自建特征也会归到这里， 如**上海这一刻**实景直播。另外收录一些官方非央视系频道（如**中国教育**、**中国交通**）|
| `special` | IPTV 等特色频道 | 主要收录前面难以分类的频道。主要包含地方 IPTV 特色频道（如**NewTV**系（包含地方频道如**NewTV吉林**）、**海看**系）、网络频道（如**第一财经**、**直播中国**）、有线扩展频道（如**弈坛春秋**） 、**测试频道/片段**、网络影院等（**包含不能观看的付费频道！**）|

-----

- **现已提供从 [ EPG 频道列表](http://epg.51zmt.top:8000/) 匹配的 `m3u8` 文件！详见 [epg/README.md](epg/README.md)**
- 如果您的播放器对编码有特殊要求或出现乱码问题，我们一并提供了[ **UTF-8 格式版本**](utf8/README.md)

### 注意事项(使用前必读)

- 由于目前主要还是自用，故打算每次手动生成。
- `merged` 为全部直播源，`groups` 文件夹里为各个直播源的分类。
- 带 `simple` 的为纯净格式**（不带来源与分辨率）**
- 目前~~只输出了 `txt` 格式~~，急着用的可以自行用 [Telelist](https://guihet.com/tvlive-telelist.html) 进行转换，其他格式慢慢写。
- 关于来源与命名：频道命名尽量遵循[ EPG 频道列表](http://epg.51zmt.top:8000/) 中的格式进行命名统一以确保正确匹配；来源多来自上游节目源，对于未知的多使用 IPIP 进行 IP 段标注。
- 对于不同直播源出现的不同ID，我尽量进行了命名统一，一些特殊的约定详见[命名映射表](MAPPING.md)
- ~~现阶段可以下载直播源上传至 [ EPG 频道列表](http://epg.51zmt.top:8000/)自动匹配节目表。~~
- 脚本所做的工作：通过 `requests` 和 `ffprobe` 检测直播源，后进行分类，最后用有效信息输出新的 `csv`。
- 比较重要的一点：我主要使用家机（当前是**山东移动**）进行检测，**直播源可用性对地区依赖较大**，有必要时请自行跑脚本检测。
- 山东移动的IP基本上全转内网了，因此**非山东**的可以**直接跳过**标注为「山东移动」的源！
- 补充一点：对于特定的源，一般来说可用性顺序：`同省同运营商>同省异运营商>外省同运营商>外省异运营商`。
- 脚本会去除仅音频/视频的直播源，所以该源**显然不含音频广播/无声直播**。
- 部分直播源限制连接数，如有需要请自行设置延时。
- 不加组播地址，理论上公网均可看。**部分源受地区所限不能观看，由于其自用的性质不予撤下，这时尝试请更换到其他源。**  
- `special` 分支内可能会包含一些**付费频道**，为保持完整性故不予筛掉，一般情况下**无法观看**，敬请谅解。
- 部分源会用方括号注明描述，做一个合格的搬运工。
- 通过人工筛选，尽量避免了粗略扫源造成的频道不对应情况。
- TODO：添加新格式、新直播源，优化脚本。

## 免责声明

请注意，本仓库中收集的节目源**全部来自网络**，仅供教学交流用途，具体版权**归各个版权方所有**。        
本仓库中并没有存储版权相关的视频文件，仅包含其他用户所提供的公开可用的视频流链接。且据我们了解，这些链接也是版权所有者故意公开的。    
如果这些节目源中的任何链接侵犯了您作为版权所有者的权利，您可以通过发送 Pull Request 或打开一个 Issue 来删除它们。     

另外请注意，我们**无法控制**链接的目的地及其要显示的内容，因此仅仅从我们的仓库中删除链接并不能从网络上彻底删除该内容。链接并不直接侵犯版权，且我们并不提供相关节目的复制，因此这并不是发送 DMCA 的正当理由。如果您要从网络上**彻底**删除这些内容，您应当联系该节目源的**原始提供者**以及**实际托管这些内容的网站主机**（不是 GitHub 本身，更不是该仓库的维护者）。

该免责声明参考了 [iptv-org/iptv](https://github.com/iptv-org/iptv) ，在此表示感谢。    


## 引用感谢
下面列出了**显式**引用节目源的来源，在此向提供者一并表示感谢：  
- [iptv-org/iptv](https://github.com/iptv-org/iptv)
- [北邮 IVI 测试](http://ivi.bupt.edu.cn/)
- [imDazui/Tvlist-awesome-m3u-m3u8](https://github.com/imDazui/Tvlist-awesome-m3u-m3u8)
- [SPX372928/MyIPTV](https://github.com/SPX372928/MyIPTV)
- [wcb1969/iptv](https://github.com/wcb1969/iptv)