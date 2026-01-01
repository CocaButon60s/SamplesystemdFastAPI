import syslog

syslog.openlog("python_test",syslog.LOG_PID,syslog.LOG_USER)
syslog.syslog(syslog.LOG_WARNING, "test-message")
syslog.closelog()
