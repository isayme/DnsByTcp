@echo off

echo 1:设置为OpenDNS的DNS
echo 2:设置为Google的DNS
echo 3:设置为127.0.0.1

set /p sel=选择操作(1/3):

if not defined sel (
echo 设置为自动获取 ...
netsh interface ip set dns "无线网络连接" dhcp
pause
exit
)

if %sel% LEQ 1 (
echo 设置OpenDNS的DNS ...
netsh interface ip set dns "无线网络连接" static 208.67.222.222 primary
netsh interface ip add dns "无线网络连接" 208.67.220.220
)else if %sel% LEQ 2 (
echo 设置Google的DNS ...
netsh interface ip set dns "无线网络连接" static 8.8.8.8 primary
netsh interface ip add dns "无线网络连接" 8.8.4.4
)else if %sel% LEQ 3 (
echo 设置127.0.0.1 ...
netsh interface ip set dns "无线网络连接" static 127.0.0.1
)

pause