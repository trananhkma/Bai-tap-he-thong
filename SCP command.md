#Hướng dẫn sử dụng lệnh SCP
**SCP** (Secure Copy) là câu lệnh dùng để copy file và thư mục giữa localhost và remotehost hoặc giữa 2 remotehost.
Ở chế độ mặc định, giao thức truyền file này sẽ mã hóa fie trước khi gửi qua đường truyền, nó sử dụng thuật toán mã hóa AES-128. <br>



###I. Cú pháp câu lệnh
	scp filename username@destinationhost:destinationfolder
	
Có nghĩa là copy file nguồn *filename* đến thư mục đích *destinationfolder* tại máy đích có ip là *destinationhost* với tài khoản *username*

#####1. Copy một file từ remotehost về localhost
	scp username@remotehost:file_name /some/local/directory

#####2. Copy một file từ localhost lên remotehost:
  	scp file_name username@remotehost:/some/remote/directory
  
#####3. Copy thư mục foo vào thư mục bar:
  	scp -r foo username@remotehost:/some/remote/directory/bar
  
#####4. Copy 2 file lên remotehost:
	scp file1 file2 your_username@remotehost:/root
  
#####5. Copy file từ remotehost1 sang remotehost2:
	scp username@rh1.edu:/some/remote/directory/file_name username@rh2.edu:/some/remote/directory/


###II. Các tham số thường dùng:
#####1. Sử dụng tham số -v để hiển thị thông tin của quá trình truyền file với SCP:
Có thể sử dụng tham số **-v** để in ra thông tin debug. Những thông tin này có thể giúp người dùng kiểm tra, sửa lỗi kết nối, xác thực và giải quyết vấn đề.
	scp -v Label.pdf mrarianto@202.x.x.x:.

Output: 

	Executing: program /usr/bin/ssh host 202.x.x.x, user mrarianto, command scp -v -t .
	OpenSSH_6.0p1 Debian-3, OpenSSL 1.0.1c 10 May 2012
	debug1: Reading configuration data /etc/ssh/ssh_config
	debug1: /etc/ssh/ssh_config line 19: Applying options for *
	debug1: Connecting to 202.x.x.x [202.x.x.x] port 22.
	debug1: Connection established.
	debug1: Host '202.x.x.x' is known and matches the RSA host key.
	debug1: Found key in /home/pungki/.ssh/known_hosts:1
	debug1: ssh_rsa_verify: signature correct
	debug1: Next authentication method: password
	mrarianto@202.x.x.x's password:
	debug1: Authentication succeeded (password).
	Authenticated to 202.x.x.x ([202.x.x.x]:22).
	Sending file modes: C0770 3760348 Label.pdf
	Sink: C0770 3760348 Label.pdf
	Label.pdf 100% 3672KB 136.0KB/s 00:27
	Transferred: sent 3766304, received 3000 bytes, in 65.2 seconds
	Bytes per second: sent 57766.4, received 46.0
	debug1: Exit status 0
	
#####2. Hiện thị thời gian dự kiến, tốc độ kết nối
	scp -p Label.pdf mrarianto@202.x.x.x:.
	
Output:
	mrarianto@202.x.x.x's password:
	Label.pdf 100% 3672KB 126.6KB/s 00:29

#####3. Nén file trước khi truyền
Có thể thực hiện điều này với tham số **-C**. Nén file trước khi truyền sẽ giúp chuyển file nhanh hơn, đặc biệt với các file có dung lượng cao. Khi file đến đích sẽ tự động được giải nén để trở lại trạng thái ban đầu.
	
	scp -Cpv messages.log mrarianto@202.x.x.x:.
	
Output:
	
	Executing: program /usr/bin/ssh host 202.x.x.x, user mrarianto, command scp -v -p -t .
	OpenSSH_6.0p1 Debian-3, OpenSSL 1.0.1c 10 May 2012
	debug1: Reading configuration data /etc/ssh/ssh_config
	debug1: /etc/ssh/ssh_config line 19: Applying options for *
	debug1: Connecting to 202.x.x.x [202.x.x.x] port 22.
	debug1: Connection established.
	debug1: identity file /home/pungki/.ssh/id_rsa type -1
	debug1: Host '202.x.x.x' is known and matches the RSA host key.
	debug1: Found key in /home/pungki/.ssh/known_hosts:1
	debug1: ssh_rsa_verify: signature correct
	debug1: Next authentication method: publickey
	debug1: Trying private key: /home/pungki/.ssh/id_rsa
	debug1: Next authentication method: password
	mrarianto@202.x.x.x's password:
	debug1: Enabling compression at level 6.
	debug1: Authentication succeeded (password).
	Authenticated to 202.x.x.x ([202.x.x.x]:22).
	debug1: channel 0: new [client-session]
	debug1: Sending command: scp -v -p -t .
	File mtime 1323853868 atime 1380428748
	Sending file timestamps: T1323853868 0 1380428748 0
	Sink: T1323853868 0 1380428748 0
	Sending file modes: C0600 97517300 messages.log
	messages.log 100% 93MB 602.7KB/s 02:38
	Transferred: sent 8905840, received 15768 bytes, in 162.5 seconds
	Bytes per second: sent 54813.9, received 97.0
	debug1: Exit status 0
	debug1: compress outgoing: raw data 97571111, compressed 8806191, factor 0.09
	debug1: compress incoming: raw data 7885, compressed 3821, factor 0.48
	
#####4. Lựa chọn mã khác để mã hóa cho file:
Như đã nói ở trên, ở chế độ mặc đinh, SCP sử dụng mã AES-128 để mã hóa file. Ta có thể chọn loại mã hóa khác (VD như 3DES) như sau:
	scp -c 3des Label.pdf mrarianto@202.x.x.x:.
	
Chú ý: **-C** và **-c**

#####5. Hạn chế băng thông sử dụng:
Thực hiện điều này với tham số **-l**. Đơn vị của băng thông đường truyền là kilobit/giây. Như vậy, muốn hạn chế đường truyền là 50KB/s (Kil0byte/giây) thì phải đặt: 50 x 8 = 400 (kb/s)

	scp -l 400 Label.pdf mrarianto@202.x.x.x:.
	
#####6. Đặt cổng kết nối
Ở chế độ mặc định, SCP sử dụng cổng 22, ta có thể thay đổi cổng này với tham số **-P** như sau:
	
	scp -P 2249 Label.pdf mrarianto@202.x.x.x:.

Chú ý: **-P** chứ không phải **-p**

#####7. Copy tất cả file và thư mục trong thư mục chỉ định
Ta có thể dùng tham số **-r** để làm điều đó:
	scp -r documents mrarianto@202.x.x.x:.
	
Sau khi lệnh này chạy xong, ta sẽ tìm thấy thư mục *document* với toàn bộ file ở trong nó tại thư mục đích.

#####8. Tắt thông báo và đo lường trạng thái
Bình thường khi sử dụng SCP sẽ có những thông báo và đo lường mạng như băng thông, thời gian còn lại...<br>
Để tắt nó đi, ta sử dụng tham số **-q**

	scp -q Label.pdf mrarianto@202.x.x.x:.
	


Trên đây là một số cách sử dụng với SCP. Hy vọng nó có ích cho người mới! Chúc vui :)













	
	
	
	
	
	
	
	
	
	
	



