#10 Câu lệnh IP hữu dụng để cấu hình mạng
Để cấu hình IP tĩnh, bạn sẽ phải sửa file cấu hình mạng. Bạn cần đăng nhập superuser để có toàn quyền thực hiện điều này.

***Note**: Bạn nên có kiến thức về IP, netmark, gateway... trước khi đọc bài này!*
###Đối với RHEL/CentOS/Fedora
Mở file cấu hình mạng. Ví dụ: Cấp phát IP cho cổng **eth0**:

    [root@tecmint ~]# vi /etc/sysconfig/network-scripts/ifcfg-eth0

Output:

    DEVICE="eth0"
    BOOTPROTO=static
    ONBOOT=yes
    TYPE="Ethernet"
    IPADDR=192.168.50.2
    NAME="System eth0"
    HWADDR=00:0C:29:28:FD:4C
    GATEWAY=192.168.50.1
###Đối với Ubuntu/Debian/Linux Mint:
Để cấp phát địa chỉ cho cổng **eth0**, bạn sửa file /etc/network/interfaces như sau:

    auto eth0
    iface eth0 inet static
    address 192.168.50.2
    netmask 255.255.255.0
    gateway 192.168.50.1

Sau đó khởi động lại card mạng:

    /etc/init.d/networking restart

##1. Cấp phát IP cho một cổng:

Ví dụ: Đặt IP 192.168.50.5 cho cổng eth1

    # ip addr add 192.168.50.5 dev eth1
###### 
    $ sudo ip addr add 192.168.50.5 dev eth1

***Chú ý:** *Nếu làm theo cách này thì cấu hình sẽ bị mất sau khi hệ thống khởi động lại.*

##2. Hiện thị địa chỉ IP:

Để xem các thông tin về mạng như: địa chỉ IP, địa chỉ MAC, sử dụng câu lệnh sau:

    # ip addr show
###### 
    $ sudo ip addr show

Màn hình output sẽ như sau:

    1: lo: <LOOPBACK,UP,LOWER_UP> mtu 16436 qdisc noqueue state UNKNOWN
        link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
        inet 127.0.0.1/8 scope host lo
        inet6 ::1/128 scope host
             valid_lft forever preferred_lft forever
    2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UNKNOWN qlen 1000
        link/ether 00:0c:29:28:fd:4c brd ff:ff:ff:ff:ff:ff
        inet 192.168.50.2/24 brd 192.168.50.255 scope global eth0
        inet6 fe80::20c:29ff:fe28:fd4c/64 scope link
            valid_lft forever preferred_lft forever
    3: eth1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UNKNOWN qlen 1000
        link/ether 00:0c:29:28:fd:56 brd ff:ff:ff:ff:ff:ff
        inet 192.168.50.5/24 scope global eth1
        inet6 fe80::20c:29ff:fe28:fd56/64 scope link
            valid_lft forever preferred_lft forever

##3. Xóa một địa chỉ IP:

Ví dụ: Xóa IP đã cấp lúc trước của cổng eth1:

    # ip addr del 192.168.50.5/24 dev eth1
###### 
    $ sudo ip addr del 192.168.50.5/24 dev eth1

##4. Bật một cổng mạng:

Điều này tương đương với đặt trạng thái cho cổng mạng là "up":
    # ip link set eth1 up
###### 
    $ sudo ip link set eth1 up

##5. Tắt một cổng mạng:

Điều này tương đương với đặt trạng thái cho cổng mạng là "down"

    # ip link set eth1 down
###### 
    $ sudo ip link set eth1 down

##6. Hiển thị bảng IP table:

Hiển thị thông tin về các dải mạng, đường đi của các gói tin trong mạng

    # ip route show
###### 
    $ sudo ip route show

Màn hình hiển thị:

    10.10.20.0/24 via 192.168.50.100 dev eth0
    192.168.160.0/24 dev eth1  proto kernel  scope link  src 192.168.160.130  metric 1
    192.168.50.0/24 dev eth0  proto kernel  scope link  src 192.168.50.2
    169.254.0.0/16 dev eth0  scope link  metric 1002
    default via 192.168.50.1 dev eth0  proto static

##7. Định tuyến tĩnh:

Đôi khi cần đặt định tuyến tĩnh thay cho động để định ra đường đi tối ưu hơn

    # ip route add 10.10.20.0/24 via 192.168.50.100 dev eth0
###### 
    $ sudo ip route add 10.10.20.0/24 via 192.168.50.100 dev eth0

##8. Xóa định tuyến tĩnh:


    # ip route del 10.10.20.0/24
###### 
    $ sudo ip route del 10.10.20.0/24

##9. Định tuyến tĩnh vĩnh viễn:

Tất cả cấu hình định tuyến ở trên sẽ mất sau khi hệ thống khởi động lại. Để tránh điều này, ta sửa file /etc/sysconfig/network-scripts/route-eth0. Ở đây là đặt IP 192.168.50.100 cho cổng eth0. Làm tương tự với các cổng khác.
###Đối với RHEL/CentOS/Fedora

    # vi /etc/sysconfig/network-scripts/route-eth0
    10.10.20.0/24 via 192.168.50.100 dev eth0

###Đối với Ubuntu/Debian/Linux Mint

Mở và sửa file /etc/network/interfaces như sau:
    $ sudo vi /etc/network/interfaces
###### 
    auto eth0
    iface eth0 inet static
    address 192.168.50.2
    netmask 255.255.255.0
    gateway 192.168.50.100
    #########{Static Route}###########
    up ip route add 10.10.20.0/24 via 192.168.50.100 dev eth0

Sau đó khởi động lại network để hệ thống áp dụng cấu hình mới.

    # /etc/init.d/network restart
###### 
    $ sudo /etc/init.d/network restart

##10. Đặt Default Gateway

Default gateway là cổng mạng đầu tiên gói tin phải đi qua khi muốn ra mạng khác. Ta có thể đặt như sau:

    # ip route add default via 192.168.50.100
###### 
    $ sudo ip route add default via 192.168.50.100

Có thể dùng "man ip" để biết thêm thông tin về các biến khác. Chúc vui! :)
