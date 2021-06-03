PATH_SPEEDTEST_LOG = "E:/speedtest_log.txt"
INSERT_SPEEDTEST = f"insert into spravka.dbo.speedtest_log(timestamp, download_bandwidth, upload_bandwidth, interface_internalIp, interface_externalIp, server_ip) " \
                   "values('{0}', {1}, {2}, '{3}', '{4}', '{5}')"