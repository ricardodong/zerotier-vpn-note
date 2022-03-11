# zerotier-vpn-note
记录一下用zerotier上外网的优缺点

## Introduction
[zerotier](https://www.zerotier.com/) 是一个搭建虚拟局域网的工具（内网穿透）。具体来说是将多个连上了互联网但是不在一个局域网的

## Advantage
0. 不需要公网IP。也就是说，在墙外任何地方，只要你有一台，联网，不关机，可操作的电脑，就能当作服务器。不一定需要租一台虚拟主机。
1. 在特殊时期也相对可靠。就算服务器IP ping不到了，只要zerotier的跟服务器还能访问，我们就还是可以访问到那台主机。如果你在墙内搭建了自己的zerotier planet，那就算zerotier的根服务器无法访问，你也依旧可以访问墙外的远程主机
2. 多功能。除了搭建路由器外，有了虚拟局域网也可以方便远程办公，或者是NAS，不再需要anydesk，公网IP，相对安全。
3. 客户端全平台可下载。官网提供Windows，MAC OS，linux，安卓的安装包，在墙内都能直接下载。app store之前有IOS版但是墙内下架了。

## Disadvantage
