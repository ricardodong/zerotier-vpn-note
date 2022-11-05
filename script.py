import os

# install and join zerotier network
# os.system("curl -s https://install.zerotier.com | sudo bash")
# zerotier_network_id = input("请输入你的zerotier 网络 ID (一串16位的字母数字):\n")
# os.system("zerotier-cli join " + zerotier_network_id)

# enable ip forward
network_config_file = open("/etc/sysctl.conf", 'a+')
network_config_file.write("net.ipv4.ip_forward = 1\n")
network_config_file.close()
os.system("sysctl -p")

# find networks
server_networks = os.popen("ip link show", 'r', 1)
networks = server_networks.readlines()
zerotier_net = internet_net = ''
if len(networks) > 6:
    print("太多网络了！无法确定互联网连接")
    assert False
for net in networks:
    if 'link/' in net:
        continue
    elif 'lo' in net.split(' ')[1]:
        continue
    elif 'zt' in net.split(' ')[1]:
        zerotier_net = net.split(' ')[1].split(":")[0]
    else:
        internet_net = net.split(' ')[1].split(":")[0]
if zerotier_net == '' or internet_net == '':
    print("无法找到正确的网络")
    assert False

# config ip forward
os.system('iptables -t nat -A POSTROUTING -o ' + internet_net + ' -j MASQUERADE')
os.system('iptables -A FORWARD -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT')
os.system('iptables -A FORWARD -i ' + zerotier_net + ' -o ' + internet_net + ' -j ACCEPT')
