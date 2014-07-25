#Hướng dẫn sử dụng lệnh SCP
-*SCP* (Secure Copy) là câu lệnh dùng để copy file và thư mục giữa localhost và remotehost hoặc giữa 2 remotehost.
-Ở chế độ mặc định, giao thức truyền file này sẽ mã hóa fie trước khi gửi qua đường truyền, nó sử dụng thuật toán mã hóa 3DES. <br>
-
-####Sau đây là cú pháp câu lệnh:
-####
-#####Copy một file từ remotehost về localhost:
- *scp* **username***@***remote_host***:***file_name /some/local/directory** 
