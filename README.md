# zerotier-vpn-note
记录一下用zerotier上外网的优缺点

## Introduction
[zerotier](https://www.zerotier.com/) 是一个搭建虚拟局域网的工具。具体来说是将多个连上了互联网但是不在一个局域网的电脑连在一个局域网里。可以用来搭建搭VPN，远程控制（配合[nomachine](https://www.nomachine.com/)），联机游戏（如minecraft），访问家庭NAS等。zerotier最大的特点是P2P链接，不需要一个中间服务器转发流量（但是需要zerotier的根服务器做NAT，类似于DNS），或者是一个公网IP。所以通常来说这是一个快速且便宜的方案。

## deploy
参考https://github.com/aturl/awesome-anti-gfw/blob/master/ZeroTier/ZeroTier's_VPN.md

计划写一个脚本自动化这个过程，应该只需要用户输入一个zerotier的局域网代码。需要root权限。

如果想要搭建planet服务器来彻底不依赖zerotier的根服务器，可以用现成的docker，参考https://post.smzdm.com/p/apxkx2m7/

## Advantage
0. 不需要公网IP。也就是说，在墙外任何地方，只要你有一台，联网，不关机，可操作的电脑，就能当作服务器。不一定需要租一台虚拟主机，或是申请公网IP。
1. 在特殊时期也相对可靠。就算服务器IP ping不到了，只要zerotier的跟服务器还能访问，我们就还是可以访问到那台主机。如果你在墙内搭建了自己的zerotier planet，那就算zerotier的根服务器无法访问，你也依旧可以访问墙外的远程主机
2. 多功能。除了搭建路由器外，有了虚拟局域网也可以方便远程办公，或者是NAS，不再需要anydesk，公网IP，相对安全。
3. 客户端全平台可下载。官网提供Windows，MAC OS，linux，安卓的安装包，在墙内都能直接下载。app store之前有IOS版但是墙内下架了。

## Disadvantage
0. 使用UDP，听说有运营商限制UDP流量。
1. 对比公网IP直连，丢包率较高，延迟差不多。
2. 不搭建planet的话，如果zerotier网站本身被墙了，整个局域网应该就会失效。
