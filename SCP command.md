#Hướng dẫn sử dụng lệnh SCP
**SCP** (Secure Copy) là câu lệnh dùng để copy file và thư mục giữa localhost và remotehost hoặc giữa 2 remotehost.
Ở chế độ mặc định, giao thức truyền file này sẽ mã hóa fie trước khi gửi qua đường truyền, nó sử dụng thuật toán mã hóa 3DES. <br>

####Sau đây là cú pháp câu lệnh:
####
#####1. Copy một file từ remotehost về localhost:
	scp username@remotehost:file_name /some/local/directory

#####2. Copy một file từ localhost lên remotehost:
  	scp file_name username@remotehost:/some/remote/directory
  
#####3. Copy thư mục foo vào thư mục bar:
  	scp -r foo username@remotehost:/some/remote/directory/bar
  
#####4. Copy 2 file lên remotehost:
	scp file1 file2 your_username@remotehost:/root
  
#####5. Copy file từ remotehost1 sang remotehost2:
	scp username@rh1.edu:/some/remote/directory/file_name username@rh2.edu:/some/remote/directory/

#####6. Copy qua cổng 2246:
  	scp -P 2246 file_name username@remotehost.edu:/some/remote/directory
