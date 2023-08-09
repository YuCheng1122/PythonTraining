#Logging 共有五個等級， DEBUG: 顯示程式日誌， INFO: 記錄一般發生的事件，WARNING: 雖然不會影響程式的執行但未來可能會導致問題發生
import logging

logging.basicConfig(level=logging.DEBUG)
logging.debug('logging message, DEBUG')